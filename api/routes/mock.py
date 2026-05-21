from fastapi import APIRouter, Query

router = APIRouter(prefix="/mock")

MOCK_ACCOUNTS = [
    {"id": "1234567890", "name": "Cliente A", "currency": "BRL", "timezone": "America/Sao_Paulo"},
    {"id": "2345678901", "name": "Cliente B", "currency": "BRL", "timezone": "America/Sao_Paulo"},
    {"id": "3456789012", "name": "Cliente C", "currency": "BRL", "timezone": "America/Sao_Paulo"},
    {"id": "4567890123", "name": "Cliente D", "currency": "BRL", "timezone": "America/Sao_Paulo"},
    {"id": "5678901234", "name": "Cliente E", "currency": "BRL", "timezone": "America/Sao_Paulo"},
]

MOCK_CAMPAIGNS = {
    "1234567890": [  # Cliente A — e-commerce grande, shopping forte
        {"name": "SHOPPING | Todos os Produtos",  "tipo": "Shopping",   "roas": 17.62, "conv": 3.19, "cpa": 29.43,  "receita": 3590133, "custo": 203778, "impLost": 53.2, "isBrand": False},
        {"name": "SEARCH | Brand | BR",           "tipo": "Search",     "roas": 34.10, "conv": 8.40, "cpa": 12.80,  "receita": 980200,  "custo": 28738,  "impLost": 35.1, "isBrand": True},
        {"name": "PMAX | Categoria Principal",    "tipo": "PMax",       "roas": 12.30, "conv": 2.10, "cpa": 48.20,  "receita": 610400,  "custo": 49625,  "impLost": 22.4, "isBrand": False},
        {"name": "SHOPPING | Linha Premium",      "tipo": "Shopping",   "roas": 14.50, "conv": 2.80, "cpa": 35.70,  "receita": 389000,  "custo": 26828,  "impLost": 28.9, "isBrand": False},
        {"name": "SEARCH | Categoria A",          "tipo": "Search",     "roas": 10.80, "conv": 1.95, "cpa": 52.10,  "receita": 421600,  "custo": 39037,  "impLost": 18.7, "isBrand": False},
        {"name": "SHOPPING | Linha Calçados",     "tipo": "Shopping",   "roas": 16.20, "conv": 3.10, "cpa": 32.30,  "receita": 194400,  "custo": 12000,  "impLost": 31.5, "isBrand": False},
        {"name": "DEMAND GEN | Remarketing",      "tipo": "Demand Gen", "roas": 3.20,  "conv": 0.85, "cpa": 118.00, "receita": 96000,   "custo": 30000,  "impLost": 0.0,  "isBrand": False},
        {"name": "DSA | Antiga Text",             "tipo": "Search",     "roas": 6.10,  "conv": 0.95, "cpa": 105.00, "receita": 85400,   "custo": 14000,  "impLost": 0.0,  "isBrand": False},
    ],
    "2345678901": [  # Cliente B — search pesado, sem shopping
        {"name": "SEARCH | Brand | BR",           "tipo": "Search",     "roas": 28.40, "conv": 7.20, "cpa": 18.50,  "receita": 710000,  "custo": 25000,  "impLost": 41.0, "isBrand": True},
        {"name": "SEARCH | Produto Principal",    "tipo": "Search",     "roas": 11.50, "conv": 2.30, "cpa": 43.50,  "receita": 460000,  "custo": 40000,  "impLost": 29.3, "isBrand": False},
        {"name": "SEARCH | Concorrentes",         "tipo": "Search",     "roas": 7.80,  "conv": 1.40, "cpa": 71.40,  "receita": 156000,  "custo": 20000,  "impLost": 8.5,  "isBrand": True},
        {"name": "PMAX | Geral",                  "tipo": "PMax",       "roas": 9.20,  "conv": 1.70, "cpa": 58.80,  "receita": 184000,  "custo": 20000,  "impLost": 17.6, "isBrand": False},
        {"name": "SEARCH | Categoria B",          "tipo": "Search",     "roas": 13.10, "conv": 2.60, "cpa": 38.50,  "receita": 262000,  "custo": 20000,  "impLost": 22.8, "isBrand": False},
        {"name": "DEMAND GEN | Prospecção",       "tipo": "Demand Gen", "roas": 4.50,  "conv": 1.00, "cpa": 100.00, "receita": 90000,   "custo": 20000,  "impLost": 0.0,  "isBrand": False},
        {"name": "SEARCH | Categoria C",          "tipo": "Search",     "roas": 5.60,  "conv": 1.10, "cpa": 90.90,  "receita": 67200,   "custo": 12000,  "impLost": 6.2,  "isBrand": False},
    ],
    "3456789012": [  # Cliente C — performance max dominante, menor escala
        {"name": "PMAX | Campanha Principal",     "tipo": "PMax",       "roas": 15.80, "conv": 3.40, "cpa": 29.40,  "receita": 948000,  "custo": 60000,  "impLost": 44.7, "isBrand": False},
        {"name": "PMAX | Secundária",             "tipo": "PMax",       "roas": 10.20, "conv": 2.00, "cpa": 50.00,  "receita": 306000,  "custo": 30000,  "impLost": 19.3, "isBrand": False},
        {"name": "SEARCH | Brand",                "tipo": "Search",     "roas": 41.00, "conv": 9.10, "cpa": 11.00,  "receita": 492000,  "custo": 12000,  "impLost": 55.2, "isBrand": True},
        {"name": "SHOPPING | Produtos",           "tipo": "Shopping",   "roas": 8.30,  "conv": 1.50, "cpa": 66.70,  "receita": 124500,  "custo": 15000,  "impLost": 12.0, "isBrand": False},
        {"name": "DEMAND GEN | Remarketing",      "tipo": "Demand Gen", "roas": 2.80,  "conv": 0.60, "cpa": 166.70, "receita": 42000,   "custo": 15000,  "impLost": 0.0,  "isBrand": False},
        {"name": "PMAX | Novos Produtos",         "tipo": "PMax",       "roas": 6.40,  "conv": 1.20, "cpa": 83.30,  "receita": 76800,   "custo": 12000,  "impLost": 9.8,  "isBrand": False},
    ],
    "4567890123": [  # Cliente D — mix equilibrado, ROAS médio
        {"name": "SEARCH | Brand | BR",           "tipo": "Search",     "roas": 22.50, "conv": 6.00, "cpa": 22.20,  "receita": 337500,  "custo": 15000,  "impLost": 28.4, "isBrand": True},
        {"name": "SHOPPING | Catálogo Geral",     "tipo": "Shopping",   "roas": 11.40, "conv": 2.20, "cpa": 45.50,  "receita": 342000,  "custo": 30000,  "impLost": 24.6, "isBrand": False},
        {"name": "SEARCH | Linha A",              "tipo": "Search",     "roas": 9.70,  "conv": 1.80, "cpa": 55.60,  "receita": 194000,  "custo": 20000,  "impLost": 16.1, "isBrand": False},
        {"name": "PMAX | Geral",                  "tipo": "PMax",       "roas": 12.80, "conv": 2.50, "cpa": 40.00,  "receita": 384000,  "custo": 30000,  "impLost": 33.2, "isBrand": False},
        {"name": "SEARCH | Linha B",              "tipo": "Search",     "roas": 7.20,  "conv": 1.30, "cpa": 76.90,  "receita": 108000,  "custo": 15000,  "impLost": 7.3,  "isBrand": False},
        {"name": "DEMAND GEN | Awareness",        "tipo": "Demand Gen", "roas": 3.60,  "conv": 0.90, "cpa": 111.10, "receita": 54000,   "custo": 15000,  "impLost": 0.0,  "isBrand": False},
        {"name": "SEARCH | Sazonais",             "tipo": "Search",     "roas": 8.90,  "conv": 1.60, "cpa": 62.50,  "receita": 89000,   "custo": 10000,  "impLost": 11.4, "isBrand": False},
        {"name": "SHOPPING | Linha Premium",      "tipo": "Shopping",   "roas": 18.30, "conv": 3.50, "cpa": 28.60,  "receita": 183000,  "custo": 10000,  "impLost": 38.9, "isBrand": False},
    ],
    "5678901234": [  # Cliente E — conta em dificuldade, ROAS baixo geral
        {"name": "SEARCH | Brand",                "tipo": "Search",     "roas": 19.00, "conv": 5.10, "cpa": 19.60,  "receita": 190000,  "custo": 10000,  "impLost": 22.0, "isBrand": True},
        {"name": "SEARCH | Produto A",            "tipo": "Search",     "roas": 5.20,  "conv": 1.00, "cpa": 96.20,  "receita": 78000,   "custo": 15000,  "impLost": 5.1,  "isBrand": False},
        {"name": "SEARCH | Produto B",            "tipo": "Search",     "roas": 4.80,  "conv": 0.90, "cpa": 111.10, "receita": 72000,   "custo": 15000,  "impLost": 3.8,  "isBrand": False},
        {"name": "PMAX | Geral",                  "tipo": "PMax",       "roas": 6.90,  "conv": 1.30, "cpa": 76.90,  "receita": 103500,  "custo": 15000,  "impLost": 14.2, "isBrand": False},
        {"name": "SHOPPING | Produtos",           "tipo": "Shopping",   "roas": 7.40,  "conv": 1.40, "cpa": 71.40,  "receita": 111000,  "custo": 15000,  "impLost": 10.5, "isBrand": False},
        {"name": "DEMAND GEN | Remarketing",      "tipo": "Demand Gen", "roas": 2.10,  "conv": 0.50, "cpa": 200.00, "receita": 31500,   "custo": 15000,  "impLost": 0.0,  "isBrand": False},
        {"name": "SEARCH | Genérico",             "tipo": "Search",     "roas": 3.40,  "conv": 0.70, "cpa": 142.90, "receita": 51000,   "custo": 15000,  "impLost": 2.1,  "isBrand": False},
    ],
}


