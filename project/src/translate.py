import pandas as pd

mapping = pd.read_csv('../data/movies/movie_characters_mapping.csv', sep=';')
name_map = dict(
    zip(
        mapping['raw_name'].str.strip().str.lower(),
        mapping['translation_name'].str.strip().str.lower()
    )
)

def translate(raw_char):
    return name_map.get(raw_char.strip().lower(), raw_char.strip().lower())