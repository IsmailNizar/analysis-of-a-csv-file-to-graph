#! /usr/bin/env python3
# coding: utf-8
import os
import re
import argparse
import logging as lg
import analysis.csv as c_an
import analysis.xml as x_an

lg.basicConfig(level=lg.DEBUG)

def parse_arguments(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datafile", help="""CSV 
    file containing pieces of information about the members of parliament""")
    parser.add_argument("-e", "--extension", help="""Type of file to analys. It is CSV or Xml ?""")
    parser.add_argument("-i", "--info", help="""information about the file""")
    return parser.parse_args()


if  __name__ == "__main__":
    args = parse_arguments()
    e = re.search(r"^.+\.(\D{3})$", args.datafile)
    extension = e.group(1)
    try:
        if extension == "csv":
            fichier = c_an.SetOfParliamentMembers("test")
            fichier.launch_analysis("curent_mps.csv", args.info)
        elif extension == "xml":
            x_an.analysisFileX("CRSANR5L15S2017E1N001.xml")
    except FileNotFoundError as error:
        lg.critical("Le fichier demandé est introuvalbe. Message d'erreur : {}".format(error))
    finally:
        print("########### L'analyse est terminée ###########")
    
os.system("pause")