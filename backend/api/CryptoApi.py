import requests
import os
from typing import List, Dict, Any

class CryptoAPI:
    BASE_URL = "https://api.coingecko.com/api/v3"

    def fetch_markets(self) -> List[Dict[str, Any]]:
        url = f"{self.BASE_URL}/coins/markets"

        headers = {
            "x-cg-demo-api-key": os.getenv("COINGECKO_API_KEY", "CG-SjfZfKH7WyXWrkSMqEyFRhcJ")
        }

        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 250,
            "page": 1,
            "sparkline": "false"
        }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()