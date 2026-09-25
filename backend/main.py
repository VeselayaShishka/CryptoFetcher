from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from service.CryptoService import CryptoService
from dto.CryptoDTO import CryptoDTO
from typing import List

app = FastAPI(title="Crypto Filter API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

def get_crypto_service() -> CryptoService:
    return CryptoService()

@app.get("/api/crypto", response_model=List[CryptoDTO])
def get_crypto_data(service: CryptoService = Depends(get_crypto_service)):
    return service.get_filtered_projects()