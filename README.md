![](https://image.slidesharecdn.com/meetuprecsys2018-180202012155/95/meetup-recsys-challenge-2018-1-638.jpg?cb=1517534572)

# RecSys Challenge 2018

## About the repository
The goal of this repository is to get familliar with data process and machine learning applied to  recommender systems, this work uses the data from the 2018 RecSys Challenge sponsored by Spotify.

### What you will find
* Data loading, preprocessing and cleaning using R. [[link]](https://github.com/dimitreOliveira/RecsysChallenge_Spotify/tree/master/R)
* SVD model. [[link]](https://github.com/dimitreOliveira/RecsysChallenge_Spotify/blob/master/svd_lightfm.py)
* Check submission file requirements. [[link]](https://github.com/dimitreOliveira/RecsysChallenge_Spotify/blob/master/verify_submission.py)
* Process submission file to match required format. [[link]](https://github.com/dimitreOliveira/RecsysChallenge_Spotify/blob/master/R/translate_submission_track_uri.R)

### Welcome ACM RecSys Community! For this year's challenge, use the Spotify Million Playlist Dataset to help users create and extend their own playlists.

official challenge link: https://recsys-challenge.spotify.com/

datasets: https://recsys-challenge.spotify.com/dataset


### Challenge Overview

#### About
Spotify is an online music streaming service with over 140 million active users and over 30 million tracks. One of its popular features is the ability to create playlists, and the service currently hosts over 2 billion playlists.

This year's challenge focuses on music recommendation, specifically the challenge of automatic playlist continuation. By suggesting appropriate songs to add to a playlist, a Recommender System can increase user engagement by making playlist creation easier, as well as extending listening beyond the end of existing playlists.

#### General info
The RecSys Challenge 2018 is organized by Spotify, The University of Massachusetts, Amherst, and Johannes Kepler University, Linz. For information about the ACM RecSys Challenge Workshop, the Challenge timeline, and information on paper submission and selection criteria, be sure to visit the main ACM RecSys Challenge page.

#### The task
The goal of the challenge is to develop a system for the task of automatic playlist continuation. Given a set of playlist features, participants’ systems shall generate a list of recommended tracks that can be added to that playlist, thereby ‘continuing’ the playlist.

#### The dataset
As part of this challenge, Spotify has released the Million Playlist Dataset. It comprises a set of 1,000,000 playlists that have been created by Spotify users, and includes playlist titles, track listings and other metadata. In order to access the Million Playlist Dataset you will need to register for the challenge and agree to the license terms. Once you've registered you can download the data from the the dataset page.

### R Dependencies:
* [dplyr](https://dplyr.tidyverse.org/)

### Python Dependencies:
* [numpy](http://www.numpy.org/)
* [pandas](http://pandas.pydata.org/)
* [scipy](https://www.scipy.org/)
* [lightfm](https://lyst.github.io/lightfm/docs/home.html)

### To-Do:
* There was still some work to do to adjust the submission files to match the required format ("check.py" code).
* There's some work to do on the current model using LightFM, but probably other approaches should be tested.
