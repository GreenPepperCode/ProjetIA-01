import data_module as data
import user_module
import search_module as search
import filter_module as filter

def display_main_menu():
    print("\nMenu Principal")
    print("1. S'inscrire")
    print("2. Se connecter")
    print("3. Quitter le programme")

def display_filter_menu(all_data):
    print("\nMenu de Filtrage")
    print("1. Filtrer par Genre")
    print("2. Filtrer par Durée")
    print("3. Filtrer par Pays")
    print("4. Retourner au menu principal")

    while True:
        choix_filtrage = input("Entrez votre choix (1-4): ")

        if choix_filtrage == '1':
            # Logique de filtrage par genre
            pass
        elif choix_filtrage == '2':
            # Logique de filtrage par durée
            pass
        elif choix_filtrage == '3':
            # Logique de filtrage par pays
            pass
        elif choix_filtrage == '4':
            break  # Sortie de la boucle pour revenir au menu utilisateur
        else:
            print("Choix invalide. Veuillez réessayer.")

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
            display_filter_menu(all_data)
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
