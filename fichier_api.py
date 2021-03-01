import logging
from fichier_fonction import dico
from fichier_fonction import avg
from fichier_fonction import per_capi
from flask import Flask
from flask import jsonify
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

logging.basicConfig(
    filename="logging_api.log",
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',)


@app.route('/')
def hello_world():
    """def hello_world : Display hello world
    """
    app.logger.info(f"{'Hello World'}")
    return jsonify('Hello, World!')


@app.route('/latest_by_country/<country>')
def by_country(country):
    """latest by country function
    to found the last co2 emssion per country"""
    app.logger.debug(f"{'Affiche dernière donnée pays'}")
    return jsonify(dico(country))


@app.route('/average_by_year/<year>')
def average_for_year(year):
    """def average : Calcul average for a year
    """
    app.logger.debug(f"{'Average'}")
    return jsonify(avg(year))


@app.route('/per_capita/<country>')
def per_capita(country):
    """def per capita to calcul
    the C02 per capita/year"""
    app.logger.debug(f"{'calcul tons of carbon dioxide/ year/ country'}")
    return jsonify(per_capi(country))


if __name__ == "__main__":
    app.run(debug=True)

