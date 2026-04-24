import json
from app import create_app


def test_health_returns_200():
    client = create_app().test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_summarize_returns_summary_and_confidence():
    client = create_app().test_client()
    resp = client.post("/summarize", json={"gif_url": "s3://mock/clip-001.gif"})
    assert resp.status_code == 200
    body = resp.get_json()
    assert isinstance(body["summary"], str) and len(body["summary"]) > 0
    assert isinstance(body["confidence"], float)
    assert 0.0 <= body["confidence"] <= 1.0
