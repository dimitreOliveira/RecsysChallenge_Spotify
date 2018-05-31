import pandas as pd
from sklearn.model_selection import train_test_split
from dataset import build_output, output_submission
from model import ItemSimilarityRecommender


pd.set_option('display.width', 320)

playlist_data = 'data/rating_track_play_added_songs.csv'
test_data = 'data/pid_10k_sample.csv'

test_df = pd.read_csv(test_data, delimiter=',')

playlist_df = pd.read_csv(playlist_data, delimiter=';', dtype={'pid': int, 'track_id': int, 'rating': int})

#playlist_df['track_uri'] = 'spotify:track:' + playlist_df['track_uri']
print(len(playlist_df))

users = test_df['pid'].unique()
songs = playlist_df['track_id'].unique()

print("----------------------------------------------------------------------")
print("Unique user count: %s:" % len(users))
print("----------------------------------------------------------------------")
print("Unique Song count: %s:" % len(songs))
print("----------------------------------------------------------------------")

train_data = playlist_df
print(train_data.head(5))

is_model = ItemSimilarityRecommender()
is_model.create(train_data, 'pid', 'track_id')

# Use the personalized model to make some song recommendations

# Print the songs for the user in training data
user_id = users[5]
user_items = is_model.get_user_items(user_id)

# print("----------------------------------------------------------------------")
# print("Training data songs for the user userid: %s:" % user_id)
# print("----------------------------------------------------------------------")
#
# for user_item in user_items:
#     print(user_item)

print("----------------------------------------------------------------------")
print("Recommendation process going on:")
print("----------------------------------------------------------------------")

# Recommend songs for the user using personalized model
# print(is_model.recommend(user_id))

# Test recommendation for the challenge

list_rec = []
for i in users:
	rec = is_model.recommend(i)
	list_rec.append(rec)

output = build_output(list_rec, 'user_id', 'song')

file_name = 'test.csv'
team_name = 'RecSysCG'
contact_information = 'dimitreandrew@gmail.com'
output_submission(output, file_name, team_name, contact_information)
