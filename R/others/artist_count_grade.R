library(dplyr)

artist <- read.csv2("../data/play_artist.csv", header = T, sep = ";", stringsAsFactors = F)

df_count <- artist %>%
  group_by(artist_id)%>%
  summarise(n = n())


max_count <- max(df_count$n)

df_count_rate <- df_count %>%
  mutate(count_rating = 100.0*(n/max_count))


write.table(df_count_rate, file = "../data/artist_freq_rating.csv",row.names=FALSE, na="",col.names=TRUE, sep=";")
