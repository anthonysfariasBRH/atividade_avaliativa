"""FastAPI app que expõe o endpoint de cálculo de desconto."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.discount import DiscountError, calculate_final_price

app = FastAPI(title="Discount API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class DiscountRequest(BaseModel):
    price: float = Field(..., description="Preço original do produto")
    discount: float = Field(..., description="Porcentagem de desconto (0-100)")


class DiscountResponse(BaseModel):
    final_price: float


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/discount", response_model=DiscountResponse)
def post_discount(payload: DiscountRequest) -> DiscountResponse:
    try:
        final_price = calculate_final_price(payload.price, payload.discount)
    except DiscountError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return DiscountResponse(final_price=final_price)
