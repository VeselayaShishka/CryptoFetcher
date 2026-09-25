from typing import List
from api.CryptoApi import CryptoAPI
from dto.CryptoDTO import CryptoDTO
from service.FilterService import DEFAULT_FILTERS, CryptoPredicate

class CryptoService:
        def __init__(self, filters: List[CryptoPredicate] = None):
            self.client = CryptoAPI()
            self.filters = filters or DEFAULT_FILTERS

        def get_filtered_projects(self) -> List[CryptoDTO]:
            raw_data = self.client.fetch_markets()

            def is_valid(coin: dict) -> bool:
                return all(predicate(coin) for predicate in self.filters)

            valid_coins = filter(is_valid, raw_data)
            return [CryptoDTO(**coin) for coin in valid_coins]