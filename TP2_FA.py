"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Bélair (2370868), Nom2 (Matricule2)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
import csv

# open an existing file for reading -
csvfile = open('collection_bibliotheque.csv', newline='')

# make a new variable - c - for Python's CSV reader object -
c = csv.DictReader(csvfile)
bibliotheque = {}
# read whatever you want from the reader object
# print it or use it any way you like
for row in c:
    livre ={
        "titre": row["titre"],
        "auteur": row["auteur"],
        "date_publication": row["date_publication"],
    }
    cote_rangement = row["cote_rangement"]
    bibliotheque[cote_rangement] = livre
print(f' \n Bibliotheque initiale : {bibliotheque} \n')
# save and close the file
csvfile.close()





########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici
# open an existing file for reading -
csvfile = open('nouvelle_collection.csv', newline='')

# make a new variable - c - for Python's CSV reader object -
c = csv.DictReader(csvfile)
# read whatever you want from the reader object
# print it or use it any way you like
for row in c:
    cote_rangement = row["cote_rangement"]
    titre = row["titre"]
    auteur = row["auteur"]
    date_publication = row["date_publication"]
    livre ={ 
    "titre": titre,
    "auteur": auteur,
    "date_publication": date_publication,
    }
    try:
        if bibliotheque[cote_rangement]: # type: ignore
            print(f"Le livre {cote_rangement} ---- {titre} par {auteur} ---- est déjà présent dans la bibliothèque")
    except:
        bibliotheque[cote_rangement] = livre
        print(f"Le livre {cote_rangement} ---- {titre} par {auteur} ---- a été ajouté avec succès")
# save and close the file
csvfile.close()






########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici

for livre in bibliotheque.copy():
    if livre[0] == "S":
        if bibliotheque[livre]["auteur"] == "William Shakespeare":
            new_livre = bibliotheque[livre]
            new_cote = "WS"
            for i in livre[1:]:
                new_cote += i
            bibliotheque.pop(livre)
            bibliotheque[new_cote] = new_livre

print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')
########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici

csvfile = open('emprunts.csv', newline='')

# make a new variable - c - for Python's CSV reader object -
c = csv.DictReader(csvfile)

for row in c:
    try:
        livre = bibliotheque[row["cote_rangement"]]
        new_livre = {
            "titre": livre["titre"],
            "auteur": livre["auteur"],
            "date_publication": livre["date_publication"],
            "emprunts" : "emprunté",
            "date_emprunt": row["date_emprunt"]
        }
        bibliotheque[row["cote_rangement"]] = new_livre
    except:
        pass
for cote in bibliotheque:
    try:
        if bibliotheque[cote]["emprunts"]:
            pass
    except:
        livre = bibliotheque[cote]
        new_livre = {
            "titre": livre["titre"],
            "auteur": livre["auteur"],
            "date_publication": livre["date_publication"],
            "emprunts" : "disponible",
        }
        bibliotheque[cote] = new_livre
print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')
csvfile.close()


########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici

csvfile = open('emprunts.csv', newline='')

# make a new variable - c - for Python's CSV reader object -
c = csv.DictReader(csvfile)
import datetime 
  
# Initializing a date and time 
time_change = datetime.timedelta(days=30)  

for row in c:
    date = row["date_emprunt"].split("-")
    target_date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
    now = datetime.datetime.now()
    date_diff = now.date() - target_date
    if date_diff.days > 30:
        frais = 2* date_diff.days
        if frais > 100:
            bibliotheque[row["cote_rangement"]] = livre
            new_livre = {
            "titre": livre["titre"],
            "auteur": livre["auteur"],
            "date_publication": livre["date_publication"],
            "emprunts" : "emprunté",
            "date_emprunt": row["date_emprunt"],
            "frais_retard": "100$"
            }
        else:
            bibliotheque[row["cote_rangement"]] = livre
            new_livre = {
            "titre": livre["titre"],
            "auteur": livre["auteur"],
            "date_publication": livre["date_publication"],
            "emprunts" : "emprunté",
            "date_emprunt": row["date_emprunt"],
            "frais_retard": str(frais)+"$"
            }
        bibliotheque[row["cote_rangement"]] = new_livre
    else:       
        pass

print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')


csvfile.close()



