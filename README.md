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