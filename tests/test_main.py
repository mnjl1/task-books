from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_author_valid_id():
    response = client.get('/authors/1')
    assert response.status_code == 200
    assert response.json() == {'first_name': 'Os', 'last_name': 'Wil', 'id': 1}


def test_author_not_valid_id():
    response = client.get('/authors/1000')
    assert response.status_code == 404
    assert response.json() == {'detail': "Author not found!"}


def test_book_valid_id():
    response = client.get('/books/1')
    assert response.status_code == 200
    assert response.json()['book_name'] == 'Rocket'


def test_book_not_valid_id():
    response = client.get('/books/1000')
    assert response.status_code == 404
