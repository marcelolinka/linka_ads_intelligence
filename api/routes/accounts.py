import os
from fastapi import APIRouter, HTTPException
from google_ads_client import get_client

router = APIRouter()

@router.get("/accounts")
def list_accounts():
    """Lista todos os clientes acessíveis via MCC."""
    client = get_client()
    mcc_id = os.getenv("MCC_CUSTOMER_ID", "").replace("-", "")

    service = client.get_service("CustomerService")
    accessible = service.list_accessible_customers()

    ga_service = client.get_service("GoogleAdsService")
    accounts = []

    for resource_name in accessible.resource_names:
        customer_id = resource_name.split("/")[-1]
        if customer_id == mcc_id:
            continue

        query = """
            SELECT
              customer.id,
              customer.descriptive_name,
              customer.currency_code,
              customer.time_zone,
              customer.manager
            FROM customer
            LIMIT 1
        """
        try:
            response = ga_service.search(customer_id=customer_id, query=query)
            for row in response:
                c = row.customer
                if not c.manager:
                    accounts.append({
                        "id": str(c.id),
                        "name": c.descriptive_name,
                        "currency": c.currency_code,
                        "timezone": c.time_zone,
                    })
        except Exception:
            continue

    accounts.sort(key=lambda x: x["name"])
    return {"accounts": accounts}
