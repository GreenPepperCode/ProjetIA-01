import json
# Chemin vers le fichier de sauvegarde
fichier_sauvegarde = 'utilisateurs.json'
# Fonctions pour gérer la sérialisation des données
def sauvegarder_donnees(data):
    with open(fichier_sauvegarde, 'w') as f:
        json.dump(data, f)

def charger_donnees():
    try:
        with open(fichier_sauvegarde, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Gestion des utilisateurs
utilisateurs = charger_donnees()

def creer_utilisateur(nom):
    if nom not in utilisateurs:
        utilisateurs[nom] = {'recherches': [], 'notes': {}}
        sauvegarder_donnees(utilisateurs)
    else:
        print(f"L'utilisateur {nom} existe déjà.")

def enregistrer_recherche(nom, recherche):
    if nom in utilisateurs:
        utilisateurs[nom]['recherches'].append(recherche)
        sauvegarder_donnees(utilisateurs)
    else:
        print(f"L'utilisateur {nom} n'existe pas.")

def afficher_recherches(nom):
    if nom in utilisateurs:
        return utilisateurs[nom]['recherches']
    else:
        return []

def noter_film(nom, film_id, note):
    if nom in utilisateurs:
        utilisateurs[nom]['notes'][film_id] = note
        sauvegarder_donnees(utilisateurs)
    else:
        print(f"L'utilisateur {nom} n'existe pas.")

def afficher_notes(nom):
    if nom in utilisateurs:
        return utilisateurs[nom]['notes']
    else:
        return {}

def supprimer_utilisateur(nom):
    if nom in utilisateurs:
        del utilisateurs[nom]
        sauvegarder_donnees(utilisateurs)
    else:
        print(f"L'utilisateur {nom} n'existe pas.")
