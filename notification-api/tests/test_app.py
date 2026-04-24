import json
from app import create_app

def test_health_returns_200():
    client = create_app().test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}

def test_notify_accepts_payload():
    client = create_app().test_client()
    resp = client.post("/notify", json={"camera_id": "cam-1", "event": "person_detected"})
    assert resp.status_code == 202
    assert resp.get_json()["accepted"] is True