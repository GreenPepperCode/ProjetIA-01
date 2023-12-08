import data_module as data
import user_module
import search_module as search
import filter_module 
from filter_module import safe_json_loads
import pandas as pd

def display_main_menu(all_data):
    # Calcul des statistiques
    total_films = len(all_data)
    total_runtime = all_data['runtime'].sum()
    
    # Extraction des noms des genres
    genre_counts = pd.Series([genre['name'] for sublist in all_data['genres'].apply(safe_json_loads) for genre in sublist]).value_counts()
    top_genres = genre_counts.head(3).index.tolist()

    # Affichage des statistiques
    print("\nStatistiques Globales:")
    print(f"Nombre total de films: {total_films}")
    print(f"Total d'heures visionnables: {total_runtime/60:.2f} heures")
    print(f"Top 3 genres: {', '.join(top_genres)}")

    # Affichage du menu principal
    print("\nMenu Principal")
    print("1. S'inscrire")
    print("2. Se connecter")
    print("3. Quitter le programme")


# Assurez-vous d'appeler cette fonction avec le DataFrame all_data dans le main


def display_filter_menu(all_data):
    print("\nMenu de Filtrage")
    print("1. Filtrer par Genre")
    print("2. Filtrer par Durée")
    print("3. Filtrer par Pays")
    print("4. Retourner au menu principal")

    while True:
        choix_filtrage = input("Entrez votre choix (1-4): ")

        if choix_filtrage == '1':
            genres = input("Entrez les genres séparés par des virgules : ").split(',')
            data_filtree = filter_module.appliquer_filtres(all_data, genres=genres)
        elif choix_filtrage == '2':
            duree_min = int(input("Entrez la durée minimale (en minutes) : "))
            duree_max = int(input("Entrez la durée maximale (en minutes) : "))
            data_filtree = filter_module.appliquer_filtres(all_data, duree_min=duree_min, duree_max=duree_max)
        elif choix_filtrage == '3':
            pays = input("Entrez le pays : ")
            data_filtree = filter_module.appliquer_filtres(all_data, pays=pays)
        elif choix_filtrage == '4':
            break  # Sortie de la boucle pour revenir au menu utilisateur
        else:
            print("Choix invalide. Veuillez réessayer.")

        if choix_filtrage in ['1', '2', '3']:
            quitter = filter_module.naviguer_films(data_filtree)
            if quitter:
                break  # Sortie de la boucle pour revenir au menu utilisateur après la navigation

    return


def display_filtered_films(data_filtree):
    index = 0
    max_index = len(data_filtree) - 1
    while True:
        if not data_filtree.empty:
            print(data_filtree.iloc[index])  # Afficher le film actuel
        else:
            print("Aucun film trouvé.")
            break

        commande = input("Utilisez '>' pour le prochain film, '<' pour le précédent, ou 'exit' pour quitter: ")
        if commande == '>' and index < max_index:
            index += 1
        elif commande == '<' and index > 0:
            index -= 1
        elif commande == 'exit':
            break


def display_user_menu(user_info, all_data):
    print(f"\nMenu de {user_info['nickname']}")
    print("1. Chercher un film")
    print("2. Voir la liste de films avec filtrage")
    print("3. Gérer mes données")
    print("4. Se déconnecter et quitter")

    est_connecte = True
    while est_connecte:
        choix = input("Entrez votre choix (1-4): ")

        if choix == '1':
            search.perform_search(all_data)  # Gère la recherche et l'affichage des résultats
        elif choix == '2':
            display_filter_menu(all_data)  # Gère le filtrage et l'affichage des résultats
        elif choix == '3':
            # Logique pour gérer les données de l'utilisateur
            pass
        elif choix == '4':
            print("Déconnexion réussie. Au revoir !")
            est_connecte = False
        else:
            print("Choix invalide. Veuillez réessayer.")


def main():
    all_data = data.load_data()
    est_actif = True
    while est_actif:
        display_main_menu(all_data)
        choix = input("Entrez votre choix (1-3): ")
        if choix == '1':
            user_info = user_module.create_account()
            display_user_menu(user_info, all_data)
        elif choix == '2':
            user_info = user_module.connect()
            while user_info:  # Tant que l'utilisateur est connecté
                display_user_menu(user_info, all_data)  # Affiche le menu de l'utilisateur
                user_choix = input("Entrez votre choix (1-4): ")
                if user_choix == '1':
                    search.perform_search(all_data)  # Effectue la recherche
                elif user_choix == '2':
                    display_filter_menu(all_data)  # Affiche le menu de filtrage
                elif user_choix == '3':
                    # Gérer les données de l'utilisateur
                    pass
                elif user_choix == '4':
                    print("Déconnexion réussie. Au revoir !")
                    break  # Sort de la boucle, se déconnecte
                else:
                    print("Choix invalide. Veuillez réessayer.")
        elif choix == '3':
            print("Au revoir !")
            est_actif = False
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()

