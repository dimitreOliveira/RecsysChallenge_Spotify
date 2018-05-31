library(dplyr)

track_play <- read.csv2("../data/play_track_id.csv", header = T, sep = ";", stringsAsFactors = F)

track_rank <- read.csv2("../data/play_track_freq_rating.csv", header = T, sep = ";", stringsAsFactors = F)

df_join <- track_play %>%
  inner_join(track_rank, by = "track_id") %>%
  select(pid, track_id, count_rating)

df_join <- df_join %>% 
  unique()


df_join_m <- df_join %>% 
  mutate(rating = as.integer(round(as.numeric(count_rating), 0))) %>%
  select(-count_rating)

df_sample <- head(df_join_m, 10000)

write.table(df_sample, file = "../data/sample_rating_track_play_int.csv",row.names=FALSE, na="",col.names=TRUE, sep=";")
write.table(df_join_m, file = "../data/rating_track_play_int.csv",row.names=FALSE, na="",col.names=TRUE, sep=";")
