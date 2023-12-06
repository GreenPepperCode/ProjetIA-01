import pandas as pd
import ast
import os

# Chemin vers le fichier traité
PROCESSED_FILE_PATH = 'dataset/processed_all_data.csv'

def extract_names(lst):
    return [d['name'] for d in lst if 'name' in d]

def process_dataframe(df):
    for col in ['genres', 'production_countries', 'spoken_languages', 'cast']:
        df[col] = df[col].fillna('[]').apply(ast.literal_eval)
        if col != 'cast':
            df[col] = df[col].apply(extract_names)
        else:
            df[col] = df[col].apply(lambda x: [d['character'] for d in x])
    return df

def load_data():
    if os.path.exists(PROCESSED_FILE_PATH):
        return pd.read_csv(PROCESSED_FILE_PATH)

    use_cols_movies = ['id', 'genres', 'original_title', 'overview', 'production_countries', 'runtime', 'spoken_languages']
    use_cols_credits = ['id', 'cast']
    data_movies = pd.read_csv('dataset/movies_metadata.csv', usecols=use_cols_movies, low_memory=False)
    data_credit = pd.read_csv('dataset/credits.csv', usecols=use_cols_credits)

    data_movies['id'] = pd.to_numeric(data_movies['id'], errors='coerce')
    data_credit['id'] = pd.to_numeric(data_credit['id'], errors='coerce')

    all_data = pd.merge(data_movies, data_credit, on='id')
    all_data = process_dataframe(all_data)

    all_data.to_csv(PROCESSED_FILE_PATH, index=False)
    return all_data

# Exemple d'utilisation
if __name__ == "__main__":
    all_data = load_data()
    print(all_data.head())
