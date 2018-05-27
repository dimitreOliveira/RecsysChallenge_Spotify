import pandas as pd
from sklearn.model_selection import train_test_split
from dataset import build_output, output_submission
from model import ItemSimilarityRecommender


pd.set_option('display.width', 320)

playlist_data = 'data/sample_rating_track_play.csv'

playlist_df = pd.read_csv(playlist_data, delimiter=';')

print(len(playlist_df))

users = playlist_df['pid'].unique()
songs = playlist_df['track_uri'].unique()

print("----------------------------------------------------------------------")
print("Unique user count: %s:" % len(users))
print("----------------------------------------------------------------------")
print("Unique Song count: %s:" % len(songs))
print("----------------------------------------------------------------------")

train_data, test_data = train_test_split(playlist_df, test_size=0.2, random_state=0)
print(train_data.head(5))

is_model = ItemSimilarityRecommender()
is_model.create(train_data, 'pid', 'track_uri')

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
rec1 = is_model.recommend(users[1])
rec2 = is_model.recommend(users[2])
rec3 = is_model.recommend(users[3])
rec4 = is_model.recommend(users[4])
rec5 = is_model.recommend(users[5])

list_rec = [rec1, rec2, rec3, rec4, rec5]

output = build_output(list_rec, 'user_id', 'song')

file_name = 'test.csv'
team_name = 'RecSysCG'
contact_information = 'email@gmail.com'
output_submission(output, file_name, team_name, contact_information)
