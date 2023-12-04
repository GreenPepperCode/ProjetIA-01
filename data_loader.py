import pandas as pd

def load_and_clean_data(movies_path: str, credits_path: str):
    # Chargement des données
    data = pd.read_csv(movies_path, low_memory=False)
    data_2 = pd.read_csv(credits_path)

    # Nettoyage des données en supprimant certaines colonnes
    data = data.drop(["adult", "belongs_to_collection", "budget", "homepage", "imdb_id", "original_language", "overview", "status", "poster_path", "production_companies", "popularity", "revenue", "tagline", "release_date", "video", "vote_average", "vote_count"], axis=1)
    data_2 = data_2.drop(["crew"], axis=1)

    # S'assurer que la colonne 'id' est du même type dans les deux DataFrames
    data['id'] = pd.to_numeric(data['id'], errors='coerce')
    data_2['id'] = pd.to_numeric(data_2['id'], errors='coerce')

    # Supprimer les lignes avec des ID manquants ou mal formatés
    data.dropna(subset=['id'], inplace=True)
    data_2.dropna(subset=['id'], inplace=True)

    # Fusion des DataFrames sur la colonne 'id'
    all_data = data.merge(data_2, on='id')

    # Suppression des lignes avec des valeurs manquantes
    all_data.dropna(axis=0, inplace=True)

    return all_data

def get_data(movies_path: str = 'dataset/movies_metadata.csv', credits_path: str = 'dataset/credits.csv'):
    return load_and_clean_data(movies_path, credits_path)
