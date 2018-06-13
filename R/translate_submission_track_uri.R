library(dplyr)

# translating track id in int to track_uri


track_play <- read.csv2("../data/play_track_id.csv", header = T, sep = ";", stringsAsFactors = F)
submissions <- read.csv2("../submissions/submission1.csv", header = T, sep = ",", stringsAsFactors = F)
test <- submissions

info <- track_play[, c(2, 4)]
new <- submissions %>% select(pid)

name <- "trackuri_"
for(i in colnames(submissions)){
  if(i != "pid"){
    df <- submissions[,c("pid", i)]
    
    names <- c("pid", "track_id")
    colnames(df) <- names
    
    df_join <- df %>%
      inner_join(info, by = c("track_id")) %>%
      distinct() %>%
      select(-pid)
    
    
    names <- c("track_id", i)
    colnames(df_join) <- names
    
    df_join <- df_join %>% select(-track_id)
    
    new <- cbind(new, df_join)
    
  }
}

write.table(new, file = "../submissions/submission.csv",row.names=FALSE, na="",col.names=TRUE, sep=",")

count <- 0
for(i in colnames(submissions)){
  if(i != "pid"){
    df <- submissions[,c(i)]
    
    n <- length(unique(df))
    if(n < 10000){
      count <- count + 1
    }
    
  }
}

print(count)

