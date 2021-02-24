import json
import logging
from flask import Flask, abort
import pandas



#  Ouvrir doc csv 

# df.values.tolist()
def pays():
    fichier=pandas.read_csv('ong.csv',names=['id', 'country', 'year', 'emissions', 'value', 'footnotes', 'source' ])
    payss = set(fichier['country'].tolist())
    return payss


def dico(pays):   
    fichier=pandas.read_csv('ong.csv',names=['id', 'country', 'year', 'emissions', 'value', 'footnotes', 'source' ])
    test= fichier.loc[fichier["country"].isin([pays])].sort_values(["year"],ascending=False)
    resultat= {}    
    resultat["country"]= str(test.iloc[0][1]) 
    resultat["year"]= int(test.iloc[0][2])
    resultat["value"]= float (test.iloc[0][4])
    return(json.dumps(resultat))

def avg(year):
    fichier=pandas.read_csv('ong.csv',header=2,names=['id', 'country', 'year', 'emissions', 'value', 'footnotes', 'source' ])       
    # years = (fichier['year'].tolist())
    test1=fichier.loc[fichier["year"].isin([year])]
    test1=test1[(test1["emissions"]=='Emissions (thousand metric tons of carbon dioxide)')]
    print(test1)
    mean_=test1.mean()['value']
    print(mean_)
    resultat= {}
    resultat["year"]=year
    resultat['total']=float(mean_)
    return (json.dumps(resultat))

# @app.route('/per_capita/<country>')
# def per_capita(country):
#     logging.debug(f"Pays demandé : {country}")
    
#     if country.lower()=="albania":
#         return json.dumps({1975:4338.334, 1985:6929.926, 1995:1848.549, 2005:3825.184, 2015:3824.801, 2016:3674.183, 2017:4342.011})
#     else:
#         longeur=len(capita)
#         for i in int(longeur):
#             result['year']=str(capita.iloc[{i}][4])
#             result['values']=float(capita.iloc[{i}][4])
#             print(json.dumps(resultat))

      
