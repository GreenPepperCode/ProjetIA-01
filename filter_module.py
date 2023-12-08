import json

def safe_json_loads(json_str):
    try:
        json_str = json_str.replace("\'", "\"")
        return json.loads(json_str)
    except json.JSONDecodeError:
        return []

def display_films_per_page(all_data, page, page_size=5):
    start = page * page_size
    end = start + page_size
    films = all_data.iloc[start:end]

    for index, film in films.iterrows():
        # Parser les colonnes JSON
        genres = safe_json_loads(film['genres'])
        countries = safe_json_loads(film['production_countries'])
        languages = safe_json_loads(film['spoken_languages'])
        cast = safe_json_loads(film['cast'])

        print(f"Film {index + 1 + start}: {film['title']}")
        print("Genres:", ', '.join([genre['name'] for genre in genres if 'name' in genre]))
        print("Pays de production:", ', '.join([country['name'] for country in countries if 'name' in country]))
        print("Langues parlées:", ', '.join([lang['name'] for lang in languages if 'name' in lang]))
        print("Cast:", ', '.join([cast_member['name'] for cast_member in cast if 'name' in cast_member]))
        print(f"Durée: {film['runtime']} minutes\n")


def afficher_films(data_filtree, page=0):
    films_par_page = 5
    debut = page * films_par_page
    fin = debut + films_par_page
    films_a_afficher = data_filtree.iloc[debut:fin]

    for index, row in films_a_afficher.iterrows():
        print(f"Film {index + 1 + debut}: {row['title']}")

def naviguer_films(data_filtree):
    page = 0
    films_par_page = 5

    while True:
        debut = page * films_par_page
        fin = debut + films_par_page
        films_a_afficher = data_filtree.iloc[debut:fin]

        for index, row in films_a_afficher.iterrows():
            print(f"Film {index + 1 + debut}: {row['title']}")

        action = input("Utilisez '<' pour précédent, '>' pour suivant, ou 'q' pour quitter: ")
        if action == '<' and page > 0:
            page -= 1
        elif action == '>' and fin < len(data_filtree):
            page += 1
        elif action == 'q':
            return True  # Indiquer que l'utilisateur veut quitter la navigation


def filtrer_films_par_genre(all_data, genres):
    if genres:
        return all_data[all_data['genres'].apply(lambda x: all(genre in x for genre in genres))]
    return all_data

def filtrer_films_par_duree(all_data, duree_min=None, duree_max=None):
    if duree_min is not None:
        all_data = all_data[all_data['runtime'] >= duree_min]
    if duree_max is not None:
        all_data = all_data[all_data['runtime'] <= duree_max]
    return all_data

def filtrer_films_par_pays(all_data, pays):
    if pays:
        return all_data[all_data['production_countries'].apply(lambda x: pays in x)]
    return all_data

def appliquer_filtres(all_data, genres=None, duree_min=None, duree_max=None, pays=None):
    data_filtree = all_data
    data_filtree = filtrer_films_par_genre(data_filtree, genres)
    data_filtree = filtrer_films_par_duree(data_filtree, duree_min, duree_max)
    data_filtree = filtrer_films_par_pays(data_filtree, pays)
    return data_filtree
