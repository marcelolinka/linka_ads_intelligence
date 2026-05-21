"""
Execute este script UMA VEZ para gerar o refresh_token.
python auth_setup.py

Depois copie o refresh_token para o .env.
"""
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

SCOPES = ["https://www.googleapis.com/auth/adwords"]

client_config = {
    "installed": {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
    }
}

flow = InstalledAppFlow.from_client_config(client_config, scopes=SCOPES)
credentials = flow.run_local_server(port=8085, prompt="consent", access_type="offline")

print("\n✅ Autenticação concluída!")
print(f"\nRefresh Token:\n{credentials.refresh_token}")
print("\nCopie o valor acima para o campo REFRESH_TOKEN no arquivo .env")
