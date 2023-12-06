import data_module as data
import user_module as user
import search_module as search
import filter_module as filter

def display_main_menu():
    print("\nMenu Principal")
    print("1. S'inscrire")
    print("2. Se connecter")
    print("3. Quitter le programme")

def sign_up(all_data):
    username = input("Choisissez un nom d'utilisateur pour l'inscription : ")
    user.create_user(username)
    print(f"Utilisateur {username} inscrit avec succès.")
    display_user_menu(username, all_data)

def log_in(all_data):
    username = input("Entrez votre nom d'utilisateur : ")
    if user.verify_user(username):
        print(f"Bonjour, {username} ! Bienvenue dans le système.")
        display_user_menu(username, all_data)
    else:
        print("Nom d'utilisateur non trouvé. Veuillez réessayer ou vous inscrire.")

def display_user_menu(username, all_data):
    print(f"\nMenu de {username}")
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
    print("\nTypes de recherche :")
    print("1. Par Durée")
    print("2. Par Acteur")
    print("3. Par Genre")
    print("4. Par Langue")
    choix_recherche = input("Choisissez un type de recherche (1-4): ")

    if choix_recherche == '1':
        duree = int(input("Entrez la durée du film (en minutes): "))
        print(search.trouver_films_par_duree(duree, all_data))
    elif choix_recherche == '2':
        acteur = input("Entrez le nom de l'acteur : ")
        print(search.trouver_films_par_acteur(acteur, all_data))
    elif choix_recherche == '3':
        genre = input("Entrez le genre du film : ")
        print(search.trouver_films_par_genre(genre, all_data))
    elif choix_recherche == '4':
        langue = input("Entrez la langue du film : ")
        print(search.trouver_films_par_langue(langue, all_data))
    else:
        print("Choix invalide. Veuillez réessayer.")


def main():
    all_data = data.load_data()
    est_actif = True
    while est_actif:
        display_main_menu()
        choix = input("Entrez votre choix (1-3): ")
        if choix == '1':
            sign_up(all_data)
        elif choix == '2':
            log_in(all_data)
        elif choix == '3':
            print("Au revoir !")
            est_actif = False
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
