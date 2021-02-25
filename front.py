import json
import logging
import pandas as pd
from flask import Flask, abort, jsonify
from back import dico,pays,avg,per_capi,ouvrir_fichier
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def hello_world():
    #utilisé pour tester si l'app fonctionne bien
    return jsonify('Hello, World!')


@app.route('/latest_by_country/<country>')
def by_country(country):
    return jsonify(dico(country))


@app.route('/average_by_year/<year>')
def average_for_year(year):
    return jsonify(avg(year))

    
@app.route('/per_capita/<country>')
def per_capita(country):
    return jsonify(per_capi(country))


if __name__=="__main__":
    app.run(debug=True)  