# Verba mock por cliente (saldo restante simulado)
MOCK_SALDO = {
    "1234567890": 102000,
    "2345678901":  58000,
    "3456789012":  74000,
    "4567890123":  43000,
    "5678901234":  31000,
}
MOCK_DIAS = 11  # dias restantes simulados


def escala_score(c: dict) -> int:
    s = 0
    roas = c["roas"]
    if roas >= 16:   s += 4
    elif roas >= 12: s += 3
    elif roas >= 8:  s += 2
    else:            s += 1
    il = c["impLost"]
    if il > 0:
        if il >= 40:   s += 4
        elif il >= 20: s += 3
        elif il >= 10: s += 2
        else:          s += 1
    else:
        if c["impLost"] == 0 and c.get("status_raw") == "limitado":
            s += 2
    if c["receita"] > 1_000_000: s += 2
    elif c["receita"] > 300_000: s += 1
    return min(10, s)


def status_badge(c: dict) -> str:
    if c.get("rescued") or c.get("isNew"): return "Resgatada"
    if c["roas"] < 8:  return "Reduzir"
    if c["roas"] < 10: return "Monitorar"
    if c["roas"] >= 14 and c["impLost"] >= 15: return "Expandir"
    return "Manter"


@router.get("/accounts")
def mock_accounts():
    return {"accounts": MOCK_ACCOUNTS}


