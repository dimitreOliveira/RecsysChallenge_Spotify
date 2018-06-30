library(dplyr)

# Add track name
submissions <- read.csv2("../data/challenge/submission.csv", header = T, sep = ",", stringsAsFactors = F)
start <- "spotify:track:"


new <- submissions %>% select(pid)

#info <- as.data.frame(lapply(info, as.numeric)) 
for(i in colnames(submissions)){
  if(i != "pid"){
    df <- submissions[,c("pid", i)]
    
    names <- c("pid", "track_id")
    colnames(df) <- names
    
    df$track_id <- paste0(start, df$track_id)
    
    
    names <- c("pid", i)
    colnames(df) <- names
    
    df <- df %>% select(-pid)
    
    new <- cbind(new, df)
    
  }
}

write.table(new, file = "../submissions/submission.csv",row.names=FALSE, na="",col.names=TRUE, sep=",")

