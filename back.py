import json
import logging
from flask import Flask, abort
import pandas

#  Ouvrir doc csv 
def ouvrir_fichier():
    df = pandas.read_csv('ong.csv',header=2, names=['id', 'country', 'year', 'emissions', 'value', 'footnotes', 'source' ])
    return df

# df.values.tolist()
def pays():
    df = ouvrir_fichier()
    choix_pays = set(df['country'].tolist())
    return choix_pays
   
# Cette fonction affiche la derniere 
def dico(pays):   
    df = ouvrir_fichier()
    df= df.loc[df["country"].isin([pays])].sort_values(["year"],ascending=False)
    resultat= {}    
    resultat["country"]= str(df.iloc[0][1]) 
    resultat["year"]= int(df.iloc[0][2])
    resultat["value"]= float (df.iloc[0][4])
    return resultat 

# Cette fonction fait la moyenne "thousand metric tons of carbon dioxide" d'une année
def avg(year):
    df = ouvrir_fichier()
    df = df.loc[df["year"].isin([year])]
    df = df[(df["emissions"]=='Emissions (thousand metric tons of carbon dioxide)')]
    print(df)
    mean_value=df.mean()['value']
    resultat= {}
    resultat["year"] = year
    resultat['total'] = float(mean_value)
    print(mean_value)
    return resultat

# Cette fonction calcule "metric tons of carbon dioxide" par année d'un pays
def per_capi(country):
    df = ouvrir_fichier()
    df = df.loc[df['country'].isin([country])]
    df = df[(df['emissions']=='Emissions per capita (metric tons of carbon dioxide)')]
    resultat={}
    longeur=len(df)
    for i in range(longeur):
        resultat[int(df.iloc[i][2])]=float(df.iloc[i][4])

    return resultat
