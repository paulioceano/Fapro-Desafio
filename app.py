import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)
MIN_DATE = datetime.strptime('2013-01-01', '%Y-%m-%d')


@app.route('/uf/<date>', methods=['GET'])
def get_uf(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
        if date > MIN_DATE:
            try:
                url = f'https://www.sii.cl/valores_y_fechas/uf/uf{date.year}.htm'
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                # Get general year table
                table = soup.find_all('table')[-1]
                # Get the requested day
                rows = table.find_all('tr')[1:]
                daily_row = rows[date.day - 1]
                # Get the requested month
                columns = daily_row.find_all('td')
                month_column = columns[date.month - 1]
                uf_found = month_column.text.strip()
                if uf_found == "":
                    return jsonify({'value': None, 'error': "No se encontró el valor de la UF para la fecha solicitada."}), 404
                else:
                    return jsonify({'value': uf_found, 'date': date.strftime('%Y-%m-%d')}), 200
            except IndexError:
                return jsonify({'value': None, 'error': "No se encontró el valor de la UF para la fecha solicitada."}), 404
        else:
            return jsonify({'value': None, 'error': "Por favor, seleccione una fecha posterior al 2013-01-01"}), 400
    except ValueError:
        return jsonify({'error': 'Formato de fecha inválido. Use el formato YYYY-MM-DD.', 'value': None}), 400


if __name__ == '__main__':
    app.run(debug=True)
