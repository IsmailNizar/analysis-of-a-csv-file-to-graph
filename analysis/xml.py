import os

def analysisFileX(dataFile):
    currentP = os.path.dirname(os.path.dirname(__file__)) # retourner le path de dossier courent
    path = os.path.join(currentP,"data","xml","compteRendu",dataFile) # ajouter au path d'autres details pour avoir un path complet
    with open(path,'r') as file:
        preview = file.readline()
    print("this is a preview : {}".format(preview))

if __name__ == "__main__":
    pass