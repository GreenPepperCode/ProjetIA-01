#trouver un film avec la duree 
import pandas as pd
import json
 
# Définition de la fonction pour trouver des films par leur durée
def trouver_films_par_duree(duree_recherchee, all_data):
    films_trouves = []  # Liste pour stocker les titres des films trouvés
 
    # Parcourir chaque ligne du DataFrame
    for index, row in all_data.iterrows():
        # Vérifier si la durée du film correspond à la durée recherchée
        if row['runtime'] == duree_recherchee:
            films_trouves.append(row['title'])  # Ajouter le titre du film à la liste des films trouvés
 
        # Vérifier si 5 films ont déjà été trouvés
        if len(films_trouves) == 5:
            break  # Arrêter la boucle principale une fois que 5 films ont été trouvés
 
    return films_trouves  # Renvoyer la liste des films trouvés

#trouver un film avec le nom d un acteur 
def trouver_films_par_acteur(nom_acteur, all_data):
    films_trouves = []
 
    for _, row in all_data.iterrows():
        try:
            # Convertir la colonne 'cast' en liste de dictionnaires
            cast = json.loads(row['cast'].replace("'", "\""))
 
            # Vérifier si l'acteur recherché est dans la liste des acteurs du film
            if any(acteur['name'] == nom_acteur for acteur in cast):
                films_trouves.append(row['title'])  # Assurez-vous que 'title' est le nom correct de la colonne
 
            # Arrêter une fois que 5 films ont été trouvés
            if len(films_trouves) == 5:
                break
        except json.JSONDecodeError:
            continue
 
    return films_trouves
 
 #trouver un film avec un genre
def trouver_films_par_genre(genre_recherche, all_data):
    films_trouves = []
 
    for _, row in all_data.iterrows():
        # La colonne 'genres' est une chaîne JSON, la convertir en liste de dictionnaires
        genres = json.loads(row['genres'].replace("'", "\""))
 
        # Vérifier si le genre recherché est dans la liste des genres du film
        if any(genre['name'] == genre_recherche for genre in genres):
            films_trouves.append(row['title'])  # Assurez-vous que 'title' est le nom correct de la colonne
 
        # Arrêter une fois que 5 films ont été trouvés
        if len(films_trouves) == 5:
            break
 
    return films_trouves

def trouver_films_par_langue(langue_recherchee, all_data):
    films_trouves = []
 
    for _, row in all_data.iterrows():
        try:
            # Convertir la chaîne 'spoken_languages' en liste de dictionnaires
            langues = json.loads(row['spoken_languages'].replace("'", "\""))
        except json.JSONDecodeError:
            continue  # Si l'erreur se produit, passez au film suivant
 
        # Vérifier si la langue recherchée est dans la liste des langues parlées du film
        if any(langue['name'] == langue_recherchee for langue in langues):
            films_trouves.append(row['title'])  # Ajouter le titre du film à la liste des films trouvés
 
            # Arrêter une fois que 5 films ont été trouvés
            if len(films_trouves) == 5:
                break
 
    return films_trouves

def perform_search(all_data):
    continuer_recherche = True
    data_filtree = all_data.copy()  # Créer une copie du DataFrame pour appliquer les filtres

    while continuer_recherche:
        print("\nTypes de recherche :")
        print("1. Par Durée")
        print("2. Par Acteur")
        print("3. Par Genre")
        print("4. Par Langue")
        print("5. Retour au menu utilisateur")
        choix_recherche = input("Choisissez un type de recherche (1-5): ")

        films_list = []
        if choix_recherche == '1':
            duree = int(input("Entrez la durée du film (en minutes): "))
            data_filtree = data_filtree[data_filtree['runtime'] == duree]
        elif choix_recherche == '2':
            acteur = input("Entrez le nom de l'acteur : ")
            data_filtree = data_filtree[data_filtree['cast'].apply(lambda x: acteur in x)]
        elif choix_recherche == '3':
            genre = input("Entrez le genre du film : ")
            data_filtree = data_filtree[data_filtree['genres'].apply(lambda x: genre in x)]
        elif choix_recherche == '4':
            langue = input("Entrez la langue du film : ")
            data_filtree = data_filtree[data_filtree['spoken_languages'].apply(lambda x: langue in x)]
        elif choix_recherche == '5':
            continuer_recherche = False
            break

        if not data_filtree.empty:
            # Afficher un maximum de 5 films
            for index, row in data_filtree.head(5).iterrows():
                print(row['title'])
        else:
            print("Aucun film trouvé.")

        if choix_recherche != '5':
            input("\nAppuyez sur Entrée pour continuer...")

    # Réinitialiser la recherche si l'utilisateur retourne au menu principal
    return
