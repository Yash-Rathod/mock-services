import json
from app import create_app


def test_health_returns_200():
    client = create_app().test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_process_returns_gif_url_and_duration():
    client = create_app().test_client()
    resp = client.post("/process", json={"camera_id": "cam-2", "frames": 30})
    assert resp.status_code == 200
    body = resp.get_json()
    assert "gif_url" in body
    assert isinstance(body["gif_url"], str) and body["gif_url"].startswith("s3://")
    assert isinstance(body["duration_ms"], int) and body["duration_ms"] > 0
