import pandas
from flask import abort




def ouvrir_fichier():
    """This function make the connexion with the csv file
    """
    df = pandas.read_csv('ong.csv',header=2, names=['id', 'country', 'year', 'emissions', 'value', 'footnotes', 'source' ])
    return df



def pays():
    """This function permit to convert the csv file to list 
    """
    df = ouvrir_fichier()
    choix_pays = set(df['country'].tolist())
    return choix_pays



def dico(pays):   
    """This function order the csv file to make some request, and answer
    """ 
    df = ouvrir_fichier()
    df= df.loc[df["country"].isin([pays])].sort_values(["year"],ascending=False)
    resultat= {}    
    resultat["country"]= str(df.iloc[0][1]) 
    resultat["year"]= int(df.iloc[0][2])
    resultat["value"]= float (df.iloc[0][4])
    return resultat 


def avg(year):
    """ This function make the average of the value per year of "thousand metric tons of carbon dioxide" 
    """
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


def per_capi(country):
    """This function calcul the "metric tons of carbon dioxide" per year for a country
    """
    df = ouvrir_fichier()
    df = df.loc[df['country'].isin([country])]
    df = df[(df['emissions']=='Emissions per capita (metric tons of carbon dioxide)')]
    resultat={}
    longeur=len(df)
    for i in range(longeur):
        resultat[int(df.iloc[i][2])]=float(df.iloc[i][4])

    return resultat

