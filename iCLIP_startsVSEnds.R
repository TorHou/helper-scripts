library(dplyr)
library(ggplot2)

# A=read.table("/home/houwaart/Repositories/iCount/merged.f1m.bed",col.names=c("chrom","start","end","id","pcrd","strand"))
#A=read.table("/home/houwaart/Repositories/iCount/merged.bed",colClasses = c("character","integer","integer","NULL","NULL","character"),col.names=c("chrom","start","end","id","pcrd","strand"))
A=read.table("/home/houwaart/Repositories/iCount/PTBP1_r3.bed",colClasses = c("character","integer","integer","NULL","NULL","character"),col.names=c("chrom","start","end","id","pcrd","strand"))


Es <- A %>% group_by(chrom,strand,end) %>% summarize(counts = n()) 
Ss <- A %>% group_by(chrom,strand,start) %>% summarize(counts = n()) 

chrC <- A %>% group_by(chrom) %>% summarize(chromcounts = n()) %>% arrange(desc(chromcounts))

Ends <- bind_rows(Es %>% filter(strand=="+"), Ss %>% filter(strand=="-"))
Starts <- bind_rows(Es %>% filter(strand=="-"), Ss %>% filter(strand=="+"))


S_counts <- Starts %>% group_by(counts) %>% summarize(counter = n())
E_counts <- Ends %>% group_by(counts) %>% summarize(counter = n())
plot(S_counts)
points(E_counts, col="red")
head(E_counts)
plot(cumsum(head(S_counts$counts*S_counts$counter,20)),col="green");
points(cumsum(head(E_counts$counts*E_counts$counter,20)),col="red")

diffs=head(E_counts$counts*E_counts$counter,100)-head(S_counts$counts*S_counts$counter,100)
plot(cumsum(diffs))

plot(head(E_counts$counts*E_counts$counter,50),col="red");
points(head(S_counts$counts*S_counts$counter,50),col="green");

