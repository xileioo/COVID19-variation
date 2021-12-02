library(Biostrings)
library(stringr)
library(ggplot2)
library(RColorBrewer)

setwd("D:/work/task_JZ/20211129_COVID19_variation_GUI")

#--------COVID19------------------------------------
miss_match_num <- readRDS("COVID19_mismatch_20211112.rds")
aa <- readAAStringSet("D:/work/task_JZ/20211109_COVID19_variation/COVID19/output.fa")
length(aa)
#[1] 3813015
mydata <- as.data.frame(aa)
mydata <- strsplit(mydata$x,"")
mydata <- as.data.frame(do.call(rbind,mydata)) 

mydata$miss_match_num <- miss_match_num
mydata <- mydata[mydata$miss_match_num %in% c(0:8),]
dim(mydata)
#[1] 3722275     202
mydata <- mydata[,-202]

colnames(mydata) <- paste0(mydata[1,],331:(331+ncol(mydata)-1))

mydata_t <- as.data.frame(apply(mydata, 2, paste, collapse = ""))

colnames(mydata_t) = "AA"

df <- data.frame(loc = rownames(mydata_t),
                 A = as.character(mydata[1,]),
                 AA = mydata_t$AA)

df$Matchcount_COVID19 <- str_count(df$AA, df$A)

df$variation_COVID19 <- 1 - df$Matchcount_COVID19 / nchar(df$AA[1])
df <- df[,-3]
#-----------------------------------------------------------------------

#--------Sarbecovirus------------------------------------
aa <- readAAStringSet("RBD_aa_aligned.fasta")

mydata <- as.data.frame(aa)
mydata <- strsplit(mydata$x,"")
mydata <- as.data.frame(do.call(rbind,mydata))
mydata <- mydata[,-43]
colnames(mydata) <- paste0(mydata[1,],331:(331+ncol(mydata)-1))
mydata_t <- as.data.frame(apply(mydata, 2, paste, collapse = ""))
colnames(mydata_t) = "AA"

df$AA = mydata_t$AA
df$Matchcount_Sarbecovirus <- str_count(df$AA, df$A)
df$variation_Sarbecovirus <- 1 - df$Matchcount_Sarbecovirus / nchar(df$AA[1])
df <- df[,-5]

df$loc2 <- substr(df$loc,2,4)
df$loc3 <- 1:nrow(df)

write.csv(df,"1_variation_COVID19_Sarbecovirus.csv",
          quote = F,row.names = F)

