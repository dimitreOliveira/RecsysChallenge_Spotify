import pandas as pd
from sklearn.model_selection import train_test_split
from model import ItemSimilarityRecommender


pd.set_option('display.width', 320)

# triplets_file link: https://static.turi.com/datasets/millionsong/10000.txt
# songs_metadata_file link: https://static.turi.com/datasets/millionsong/song_data.csv

triplets_file = 'data/triplets_file.csv'
songs_metadata_file = 'data/song_data.csv'

song_df_1 = pd.read_csv(triplets_file)
song_df_2 = pd.read_csv(songs_metadata_file)

# Merge the two dataframes above to create input dataframe for recommender systems
song_df = pd.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")

print(len(song_df))

# Merge song title and artist_name columns to make a merged column
song_df['song'] = song_df['title'].map(str) + " - " + song_df['artist_name']

song_grouped = song_df.groupby(['song']).agg({'listen_count': 'count'}).reset_index()
grouped_sum = song_grouped['listen_count'].sum()
song_grouped['percentage'] = song_grouped['listen_count'].div(grouped_sum)*100
print(song_grouped.sort_values(['listen_count', 'song'], ascending=[0, 1]))

users = song_df['user_id'].unique()
songs = song_df['song'].unique()

print("----------------------------------------------------------------------")
print("Unique user count: %s:" % len(users))
print("----------------------------------------------------------------------")
print("Unique Song count: %s:" % len(songs))
print("----------------------------------------------------------------------")

train_data, test_data = train_test_split(song_df, test_size=0.20, random_state=0)
print(train_data.head(5))

is_model = ItemSimilarityRecommender()
is_model.create(train_data, 'user_id', 'song')

# Use the personalized model to make some song recommendations

# Print the songs for the user in training data
user_id = users[5]
user_items = is_model.get_user_items(user_id)

print("----------------------------------------------------------------------")
print("Training data songs for the user userid: %s:" % user_id)
print("----------------------------------------------------------------------")

for user_item in user_items:
    print(user_item)

print("----------------------------------------------------------------------")
print("Recommendation process going on:")
print("----------------------------------------------------------------------")

# Recommend songs for the user using personalized model
print(is_model.recommend(user_id))

# # We can also apply the model to find similar songs to any song in the dataset
# song = 'Yellow - Coldplay'
# print(is_model.get_similar_items([song]))
