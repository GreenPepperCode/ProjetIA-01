import pandas as pd

def load_data():
    # Chemin vers vos fichiers CSV
    movies_path = 'dataset/movies_metadata.csv'
    credits_path = 'dataset/credits.csv'

    # Chargement des DataFrames
    data_movies = pd.read_csv(movies_path, low_memory=False)
    data_credits = pd.read_csv(credits_path)

    # Suppression des colonnes inutiles
    data_movies = data_movies.drop(["adult", "belongs_to_collection", "budget", "homepage", "imdb_id", "original_language", "overview", "status", "poster_path", "production_companies", "popularity", "revenue", "tagline", "release_date", "video", "vote_average", "vote_count"], axis=1)
    data_credits = data_credits.drop(["crew"], axis=1)

    # Assurer que les ID sont des chaînes de caractères
    data_movies['id'] = data_movies['id'].astype(str)
    data_credits['id'] = data_credits['id'].astype(str)

    # Fusion des DataFrames sur la colonne 'id'
    all_data = pd.merge(data_movies, data_credits, on='id')

    # Suppression des lignes avec des valeurs manquantes
    all_data.dropna(axis=0, inplace=True)

    return all_data
