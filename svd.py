import numpy as np
import csv
import math as mt
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import *
from sparsesvd import sparsesvd

playlist_data = 'data/rating_track_play_added_songs.csv'
test_data = 'data/pid_10k_sample.csv'
# constants defining the dimensions of our User Rating Matrix (URM)
MAX_PID = 37143
MAX_UID = 15375


def readUrm():
    urm = np.zeros(shape=(MAX_UID, MAX_PID), dtype=np.float32)
    with open(playlist_data, 'rb') as trainFile:
        urmReader = csv.reader(trainFile, delimiter=',')
        for row in urmReader:
            urm[int(row[0]), int(row[1])] = float(row[2])

    return csr_matrix(urm, dtype=np.float32)


def readUsersTest():
    uTest = dict()
    with open(test_data, 'rb') as testFile:
        testReader = csv.reader(testFile, delimiter=',')
        for row in testReader:
            uTest[int(row[0])] = list()

    return uTest


def getMoviesSeen():
    moviesSeen = dict()
    with open("./trainSample.csv", 'rb') as trainFile:
        urmReader = csv.reader(trainFile, delimiter=',')
        for row in urmReader:
            try:
                moviesSeen[int(row[0])].append(int(row[1]))
            except:
                moviesSeen[int(row[0])] = list()
                moviesSeen[int(row[0])].append(int(row[1]))

    return moviesSeen


def computeSVD(urm, K):
    U, s, Vt = sparsesvd(urm, K)

    dim = (len(s), len(s))
    S = np.zeros(dim, dtype=np.float32)
    for i in range(0, len(s)):
        S[i,i] = mt.sqrt(s[i])

    U = csr_matrix(np.transpose(U), dtype=np.float32)
    S = csr_matrix(S, dtype=np.float32)
    Vt = csr_matrix(Vt, dtype=np.float32)

    return U, S, Vt


def computeEstimatedRatings(urm, U, S, Vt, uTest, moviesSeen, K, test):
    rightTerm = S*Vt

    estimatedRatings = np.zeros(shape=(MAX_UID, MAX_PID), dtype=np.float16)
    for userTest in uTest:
        prod = U[userTest, :]*rightTerm

        #we convert the vector to dense format in order to get the indices of the movies with the best estimated ratings
        estimatedRatings[userTest, :] = prod.todense()
        recom = (-estimatedRatings[userTest, :]).argsort()[:250]
        for r in recom:
            if r not in moviesSeen[userTest]:
                uTest[userTest].append(r)

                if len(uTest[userTest]) == 5:
                    break

    return uTest
