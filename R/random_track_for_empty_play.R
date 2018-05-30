library(dplyr)

#load data
track_play <- read.csv2("../data/play_track_id.csv", header = T, sep = ";", stringsAsFactors = F)

track_rank <- read.csv2("../data/rating_track_play_int.csv", header = T, sep = ";", stringsAsFactors = F)

play <- read.csv2("../data/challenge/playlists_challenge.csv", header = T, sep = ";", stringsAsFactors = F)


# selecting unique tracks
track_rank_unique_tracks <- track_rank %>%
  select(track_id, rating) %>%
  unique()

# creating dataframe with to 100 songs to be added to the playlist without tracks
track_rank_100 <- head(arrange(track_rank_unique_tracks, desc(rating)), 100)
track_rank_1000 <- track_rank_100[rep(1:nrow(track_rank_100),each=10),] 
random_1000 <- track_rank_1000[sample(nrow(track_rank_1000)),]


# adding tracks
play_without_songs <- play %>%
  filter(num_samples == 0) %>%
  select(pid)

play_added_songs <- cbind(play_without_songs, random_1000)

play_tracks <- rbind(track_rank, play_added_songs)

write.table(play_tracks, file = "../data/rating_track_play_added_songs.csv",row.names=FALSE, na="",col.names=TRUE, sep=";")

