from typing import Dict, Any, Callable

CryptoPredicate = Callable[[Dict[str, Any]], bool]

def has_valid_mcap(coin: Dict[str, Any]) -> bool:
    return (coin.get("market_cap") or 0) > 0

def has_valid_fdv(coin: Dict[str, Any]) -> bool:
    return (coin.get("fully_diluted_valuation") or float('inf')) < 100_000_000

def has_valid_volume(coin: Dict[str, Any]) -> bool:
    return (coin.get("total_volume") or 0) > 50_000

def has_matching_supply(coin: Dict[str, Any]) -> bool:
    total = coin.get("total_supply")
    max_s = coin.get("max_supply")
    return max_s is not None and total is not None and max_s == total

def has_valid_tvl_and_preview(coin: Dict[str, Any]) -> bool:
    is_preview = coin.get("preview_listing", True)
    tvl = coin.get("tvl") or 50001
    return is_preview and (tvl > 50_000)


DEFAULT_FILTERS = [
    has_valid_mcap,
    has_valid_fdv,
    has_valid_volume,
    has_matching_supply,
    has_valid_tvl_and_preview
]