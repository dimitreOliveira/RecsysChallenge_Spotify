library(dplyr)

artist <- read.csv2("../data/play_artist.csv", header = T, sep = ";", stringsAsFactors = F)

track <- read.csv2("../data/play_track_id.csv", header = T, sep = ";", stringsAsFactors = F)

artist_pid <- track %>%
  inner_join(artist, by = "track_uri") %>%
  select(track_id, artist_id)


df_artist_id <- read.csv2("../data/artist_freq_rating.csv", header = T, sep = ";", stringsAsFactors = F)
df_track_id <- read.csv2("../data/play_track_freq_rating.csv", header = T, sep = ";", stringsAsFactors = F)


artist_join_rating <- artist_pid %>%
  left_join(df_artist_id, by = "artist_id")


names1 <- c("track_id", "artist_id", "artist_count", "artist_rating")
colnames(artist_join_rating) <- names1


track_join_rating <- artist_join_rating %>%
  left_join(df_track_id, by = "track_id")
  

names2 <- c("track_id", "artist_id", "artist_count", "artist_rating", "track_count", "track_rating")

colnames(track_join_rating) <- names2

track_join_rating <- track_join_rating %>% 
  unique()

write.table(track_join_rating, file = "../data/track_artist_rating.csv",row.names=FALSE, na="",col.names=TRUE, sep=";")
