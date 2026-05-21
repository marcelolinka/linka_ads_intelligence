from fastapi import APIRouter, Query
from google_ads_client import get_client

router = APIRouter()

CHANNEL_TYPE_MAP = {
    "SEARCH": "Search",
    "DISPLAY": "Display",
    "SHOPPING": "Shopping",
    "VIDEO": "Demand Gen",
    "PERFORMANCE_MAX": "PMax",
    "SMART": "PMax",
    "DISCOVERY": "Demand Gen",
}

@router.get("/campaigns/{customer_id}")
def get_campaigns(
    customer_id: str,
    date_range: str = Query(default="THIS_MONTH", description="Ex: THIS_MONTH, LAST_30_DAYS, LAST_90_DAYS"),
):
    """
    Retorna métricas de campanha para um cliente.
    date_range aceita qualquer literal do Google Ads (THIS_MONTH, LAST_30_DAYS, etc.)
    """
    client = get_client()
    ga_service = client.get_service("GoogleAdsService")
    cid = customer_id.replace("-", "")

    query = f"""
        SELECT
          campaign.id,
          campaign.name,
          campaign.advertising_channel_type,
          campaign.status,
          campaign_budget.amount_micros,
          metrics.cost_micros,
          metrics.conversions_value,
          metrics.conversions,
          metrics.cost_per_conversion,
          metrics.search_budget_lost_impression_share,
          campaign.labels
        FROM campaign
        WHERE campaign.status != 'REMOVED'
          AND segments.date DURING {date_range}
        ORDER BY metrics.cost_micros DESC
    """

    response = ga_service.search(customer_id=cid, query=query)

    total_cost = 0
    campaigns = []

    for row in response:
        c = row.campaign
        m = row.metrics
        b = row.campaign_budget

        cost = m.cost_micros / 1_000_000
        conv_value = m.conversions_value
        conv = m.conversions
        cpa = m.cost_per_conversion / 1_000_000 if m.cost_per_conversion else 0
        roas = round(conv_value / cost, 2) if cost > 0 else 0
        conv_rate = round((conv / (cost / cpa)) * 100, 2) if cpa > 0 and cost > 0 else 0
        imp_lost = round(m.search_budget_lost_impression_share * 100, 1) if m.search_budget_lost_impression_share else 0
        budget = b.amount_micros / 1_000_000 if b.amount_micros else 0

        channel = CHANNEL_TYPE_MAP.get(c.advertising_channel_type.name, "Search")

        # Detecta Brand Search pelo nome
        name_upper = c.name.upper()
        is_brand = any(w in name_upper for w in ["BRAND", "BR |", "| BR", "MARCA"])

        campaigns.append({
            "name": c.name,
            "tipo": channel,
            "roas": roas,
            "conv": conv_rate,
            "cpa": round(cpa, 2),
            "receita": round(conv_value, 2),
            "custo": round(cost, 2),
            "status": "limitado" if imp_lost > 10 else "qualificado",
            "impLost": imp_lost,
            "impLostReal": imp_lost,
            "isBrand": is_brand,
            "brandCap": None,
            "rescued": False,
            "isNew": False,
            "dailyBudget": round(budget, 2),
        })
        total_cost += cost

    return {
        "customer_id": customer_id,
        "date_range": date_range,
        "total_cost": round(total_cost, 2),
        "campaigns": campaigns,
    }
