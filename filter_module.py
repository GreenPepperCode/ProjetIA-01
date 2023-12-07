import pandas as pd

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
