library(dplyr)

playlists <- read.csv2("../data/play_track.csv", header = T, sep = ";", stringsAsFactors = F)

playlists$track_id <- as.numeric(factor(playlists$track_uri, 
                                        levels=unique(playlists$track_uri)))

write.table(playlists, file = "../data/play_track_id.csv",row.names=FALSE, na="",col.names=TRUE, sep=";")