library(dplyr)

tracks <- read.csv2("../data/unique_tracks.csv", header = T, sep = ";", stringsAsFactors = F)

play_track <- read.csv2("../data/play_track.csv", header = T, sep = ";", stringsAsFactors = F)

tracks$artist_id <- as.numeric(factor(tracks$artist_uri, 
                                        levels=unique(tracks$artist_uri)))

tracks <- tracks %>%
            select(artist_id, track_uri)


artist_pid <- tracks %>%
              inner_join(play_track, by = "track_uri") %>%
              select(pid, artist_id)

write.table(tracks, file = "../data/play_artist.csv",row.names=FALSE, na="",col.names=TRUE, sep=";")