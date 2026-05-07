"""Testes automatizados do cálculo de desconto e do endpoint HTTP."""

import pytest
from fastapi.testclient import TestClient

from app.discount import DiscountError, calculate_final_price
from app.main import app

client = TestClient(app)


class TestCalculateFinalPrice:
    """Testes da função pura de cálculo."""

    def test_applies_ten_percent_discount(self):
        assert calculate_final_price(100, 10) == 90

    def test_applies_twenty_five_percent_discount(self):
        assert calculate_final_price(200, 25) == 150

    def test_no_discount_returns_original_price(self):
        assert calculate_final_price(99.90, 0) == 99.90

    def test_full_discount_returns_zero(self):
        assert calculate_final_price(50, 100) == 0

    def test_keeps_two_decimal_places(self):
        assert calculate_final_price(19.99, 15) == 16.99

    def test_negative_price_raises(self):
        with pytest.raises(DiscountError):
            calculate_final_price(-10, 5)

    def test_zero_price_raises(self):
        with pytest.raises(DiscountError):
            calculate_final_price(0, 10)

    def test_discount_above_100_raises(self):
        with pytest.raises(DiscountError):
            calculate_final_price(100, 150)

    def test_negative_discount_raises(self):
        with pytest.raises(DiscountError):
            calculate_final_price(100, -5)


class TestDiscountEndpoint:
    """Testes de integração HTTP do endpoint /discount."""

    def test_valid_request_returns_final_price(self):
        response = client.post("/discount", json={"price": 100, "discount": 10})
        assert response.status_code == 200
        assert response.json() == {"final_price": 90}

    def test_request_with_decimal_values(self):
        response = client.post("/discount", json={"price": 250.0, "discount": 20})
        assert response.status_code == 200
        assert response.json() == {"final_price": 200}

    def test_invalid_price_returns_400(self):
        response = client.post("/discount", json={"price": -1, "discount": 10})
        assert response.status_code == 400

    def test_invalid_discount_returns_400(self):
        response = client.post("/discount", json={"price": 100, "discount": 120})
        assert response.status_code == 400

    def test_health_endpoint(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
