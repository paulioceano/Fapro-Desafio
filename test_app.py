import datetime
import requests
from app import app

def test_valid_date():
    with app.test_client() as client:
        response = client.get('/uf/2022-01-01')
        assert response.status_code == 200
        assert response.json == {'value': '30.996,73', 'date': '2022-01-01'}

def test_invalid_date():
    with app.test_client() as client:
        response = client.get('/uf/2012-12-31')
        assert response.status_code == 400
        assert response.json == {'error': 'Por favor, seleccione una fecha posterior al 2013-01-01', 'value': None}

def test_future_date():
    date = datetime.date.today() + datetime.timedelta(days=10)
    with app.test_client() as client:
        response = client.get(f'/uf/{date}')
        assert response.status_code == 404
        assert response.json == {'error': 'No se encontró el valor de la UF para la fecha solicitada.', 'value': None}

def test_invalid_format():
    with app.test_client() as client:
        response = client.get('/uf/2022/01/01')
        assert response.status_code == 404

def test_uf_not_found():
    with app.test_client() as client:
        response = client.get('/uf/2022-02-29')
        assert response.status_code == 400
        assert response.json == {'value': None, 'error': 'Formato de fecha inválido. Use el formato YYYY-MM-DD.'}

def test_external_api():
    date = datetime.date.today()
    url = f'https://www.sii.cl/valores_y_fechas/uf/uf{date.year}.htm'
    response = requests.get(url)
    assert response.status_code == 200
