import os
from google.ads.googleads.client import GoogleAdsClient
from dotenv import load_dotenv

load_dotenv()

def get_client() -> GoogleAdsClient:
    config = {
        "developer_token": os.getenv("DEVELOPER_TOKEN"),
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "refresh_token": os.getenv("REFRESH_TOKEN"),
        "login_customer_id": os.getenv("MCC_CUSTOMER_ID", "").replace("-", ""),
        "use_proto_plus": True,
    }
    return GoogleAdsClient.load_from_dict(config)
