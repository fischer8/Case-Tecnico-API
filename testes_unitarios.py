import pytest
from app import create_app
import copy

API_KEY = "case_tecnico"

exemplo_request = {
    "funcional": 123,
    "dataHora": "2025-09-30T10:00:00",
    "codigoAtividade": "COD001",
    "descricaoAtividade": "teste"
}

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

@pytest.fixture
def auth_headers():
    return {"x-api-key": API_KEY}

def test_get_atividades(client, auth_headers):
    response = client.get('/atividades', headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert response.json == [] 

def test_post_atividade(client, auth_headers):
    response = client.post('/atividades', json=exemplo_request, headers=auth_headers)
    assert response.status_code == 201
    assert "atividade" in response.json
    assert "mensagem" in response.json
    assert response.json['mensagem'] == "Atividade cadastrada com sucesso!"

    atividade = response.json['atividade']
    for key in exemplo_request:
        assert atividade[key] == exemplo_request[key]
    assert "idAtividade" in atividade

def test_post_multiplas_atividades(client, auth_headers):
    for id_atividade in range(1, 7):
        req = copy.deepcopy(exemplo_request)
        response = client.post('/atividades', json=req, headers=auth_headers)
        assert response.status_code == 201

        atividade = response.json['atividade']
        assert atividade['idAtividade'] == id_atividade

        for key in exemplo_request:
            assert atividade[key] == exemplo_request[key]
        assert response.json['mensagem'] == "Atividade cadastrada com sucesso!"

@pytest.mark.parametrize("url,expected_status,expected_msg", [
    ("/rota_inexistente", 404, "Rota não encontrada"),
    ("/atividades/999999", 404, "Nenhuma atividade encontrada para 999999")
])
def test_erros_get(client, url, expected_status, expected_msg):
    response = client.get(url, headers={"x-api-key": API_KEY})
    assert response.status_code == expected_status
    assert "erro" in response.json
    assert expected_msg in response.json['erro']

@pytest.mark.parametrize("missing_field,expected_msg", [
    ("funcional", "Campo 'funcional' é obrigatório"),
    ("codigoAtividade", "Campo 'codigoAtividade' é obrigatório"),
    ("dataHora", "Campo 'dataHora' é obrigatório"),
    ("descricaoAtividade", "Campo 'descricaoAtividade' é obrigatório")
])
def test_erros_post(client, missing_field, expected_msg, auth_headers):
    request_data = copy.deepcopy(exemplo_request)
    del request_data[missing_field]

    response = client.post('/atividades', json=request_data, headers=auth_headers)
    assert response.status_code == 400
    assert "erro" in response.json
    assert response.json['erro'] == expected_msg
