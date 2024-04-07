import pytest
from app import app
@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_get_dados(client):
    response = client.get('/dados')
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data, list)  # Verifica se os dados são retornados como uma lista
    assert len(data) > 0  # Verifica se há dados retornados

def test_save_dados(client):
    novo_dado = {
        "nome": "Teste",
        "whatsapp": "123456789",
        "dia": "01/01/2022",
        "horario": "08:00",
        "tipo_cilio": "Teste"
    }
    response = client.post('/dados', json=novo_dado)
    data = response.get_json()

    assert response.status_code == 201
def test_update_dados(client):
    # First, create a new data entry to update
    novo_dado = {
        "nome": "Teste Update",
        "whatsapp": "987654321",
        "dia": "02/02/2022",
        "horario": "09:00",
        "tipo_cilio": "Teste Update"
    }
    
    response = client.put(f'/dados/{data["id"]}', json=updated_dado)
    data = response.get_json()
    assert response.status_code == 200

    # Update the data entry created above
    updated_dado = {
        "nome": "Teste Updated",
        "whatsapp": "555555555",
        "dia": "03/03/2022",
        "horario": "10:00",
        "tipo_cilio": "Teste Updated"
    }
    response = client.put(f'/dados/{data["id"]}', json=updated_dado)
    assert response.status_code == 200
    # Add more asserts to check the updated data

def test_delete_dados(client):
    # First, create a new data entry to delete
    novo_dado = {
        "nome": "Teste Delete",
        "whatsapp": "111111111",
        "dia": "04/04/2022",
        "horario": "11:00",
        "tipo_cilio": "Teste Delete"
    }
    response = client.post('/dados', json=novo_dado)
    data = response.get_json()
    assert response.status_code == 201

    # Delete the data entry created above
    response = client.delete(f'/dados/{data["id"]}')
    assert response.status_code == 204
    # Add more asserts to check if data was successfully deleted

# Add more test cases as needed
