import json
import logging
import pandas as pd
from flask import Flask, abort
from nsca import dico,pays,avg
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

pays()
@app.route('/')
def hello_world():
    #utilisé pour tester si l'app fonctionne bien
    return 'Hello, World!'

@app.route('/latest_by_country/<country>')
def by_country(country):
    return dico(country)

@app.route('/average_by_year/<year>')
def average_for_year(year):
    #on cherche la moyenne des émissions totales au niveau mondial pour une année demandée
    return avg(year)
     
    # logging.debug(f"Pays demandé : {country}")
    
    # if country.lower()=="albania":
    #     return json.dumps({1975:4338.334, 1985:6929.926, 1995:1848.549, 2005:3825.184, 2015:3824.801, 2016:3674.183, 2017:4342.011})
    # else:
    #     #erreur 404 si on demande un pays qui n'est pas connu
    #     abort(404)
if __name__=="__main__":
    app.run(debug=True)  