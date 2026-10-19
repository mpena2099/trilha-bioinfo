from fastapi.testclient import TestClient

from modulo4_ia_xai.api.app_fastapi import app

client = TestClient(app)


def test_prever_retorna_risco_e_aviso():
    r = client.post("/prever", json={"rs123": 1, "rs456": 0})
    assert r.status_code == 200
    corpo = r.json()
    assert corpo["risco"] == 0.3
    assert "aviso" in corpo


def test_prever_outro_genotipo():
    r = client.post("/prever", json={"rs123": 0, "rs456": 2})
    assert r.json()["risco"] == 0.7


def test_prever_rejeita_genotipo_invalido():
    r = client.post("/prever", json={"rs123": 3, "rs456": 0})
    assert r.status_code == 422
