import os
import pandas as pd
import numpy as np
from keras import Input, Model
from keras.layers import Embedding, merge, Flatten, Dropout, Dense
from keras.optimizers import Adam
from keras.regularizers import l2

path = 'data/ml-latest-small/'
model_path = path + 'models/'
if not os.path.exists(model_path):
    os.mkdir(model_path)

ratings = pd.read_csv(path+'ratings.csv')
movie_names = pd.read_csv(path+'movies.csv').set_index('movieId')['title'].to_dict()

batch_size = 64
users = ratings.userId.unique()
movies = ratings.movieId.unique()
n_users = len(users)
n_movies = len(movies)

userid2idx = {o: i for i, o in enumerate(users)}
movieid2idx = {o: i for i, o in enumerate(movies)}

ratings.movieId = ratings.movieId.apply(lambda x: movieid2idx[x])
ratings.userId = ratings.userId.apply(lambda x: userid2idx[x])

user_min = ratings.userId.min()
user_max = ratings.userId.max()
movie_min = ratings.movieId.min()
movie_max = ratings.movieId.max()

msk = np.random.rand(len(ratings)) < 0.8
trn = ratings[msk]
val = ratings[~msk]

g = ratings.groupby('userId')['rating'].count()
topUsers = g.sort_values(ascending=False)[:15]


def embedding_input(name, n_in, n_out, reg):
    inp = Input(shape=(1,), dtype='int64', name=name)

    return inp, Embedding(n_in, n_out, input_length=1, embeddings_regularizer=l2(reg))(inp)


n_factors = 50

user_in, u = embedding_input('user_in', n_users, n_factors, 1e-4)
movie_in, m = embedding_input('movie_in', n_movies, n_factors, 1e-4)

x = merge([u, m], mode='concat')
x = Flatten()(x)
x = Dropout(0.3)(x)
x = Dense(70, activation='relu')(x)
x = Dropout(0.75)(x)
x = Dense(1)(x)
nn = Model([user_in, movie_in], x)
nn.compile(Adam(0.001), loss='mse')

print(nn.summary())

nn.fit([trn.userId, trn.movieId], trn.rating, batch_size=batch_size, epochs=1,
       validation_data=([val.userId, val.movieId], val.rating))

pre = nn.predict([trn.userId, trn.movieId])

print(pre)
