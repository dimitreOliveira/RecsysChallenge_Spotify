import pickle
import numpy as np
import pandas as pd
import scipy.sparse as sparse
from lightfm import LightFM
from lightfm.evaluation import precision_at_k
from model import lightfm_recommendation
from dataset import build_output, output_submission

pd.set_option('display.width', 320)

playlist_data = 'data/rating_track_play_added_songs.csv'
test_data = 'data/pid_10k_sample.csv'

test_df = pd.read_csv(test_data, dtype=np.int32)
playlist_df = pd.read_csv(playlist_data, delimiter=';', dtype={'pid': int, 'track_id': int, 'rating': int})

users = playlist_df['pid'].unique()
songs = playlist_df['track_id'].unique()


print("----------------------------------------------------------------------")
print("Data set size: %s:" % len(playlist_df))
print("----------------------------------------------------------------------")
print("Unique user count: %s:" % len(users))
print("----------------------------------------------------------------------")
print("Unique Song count: %s:" % len(songs))
print("----------------------------------------------------------------------")


print("Sample of the data set")
print(playlist_df.head(5))

np_data = np.array(playlist_df)
train_data = sparse.coo_matrix((np.ones(len(np_data), int), (np_data[:, 0], np_data[:, 1])))

# LOAD MODEL
lightfm_model = pickle.load(open('models/model_20ep.pickle', "rb"))

# lightfm_model = LightFM(loss='warp')
# lightfm_model.fit(train_data, epochs=20, num_threads=2, verbose=2)
# # SAVE MODEL
# with open('models/model_20ep.pickle', 'wb') as fle:
#     pickle.dump(lightfm_model, fle, protocol=pickle.HIGHEST_PROTOCOL)


# USE WHOLE DATA SET TO PREDICTION
# rec = lightfm_recommendation(lightfm_model, train_data, playlist_df['track_id'], test_df.pid.values)
# output = build_output(rec, 'pid', 'track_id')
# file_name = 'test2.csv'
# team_name = 'RecSysCG'
# contact_information = 'dimitreandrew@gmail.com'
# output_submission(output, file_name, team_name, contact_information)


# PARTITION DATA SET TO PREDICTION
partitions = 7
size = len(test_df.pid.values) // partitions
index = 7     # range from 0 to "partitions"
rec_partition = lightfm_recommendation(lightfm_model, train_data, playlist_df['track_id'],
                                       test_df.pid.values[size * index:size * (index + 1)])
output = build_output(rec_partition, 'pid', 'track_id')
output.to_csv('submissions/partition%s.csv' % index)
# after creating all partitions run "join_partitions.py"
