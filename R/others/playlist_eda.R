library(dplyr)

playlists <- read.csv2("../data/playlists.csv", header = T, sep = ";", stringsAsFactors = F)

# checking uniques
unique_playlists <- nrow(distinct(playlists, pid))

# just numeric data
playlists$collaborative[playlists$collaborative == "true"] <- 1
playlists$collaborative[playlists$collaborative == "false"] <- 0
playlists$collaborative <- as.numeric(playlists$collaborative)

summary(playlists)
p_num <- playlists %>% select(-name)

cor(p_num, method = c("pearson"))
