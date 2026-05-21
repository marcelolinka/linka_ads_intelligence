from fastapi import APIRouter, Query

router = APIRouter(prefix="/mock")

MOCK_ACCOUNTS = [
    {"id": "1234567890", "name": "Cliente A", "currency": "BRL", "timezone": "America/Sao_Paulo"},
    {"id": "2345678901", "name": "Cliente B", "currency": "BRL", "timezone": "America/Sao_Paulo"},
    {"id": "3456789012", "name": "Cliente C", "currency": "BRL", "timezone": "America/Sao_Paulo"},
    {"id": "4567890123", "name": "Cliente D", "currency": "BRL", "timezone": "America/Sao_Paulo"},
    {"id": "5678901234", "name": "Cliente E", "currency": "BRL", "timezone": "America/Sao_Paulo"},
]

MOCK_CAMPAIGNS = [
    {"name": "SHOPPING | Todos os Produtos",   "tipo": "Shopping",   "roas": 17.62, "conv": 3.19, "cpa": 29.43,  "receita": 3590133, "custo": 203778, "impLost": 53.2, "isBrand": False},
    {"name": "SEARCH | Brand | BR",            "tipo": "Search",     "roas": 34.10, "conv": 8.40, "cpa": 12.80,  "receita": 980200,  "custo": 28738,  "impLost": 35.1, "isBrand": True},
    {"name": "PMAX | Categoria Principal",     "tipo": "PMax",       "roas": 12.30, "conv": 2.10, "cpa": 48.20,  "receita": 610400,  "custo": 49625,  "impLost": 22.4, "isBrand": False},
    {"name": "SEARCH | Categoria A",           "tipo": "Search",     "roas": 10.80, "conv": 1.95, "cpa": 52.10,  "receita": 421600,  "custo": 39037,  "impLost": 18.7, "isBrand": False},
    {"name": "SHOPPING | Linha Premium",       "tipo": "Shopping",   "roas": 14.50, "conv": 2.80, "cpa": 35.70,  "receita": 389000,  "custo": 26828,  "impLost": 28.9, "isBrand": False},
    {"name": "DEMAND GEN | Remarketing",       "tipo": "Demand Gen", "roas": 3.20,  "conv": 0.85, "cpa": 118.00, "receita": 96000,   "custo": 30000,  "impLost": 0.0,  "isBrand": False},
    {"name": "SEARCH | Categoria B",           "tipo": "Search",     "roas": 4.10,  "conv": 1.20, "cpa": 83.00,  "receita": 74000,   "custo": 18049,  "impLost": 12.3, "isBrand": False},
    {"name": "PMAX | Categoria B",             "tipo": "PMax",       "roas": 8.90,  "conv": 1.60, "cpa": 62.50,  "receita": 178000,  "custo": 20000,  "impLost": 15.6, "isBrand": False},
    {"name": "SEARCH | Linha Secundária",      "tipo": "Search",     "roas": 11.20, "conv": 2.05, "cpa": 48.80,  "receita": 201600,  "custo": 18000,  "impLost": 9.4,  "isBrand": False},
    {"name": "SHOPPING | Acessórios",          "tipo": "Shopping",   "roas": 9.40,  "conv": 1.75, "cpa": 57.10,  "receita": 141000,  "custo": 15000,  "impLost": 7.8,  "isBrand": False},
    {"name": "DSA | Antiga Text",              "tipo": "Search",     "roas": 6.10,  "conv": 0.95, "cpa": 105.00, "receita": 85400,   "custo": 14000,  "impLost": 0.0,  "isBrand": False},
    {"name": "SEARCH | Linha Vestuário",       "tipo": "Search",     "roas": 13.70, "conv": 2.40, "cpa": 41.70,  "receita": 164400,  "custo": 12000,  "impLost": 19.2, "isBrand": False},
    {"name": "DEMAND GEN | Prospecção",        "tipo": "Demand Gen", "roas": 5.80,  "conv": 1.10, "cpa": 91.00,  "receita": 69600,   "custo": 12000,  "impLost": 0.0,  "isBrand": False},
    {"name": "PMAX | Acessórios",              "tipo": "PMax",       "roas": 10.10, "conv": 1.85, "cpa": 54.10,  "receita": 121200,  "custo": 12000,  "impLost": 11.0, "isBrand": False},
    {"name": "SEARCH | Brand | Concorrentes",  "tipo": "Search",     "roas": 7.30,  "conv": 1.30, "cpa": 77.00,  "receita": 87600,   "custo": 12000,  "impLost": 0.0,  "isBrand": True},
    {"name": "SHOPPING | Linha Calçados",      "tipo": "Shopping",   "roas": 16.20, "conv": 3.10, "cpa": 32.30,  "receita": 194400,  "custo": 12000,  "impLost": 31.5, "isBrand": False},
    {"name": "SEARCH | Sazonais",              "tipo": "Search",     "roas": 9.80,  "conv": 1.70, "cpa": 58.80,  "receita": 117600,  "custo": 12000,  "impLost": 14.2, "isBrand": False},
    {"name": "DEMAND GEN | Awareness",         "tipo": "Demand Gen", "roas": 2.90,  "conv": 0.70, "cpa": 143.00, "receita": 34800,   "custo": 12000,  "impLost": 0.0,  "isBrand": False},
    {"name": "PMAX | Linha C",                 "tipo": "PMax",       "roas": 11.60, "conv": 2.20, "cpa": 45.50,  "receita": 139200,  "custo": 12000,  "impLost": 16.8, "isBrand": False},
    {"name": "SEARCH | Suporte",               "tipo": "Search",     "roas": 8.40,  "conv": 1.55, "cpa": 64.50,  "receita": 100800,  "custo": 12000,  "impLost": 8.1,  "isBrand": False},
]

@router.get("/accounts")
def mock_accounts():
    return {"accounts": MOCK_ACCOUNTS}

@router.get("/campaigns/{customer_id}")
def mock_campaigns(
    customer_id: str,
    date_range: str = Query(default="THIS_MONTH"),
):
    total_cost = sum(c["custo"] for c in MOCK_CAMPAIGNS)
    campaigns = [
        {
            **c,
            "status": "limitado" if c["impLost"] > 10 else "qualificado",
            "impLostReal": c["impLost"],
            "brandCap": None,
            "rescued": False,
            "isNew": False,
        }
        for c in MOCK_CAMPAIGNS
    ]
    return {
        "customer_id": customer_id,
        "date_range": date_range,
        "total_cost": round(total_cost, 2),
        "campaigns": campaigns,
    }
