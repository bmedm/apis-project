#!/usr/bin/env python3
import sys
import argparse
import src.source as src
import pandas as pd



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
        print(src.director1(args.director))
    elif args.director==None and args.title!=None and args.scoredir==None:
        print(src.titlefilm(args.title))
    elif args.director==None and args.title==None and args.scoredir!=None:
        print(src.scoredirector(args.scoredir))
    


if __name__ == "__main__":
        main()