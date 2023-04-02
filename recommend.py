import pandas as pd
import difflib
import pickle

artist_data = pd.read_csv('artists.csv')
artists_data=artist_data.iloc[0:20000]
artists_data = artists_data.drop_duplicates(subset='artist_mb',keep='first')
selected_features = ['artist_mb','tags_lastfm','country_mb','tags_mb']
similarity11 = pickle.load(open('similarityscores.pkl','rb'))

def recommend(artist):
    artist_name = artist
    list_of_artist_name=artists_data['artist_mb'].tolist()
    find_close_match=difflib.get_close_matches(artist_name,list_of_artist_name)
    close_match=find_close_match[0]
    print(close_match)
    artist_index = artists_data[artists_data['artist_mb'] == close_match].index[0]
    distances = similarity11[artist_index]
    artists_list = sorted(list(enumerate(distances)),key = lambda x:x[1],reverse = True)[1:30]

    print(type(artists_list))

    recommended_artists = []
    recommended_artists.append(close_match)
    for i in artists_list:
        recommended_artists.append(artists_data.iloc[i[0]].artist_mb)

    return recommended_artists;

print("Machine Ready...")




