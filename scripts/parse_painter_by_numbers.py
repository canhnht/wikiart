import os
from shutil import copyfile
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

ALL_DATA_INFO = '/Volumes/Young Buffalo/datasets/paintings/painter-by-numbers/all_data_info.csv'
TRAIN_FOLDER = '/Volumes/Young Buffalo/datasets/paintings/painter-by-numbers/train'
TEST_FOLDER = '/Volumes/Young Buffalo/datasets/paintings/painter-by-numbers/test'
OUTPUT_FOLDER = '/Users/thanhcanh/Documents/projects/style-transfer/wikiart/wikiart-saved/painters'

all_data=pd.read_csv(ALL_DATA_INFO, encoding="utf_8")
print("Original record size", all_data.shape)
recordClean=all_data.loc[-all_data.isnull().any(axis=1), :]
recordNaN=all_data.loc[all_data.isnull().any(axis=1), :]
print("Clean record size", recordClean.shape)
print("Records with NaN values", recordNaN.shape)

artists = [
    'jackson pollock',
    'edvard munch',
    'pablo picasso',
    'berthe morisot',
    'claude monet',
    'ernst ludwig kirchner',
    'nicholas roerich',
    'paul cezanne',
    'paul gauguin',
    'sesshu toyo',
    'vincent van gogh',
    'wassily kandinsky'
]

for index, row in all_data.iterrows():
    artist = row['artist'].lower()
    in_train = row['in_train']
    folder = row['artist_group']
    filename = row['new_filename']
    genre = row['genre']
    style = row['style']
    if artist in artists:
        if os.path.exists(os.path.join(TRAIN_FOLDER, filename)):
            filepath = os.path.join(TRAIN_FOLDER, filename)
        else:
            filepath = os.path.join(TEST_FOLDER, filename)
        print('rowwwwwwww', in_train, artist, filepath)
        artist_folder = os.path.join(OUTPUT_FOLDER, artist)
        os.makedirs(artist_folder, exist_ok=True)
        dest = os.path.join(artist_folder, filename)
        copyfile(filepath, dest)

        if pd.notna(genre):
            genre_folder = os.path.join(OUTPUT_FOLDER, artist, 'genre', genre)
            os.makedirs(genre_folder, exist_ok=True)
            dest = os.path.join(genre_folder, filename)
            copyfile(filepath, dest)

        if pd.notna(style):
            style_folder = os.path.join(OUTPUT_FOLDER, artist, 'style', style)
            os.makedirs(style_folder, exist_ok=True)
            dest = os.path.join(style_folder, filename)
            copyfile(filepath, dest)
