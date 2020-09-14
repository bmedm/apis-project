import numpy as np
import pandas as pd
import re
import json
import urllib
import requests
from pandas import json_normalize

def geturlid(url="https://ghibliapi.herokuapp.com/",path="films/",ids="dc2e6bd1-8156-4886-adff-b39e6043af0c"):
    """
    obtener dataframe de la api 
    con path e id (por defecto films
                  y el viaje de chihiro)
    """
    urls = url+path+ids
    response = requests.request("GET", urls)
    data=response.text
    data1=json.loads(data)
    flat_data=json_normalize(data1)

    return flat_data

def geturl(path="films/"):
    """
    obtener dataframe de la api 
    con path. (por defecto films/)
    """
   
    url = f"https://ghibliapi.herokuapp.com/{path}"
    response = requests.request("GET", url)
    data=response.text
    data1=json.loads(data)
    flat_data=json_normalize(data1)
    
    return flat_data

df=pd.read_csv('input/ghibli_clean.csv')
scores=pd.read_csv('input/scores.csv')
def director1(d):
    director=['Hayao Miyazaki','Isao Takahata','Yoshifumi Kondō','Hiroyuki Morita','Gorō Miyazaki','Hiromasa Yonebayashi']
    if d not in director:
        raise argparse.ArgumentTypeError(f"No hay peliculas de {d}")
    else:
        print(director(d))

def merge(df1,df2,column,how):
    """
    une dos dataframe (join)
    """
    return df1.merge(df2, left_on=column, right_on=column,how=how)

def director(x):
    """
    Dataframe solo con datos del director elegido
    """
    return df[df['director']==x][['title','score','director','year']]

def title(t):
    """
    Datos de la pelicula elegida
    """
    return df[df['title']==f'{t}'][['title','score','director','year']]
def year(y):
    """
    Datos de las peliculas del año elegido
    """
    return df[df['year']==y][['title','director','year']]
def score(x):
    """
    Media de la puntuacion de las peliculas de cada director
    """
    return scores[f'{x}']
    
def director1(d):
    director=['Hayao Miyazaki','Isao Takahata','Yoshifumi Kondō','Hiroyuki Morita','Gorō Miyazaki','Hiromasa Yonebayashi']
    if d not in director:
        raise argparse.ArgumentTypeError(f"No hay peliculas de {d}")
    else:
        print(director(d))
        
def scoredirector(x):
    director2=['Hayao Miyazaki','Isao Takahata','Yoshifumi Kondō','Hiroyuki Morita','Gorō Miyazaki','Hiromasa Yonebayashi']
    if x not in director2:
        raise argparse.ArgumentTypeError(f"No hay peliculas de {x}")
    else:
        print(score(x))
def titlefilm(x):
    films=['Castle in the Sky','My Neighbor Totoro','When Marnie Was There','Pom Poko','Howls Moving Castle','The Tale of the Princess Kaguya','Only Yesterday','Porco Rosso','Princess Mononoke','Ponyo','Grave of the Fireflies','Arrietty','Whisper of the Heart','The Wind Rises','The Cat Returns',
        "Kiki's Delivery Service",'Tales from Earthsea','From Up on Poppy Hill','My Neighbors the Yamadas','Spirited Away']
    if x not in films:
        raise argparse.ArgumentTypeError(f"No hay peliculas de {x}")
    else:
        print(title(x))