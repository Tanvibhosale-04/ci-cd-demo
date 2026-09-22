from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Hello from CI/CD Demo!"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_home_content_type():
    client = app.test_client()

    response = client.get("/")

    assert response.content_type == "text/html; charset=utf-8"


def test_health_content_type():
    client = app.test_client()

    response = client.get("/health")

    assert response.content_type == "application/json"
