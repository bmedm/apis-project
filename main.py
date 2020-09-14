#!/usr/bin/env python3
import sys
import argparse
import src.source as src
import pandas as pd


#f = pd.read_csv('input/ghibli_clean.csv')
def director1(d):
    director=['Hayao Miyazaki','Isao Takahata','Yoshifumi Kondō','Hiroyuki Morita','Gorō Miyazaki','Hiromasa Yonebayashi']
    if d not in director:
        raise argparse.ArgumentTypeError(f"No hay peliculas de {d}")
    else:
        print(src.director(d))
        
def scoredirector(x):
    director2=['Hayao Miyazaki','Isao Takahata','Yoshifumi Kondō','Hiroyuki Morita','Gorō Miyazaki','Hiromasa Yonebayashi']
    if x not in director2:
        raise argparse.ArgumentTypeError(f"No hay peliculas de {x}")
    else:
        print(src.score(x))
def titlefilm(x):
    films=['Castle in the Sky','My Neighbor Totoro','When Marnie Was There','Pom Poko','Howls Moving Castle','The Tale of the Princess Kaguya,
        'Only Yesterday','Porco Rosso','Princess Mononoke','Ponyo','Grave of the Fireflies','Arrietty','Whisper of the Heart','The Wind Rises','The Cat Returns',
        "Kiki's Delivery Service",'Tales from Earthsea','From Up on Poppy Hill','My Neighbors the Yamadas','Spirited Away']
    if x not in films:
        raise argparse.ArgumentTypeError(f"No hay peliculas de {x}")
    else:
        print(src.title(x))

def main():
    #print(args)
    df = pd.read_csv('input/ghibli_clean.csv')

    parser = argparse.ArgumentParser(description='Imprime la info de la pelicula')
    parser.add_argument('-d', dest='director',
                        default=None,
                        type=str,
                        help="Director: Hayao Miyazaki, Isao Takahata, Yoshifumi Kondō, Hiroyuki Morita, Gorō Miyazaki, Hiromasa Yonebayashi")
    parser.add_argument("-t",dest='title',
                        default=None,
                        type=str)
    parser.add_argument('-s',dest='scoredir',
                        default=None,
                        type=str,
                        help='Director: Devuelve la media de los scores de cada director')
    args = parser.parse_args()
    if args.director!=None and args.title==None and args.scoredir==None:
        print(director1(args.director))
    elif args.director==None and args.title!=None and args.scoredir==None:
        print(title1(args.title))
    elif args.director==None and args.title==None and args.scoredir!=None:
        print(scoredirector(args.scoredir))

    


if __name__ == "__main__":
        main()