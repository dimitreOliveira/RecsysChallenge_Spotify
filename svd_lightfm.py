import numpy as np
from lightfm import LightFM
import pandas as pd
import scipy.sparse as sparse
from dataset import build_output, output_submission
from model import lightfm_recommendation

pd.set_option('display.width', 320)

playlist_data = 'data/rating_track_play_added_songs.csv'
test_data = 'data/pid_10k_sample.csv'

test_df = pd.read_csv(test_data, dtype=np.int32)
playlist_df = pd.read_csv(playlist_data, delimiter=';', dtype={'pid': int, 'track_id': int, 'rating': int})

playlist_df = playlist_df[:50000]

users = playlist_df['pid'].unique()
songs = playlist_df['track_id'].unique()


print("----------------------------------------------------------------------")
print("Data set size: %s:" % len(playlist_df))
print("----------------------------------------------------------------------")
print("Unique user count: %s:" % len(users))
print("----------------------------------------------------------------------")
print("Unique Song count: %s:" % len(songs))
print("----------------------------------------------------------------------")


# playlist_data = playlist_df
print("Sample of the data set")
print(playlist_df.head(5))

np_data = np.array(playlist_df)
train_data = sparse.coo_matrix((np.ones(len(np_data), int), (np_data[:, 0], np_data[:, 1])))

lightfm_model = LightFM(loss='warp')

lightfm_model.fit(train_data, epochs=30, num_threads=2)

# rec = lightfm_recommendation(lightfm_model, train_data, playlist_df['track_id'], test_df.pid.values)
rec = lightfm_recommendation(lightfm_model, train_data, playlist_df['track_id'], [1, 5, 150])

output = build_output(rec, 'pid', 'track_id')

file_name = 'test2.csv'
team_name = 'RecSysCG'
contact_information = 'dimitreandrew@gmail.com'
output_submission(output, file_name, team_name, contact_information)
