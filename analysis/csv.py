import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class SetOfParliamentMembers:
    """ Une classe  qui permet de manipuler et d'analyser des groupes de députés.
        Réaliser des graphes selon des caractéristiques spécifiées.
     """

    #Constructeur    
    def __init__(self, name):
        self.name = name

    def total_mps(self):
        return len(self.dataframe)

    #lire et créer une dataframe(tableaux) à partir d'un fichier csv 
    def data_from_csv(self,dataFile): 
        self.dataframe = pd.read_csv(dataFile, sep=";")

    #lire et créer une dataframe à partir d'une autre dataframe
    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe

    #Réalisé un graphe qui represente le nombre des femmes et celle d'hommes dans une partie politique
    def display_chart(self):
        femme = homme = 0
        data = self.dataframe
        all_parties = data["sexe"] # mettre dans un variable le tab contenant tous les personnes disponibles
        for party in all_parties:
            if party =="F":
                femme +=1
            elif party == "H":
                homme +=1
        fig, ax = plt.subplots() # initialisation du figure
        ax.axis("equal")
        ax.pie([femme, homme],
                labels = ["Femmes", "Hommes"],
                autopct="%1.1f pourcents")
        plt.title("Graphe % d'homme et femme")
        plt.show()

        
    #Fonction qui découpe chaque personne selon la politique    
    def split_by_political_party(self):
        result ={}
        data = self.dataframe
        all_parties = data["parti_ratt_financier"].dropna().unique() #supprimer tous les rows vides ou dupliqués

        for party in all_parties: # parcourir tous les parties
            data_subset = data[data.parti_ratt_financier == party] # créer un party unique
            subset = SetOfParliamentMembers('MPs from party "{}"'.format(party)) #créer une instance de la class SetOfParliamentMembers avec la party unique trouvé
            subset.data_from_dataframe(data_subset) #créer une dataframe pour cette class
            result[party] = subset # ajouter la dataframe avec la party comme clé dans un dict

        return result

    #Fonction qui permet d'analyser un fichier CSV et répresenté la graphe    
    def launch_analysis(self,dataframe , info = False , by_partie = False ):
        somp = SetOfParliamentMembers("All Mps")
        somp.data_from_csv(os.path.join("data",dataframe))
        somp.display_chart()
        #Si les graphes souhaité selon les parties politiques
        if by_partie:
            for s in somp.split_by_political_party().values():
                s.display_chart()
        if info:
            print("Total Mps : {}".format(somp.total_mps()))



if __name__ == "__main__":
    pass