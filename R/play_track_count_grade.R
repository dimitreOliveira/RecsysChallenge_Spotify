library(dplyr)

play_track_id <- read.csv2("../data/play_track_id.csv", header = T, sep = ";", stringsAsFactors = F)

df_count <- play_track_id %>%
              group_by(track_id)%>%
              summarise(n = n())


max_count <- max(df_count$n)

df_count_rate <- df_count %>%
                  mutate(count_rating = 100.0*(n/max_count))


write.table(df_count_rate, file = "../data/play_track_freq_rating.csv",row.names=FALSE, na="",col.names=TRUE, sep=";")
