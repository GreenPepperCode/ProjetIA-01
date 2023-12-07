import data_module as data
import user_module
import search_module as search
import filter_module as filter

def display_main_menu():
    print("\nMenu Principal")
    print("1. S'inscrire")
    print("2. Se connecter")
    print("3. Quitter le programme")

def display_user_menu(user_info, all_data):
    print(f"\nMenu de {user_info['nickname']}")
    print("1. Chercher un film")
    print("2. Voir la liste de films")
    print("3. Gérer mes données")
    print("4. Se déconnecter et quitter")

    est_connecte = True
    while est_connecte:
        choix = input("Entrez votre choix (1-4): ")
        if choix == '1':
            films_trouves = search.perform_search(all_data)
        if films_trouves:
            for film in films_trouves:
                print(film)
            else:
                print("Aucun film trouvé.")
        elif choix == '2':
            # Ici, vous pouvez ajouter la logique pour voir la liste de films
            pass
        elif choix == '3':
            # Ici, vous pouvez ajouter la logique pour gérer les données de l'utilisateur
            pass
        elif choix == '4':
            print("Déconnexion réussie. Au revoir !")
            est_connecte = False
        else:
            print("Choix invalide. Veuillez réessayer.")

def perform_search(all_data):
    # Initialisation du flag pour continuer la recherche
    continuer_recherche = True

    # Boucle pour permettre à l'utilisateur de continuer à rechercher ou de revenir au menu utilisateur
    while continuer_recherche:
        # Affichage des options de recherche disponibles
        print("\nTypes de recherche :")
        print("1. Par Durée")
        print("2. Par Acteur")
        print("3. Par Genre")
        print("4. Par Langue")
        print("5. Retour au menu utilisateur")

        # Demander à l'utilisateur de choisir une option de recherche
        choix_recherche = input("Choisissez un type de recherche (1-5): ")

        # Traiter le choix de l'utilisateur
        if choix_recherche == '1':
            # Recherche par durée
            duree = int(input("Entrez la durée du film (en minutes): "))
            print(search.trouver_films_par_duree(duree, all_data))
        elif choix_recherche == '2':
            # Recherche par acteur
            acteur = input("Entrez le nom de l'acteur : ")
            print(search.trouver_films_par_acteur(acteur, all_data))
        elif choix_recherche == '3':
            # Recherche par genre
            genre = input("Entrez le genre du film : ")
            print(search.trouver_films_par_genre(genre, all_data))
        elif choix_recherche == '4':
            # Recherche par langue
            langue = input("Entrez la langue du film : ")
            print(search.trouver_films_par_langue(langue, all_data))
        elif choix_recherche == '5':
            # Sortir de la boucle pour revenir au menu utilisateur
            continuer_recherche = False
        else:
            # Gérer les choix invalides
            print("Choix invalide. Veuillez réessayer.")

        # Pause pour permettre à l'utilisateur de lire les résultats avant de continuer
        if choix_recherche != '5':
            input("\nAppuyez sur Entrée pour continuer...")



def main():
    all_data = data.load_data()
    est_actif = True
    while est_actif:
        display_main_menu()
        choix = input("Entrez votre choix (1-3): ")
        if choix == '1':
            user_info = user_module.create_account()
            display_user_menu(user_info, all_data)
        elif choix == '2':
            user_info = user_module.connect()
            display_user_menu(user_info, all_data)
        elif choix == '3':
            print("Au revoir !")
            est_actif = False
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
