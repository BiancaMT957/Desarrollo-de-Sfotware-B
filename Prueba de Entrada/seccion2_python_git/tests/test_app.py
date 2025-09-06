# tests/test_app.py
import pytest
from fastapi.testclient import TestClient
from app import app  # asegúrate de que tu FastAPI app está en app.py

client = TestClient(app)

def test_sum_normal():
    """Caso normal: lista de números con varios elementos"""
    response = client.post("/calculate", json={"numbers": [1, 2, 3]})
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 3
    assert data["sum"] == 6.0
    assert data["avg"] == 2.0

def test_sum_empty_list():
    """Caso borde: lista vacía"""
    response = client.post("/calculate", json={"numbers": []})
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 0
    assert data["sum"] == 0.0
    assert data["avg"] == 0.0

def test_sum_invalid_input():
    """Caso de error: input no válido (no es lista de números)"""
    response = client.post("/calculate", json={"numbers": "not_a_list"})
    assert response.status_code == 422  # FastAPI devuelve 422 en validaciones Pydantic
