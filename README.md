# 📈 Crypto Project Screener

A full-stack web application that fetches, filters, and displays cryptocurrency data based on strict financial metrics. Built as a technical assignment to demonstrate clean architecture, API integration, and real-time frontend filtering.

## ✨ Features

**Backend (FastAPI)**
* **REST API:** Exposes a clean endpoint to retrieve cryptocurrency data.
* **CoinGecko Integration:** Fetches live market data using the CoinGecko API.
* **Multi-Layer Architecture:** Separates concerns into API Client, Business Logic (Service/Filters), Data Transfer Objects (DTOs), and Router (Controller).
* **Strict Filtering:** Filters projects based on Market Cap, Fully Diluted Valuation (FDV), 24h Volume, Total Value Locked (TVL), and Token Supply metrics.

**Frontend (React)**
* **Real-time Search:** Filter the fetched projects instantly by coin name or symbol.
* **Dynamic FDV Filter:** User-defined maximum FDV input to narrow down projects on the fly.
* **Sorting:** Sort the data dynamically by Market Cap or 24h Trading Volume.
* **Responsive UI:** Clean, simple, and functional table layout using Bootstrap.

---

## 🛠 Tech Stack

* **Backend:** Python 3, FastAPI, Pydantic, Requests, Uvicorn
* **Frontend:** React 18, Vite, Bootstrap
* **External API:** CoinGecko API (Demo Tier)

---

## 📂 Project Structure

The project follows an Enterprise-style layered architecture (similar to Spring Boot) to maintain the Single Responsibility Principle:

```text
CryptoCurrencyFetcher/
├── backend/
│   ├── api/
│   │   └── CryptoApi.py       # API Client for CoinGecko
│   ├── dto/
│   │   └── CryptoDTO.py       # Data Transfer Objects & Validation (Pydantic)
│   ├── service/
│   │   ├── CryptoService.py   # Orchestration and Data Mapping
│   │   └── FilterService.py   # Pure functions for business rule validation
│   └── main.py                # FastAPI Router (Controllers) & DI setup
│   
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # Main React component (UI, Fetching, Sorting)
│   │   └── main.jsx           # React entry point
│   ├── package.json           # Frontend dependencies
│   └── vite.config.js         # Vite configuration
└── README.md

```


## Setup Instructions


### 1. Backend (Python 3.9+)
```bash
cd backend
pip install fastapi uvicorn requests pydantic
uvicorn main:app --reload
```

### 2. Frontend (Node.js)
```bash
cd frontend
npm install
npm run dev
```

## Data retrieval issues 

The assignment requires filtering projects where FDV < 100M and Max Supply == Total Supply. 
Applying these exact filters to the Top 100 cryptocurrencies (Page 1 of the API) naturally yields an empty list, as top-tier projects far exceed $100M in valuation, 
and most large caps have differing supply metrics. 

As a temporary workaround, we can adjust alter the function 
def has_valid_fdv(coin: Dict[str, Any]) -> bool:
    return (coin.get("fully_diluted_valuation") or float('inf')) < 100_000_000

inside of the FilterService.py file. And lower the threshold for fdv from 100m to 0.