@router.get("/campaigns/{customer_id}")
def mock_campaigns(
    customer_id: str,
    date_range: str = Query(default="THIS_MONTH"),
):
    camps_raw = MOCK_CAMPAIGNS.get(customer_id, [])
    saldo = MOCK_SALDO.get(customer_id, 50000)
    dias  = MOCK_DIAS

    # calcula potencial e score proporcional
    potenciais = [escala_score(c) for c in camps_raw]
    total_score = sum(potenciais) or 1

    campaigns = []
    for c, pot in zip(camps_raw, potenciais):
        sugestao   = round(saldo * (pot / total_score), 2)
        verba_dia  = round(sugestao / dias, 2)
        campaigns.append({
            **c,
            "status":      "limitado" if c["impLost"] > 10 else "qualificado",
            "impLostReal": c["impLost"],
            "brandCap":    None,
            "rescued":     False,
            "isNew":       False,
            "potencial":   pot,
            "sugestao":    sugestao,
            "verba_dia":   verba_dia,
            "badge":       status_badge(c),
        })

    total_cost = sum(c["custo"] for c in camps_raw)
    return {
        "customer_id": customer_id,
        "date_range":  date_range,
        "total_cost":  round(total_cost, 2),
        "saldo":       saldo,
        "dias":        dias,
        "campaigns":   campaigns,
    }
