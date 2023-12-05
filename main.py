import data_module as data
import user_module as user

def afficher_menu_principal():
    print("\nMenu Principal")
    print("1. S'inscrire")
    print("2. Se connecter")
    print("3. Quitter le programme")

def s_inscrire():
    nom = input("Choisissez un nom d'utilisateur pour l'inscription : ")
    # Crée un nouvel utilisateur
    user.creer_utilisateur(nom)
    print(f"Utilisateur {nom} inscrit avec succès.")
    
    # Connecte automatiquement l'utilisateur après l'inscription
    print(f"Bonjour, {nom} ! Vous êtes maintenant connecté.")
    afficher_menu_utilisateur(nom)

def se_connecter():
    nom = input("Entrez votre nom d'utilisateur : ")
    # Vérifier si l'utilisateur existe (tu devras ajouter cette logique dans user_module)
    if user.verifier_utilisateur(nom):
        # Utilisateur existe, logique supplémentaire de connexion
        print(f"Bonjour, {nom} ! Bienvenue dans le système.")
        # Charger des données spécifiques à l'utilisateur ou afficher un menu utilisateur
        afficher_menu_utilisateur(nom)
    else:
        # Utilisateur n'existe pas
        print("Nom d'utilisateur non trouvé. Veuillez réessayer ou vous inscrire.")

def afficher_menu_utilisateur(nom_utilisateur):
    print(f"\nMenu de {nom_utilisateur}")
    print("1. Chercher un film")
    print("2. Voir la liste de films")
    print("3. Gérer mes données")
    print("4. Se déconnecter et quitter")

    est_connecte = True
    while est_connecte:
        choix = input("Entrez votre choix (1-4): ")
        if choix == '1':
            # Logique pour chercher un film
            pass
        elif choix == '2':
            # Logique pour voir la liste de films
            pass
        elif choix == '3':
            # Logique pour gérer les données de l'utilisateur
            pass
        elif choix == '4':
            print("Déconnexion réussie. Au revoir !")
            est_connecte = False
        else:
            print("Choix invalide. Veuillez réessayer.")


def main():
    all_data = data.get_data()

    est_actif = True
    while est_actif:
        afficher_menu_principal()
        choix = input("Entrez votre choix : ")
        if choix == '1':
            user.s_inscrire()
        elif choix == '2':
            user.se_connecter()
        elif choix == '3':
            print("Au revoir !")
            est_actif = False
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
