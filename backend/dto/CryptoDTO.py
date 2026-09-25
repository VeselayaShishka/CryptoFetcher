from pydantic import BaseModel
from typing import Optional

class CryptoDTO(BaseModel):
    id: str
    symbol: str
    name: str
    market_cap: float
    fully_diluted_valuation: Optional[float] = None
    total_volume: float
    total_supply: Optional[float] = None
    max_supply: Optional[float] = None
    tvl: Optional[float] = None
    preview_listing: Optional[bool] = False