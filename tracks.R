library(Gviz)
library(Rsamtools)
library(GenomicFeatures)
library(TxDb.Hsapiens.UCSC.hg19.knownGene)
ls('package:TxDb.Hsapiens.UCSC.hg19.knownGene')


txdb <- "TxDb.Hsapiens.UCSC.hg19.knownGene::TxDb.Hsapiens.UCSC.hg19.knownGene"



afrom <- 149858780
#afrom <- 149858880
ato <-   149858975


#D7B174	A18C69	8B6526	EBCC9A	EBD4AF
#D7C174	A19569	8B7526	EBD99A	EBDEAF
#79C74	A18069	8B4F26	EBBA9A	EBC7AF

clipper_col <- "#D7B174"
pir_col <- "#A18C69"
bam_col <- "#AAAAAA"
ctrl_col <- "#AA0000"
starts_col <- "#AAAAAA"
block_col <- "#EBCC9A"
gene_col <- "#AAA9A2"
line_col <- "#555555"

iTrack <- IdeogramTrack(chromosome="chr1",genome = "hg19",fontcolor="black")

my_path <- "/home/houwaart/Projects/FoldChange_vs_Affinity/SLBP/"
sigstartsFile <- paste(my_path,"ENCFF036FAN.secondInPair.starts.bedgraph",sep="")
ctrlstartsFile <- paste(my_path,"ENCFF913HKF.secondInPair.starts.bedgraph",sep="")
signalBamFile <- paste(my_path,"ENCFF036FAN.secondInPair.bam",sep="")
signalBedgraphFile <- paste(my_path,"ENCFF036FAN.secondInPair.bedgraph",sep="")
controlBamFile <- paste(my_path,"ENCFF913HKF.secondInPair.bam",sep="")

clipperPeaks <- paste(my_path,"clipper.filtered.bed",sep="")
pirPeaks1 <- paste(my_path,"piranha.sorted.tbl.bed",sep="")
blockPeaks <- paste(my_path,"ppt.ds.filter_l2fg1.tbl.bed",sep="")
#pirPeaks2 <- "/home/houwaart/Desktop/Datenanalyse für Paper/HNRNPA1/piranha_peaks_b20_a995.bed"
#pirPeaks3 <- "/home/houwaart/Desktop/Datenanalyse für Paper/HNRNPA1/piranha_peaks_b20_a99.bed"

#bmt <- GeneRegionTrack(TxDb.Hsapiens.UCSC.hg19.knownGene, chromosom="chr1", start=afrom, end=ato)


gTrack <- GenomeAxisTrack(littleTicks = FALSE,from=afrom,to=ato,fontcolor="black",col="black")
sigTrack <- AlignmentsTrack(col=line_col,range=signalBamFile,genome="hg19",chromosome=1,isPaired=TRUE,type="coverage",name="signal coverage",background.title=bam_col,fill=bam_col)
ctrlTrack <- AlignmentsTrack(col=line_col,range=controlBamFile,genome="hg19",chromosome=1,isPaired=TRUE,type="coverage",name="control coverage",background.title=bam_col,fill=ctrl_col,alpha=0.4,max=100)

clipperTrack <- AnnotationTrack(col=line_col,clipperPeaks,start = afrom, end=ato, name = "Clipper",background.title=clipper_col,fill=clipper_col)
pirTrack1 <- AnnotationTrack(pirPeaks1,start = afrom, end=ato, name = "+",stacking="hide",background.title=pir_col,fill=pir_col)
blockTrack <- AnnotationTrack(col=line_col,blockPeaks,start = afrom, end=ato, stacking="hide",name="Block- based",background.title=block_col,fill=block_col)
sigstartsTrack <- DataTrack(sigstartsFile, name = "read starts", type = "histogram",background.title=starts_col)
ctrlstartsTrack <- DataTrack(ctrlstartsFile, name = "read starts", type = "histogram",background.title=starts_col,fill=starts_col,ylim=c(0,30),fill=ctrl_col,alpha=0.6)
motifTrack <- AnnotationTrack(start = c(149858941),width = 16, chromosome = "chr1", strand = c("+"), id = c("SLM"),genome = "hg19", name = "", shape="box",featureAnnotation = "id",background.title=bam_col,fill=bam_col,col="black")


dsigTrack<-DataTrack(range=signalBamFile,genome="hg19",chromosome=1,type="histogram",name="coverage")
dctrlTrack<-DataTrack(range=controlBamFile,genome="hg19",chromosome=1,type="histogram",ylim=c(0,170),fill=ctrl_col,alpha=0.6,name="coverage")
#displayPars(clipperTrack) <- list(col="red")
otcov <- OverlayTrack(trackList = list(dsigTrack, dctrlTrack),background.title=bam_col,name = "coverage")
otstarts <- OverlayTrack(trackList = list(sigstartsTrack, ctrlstartsTrack),background.title=bam_col,name = "starts")

#pirTrack2 <- AnnotationTrack(pirPeaks2,start = afrom, end=ato, col=acol, stacking = "squish")
#pirTrack3 <- AnnotationTrack(pirPeaks3,start = afrom, end=ato, col=acol)
t1p<-pirTrack1@range[pirTrack1@range@strand=='+']
t1m<-pirTrack1@range[pirTrack1@range@strand=='-']
#t2p<-pirTrack2@range[pirTrack2@range@strand=='+']
#t2m<-pirTrack2@range[pirTrack2@range@strand=='-']
#t3p<-pirTrack3@range[pirTrack3@range@strand=='+']
#t3m<-pirTrack3@range[pirTrack3@range@strand=='-']
pirTrack1p <- AnnotationTrack(col=line_col,t1p,start = afrom, end=ato, name = "Piranha",background.title=pir_col,fill=pir_col)
#pirTrack1m <- AnnotationTrack(t1m,start = afrom, end=ato, name = "1-")
#pirTrack2p <- AnnotationTrack(t2p,start = afrom, end=ato, name = "P2")
#pirTrack2m <- AnnotationTrack(t2m,start = afrom, end=ato, name = "2-")
#pirTrack3p <- AnnotationTrack(t3p,start = afrom, end=ato, name = "P3")
#pirTrack3m <- AnnotationTrack(t3m,start = afrom, end=ato, name = "3-")

bmt <- BiomartGeneRegionTrack(fontcolor="black",just.group="below",col="black", genome = "hg19", chromosome = "chr1",start = afrom, end = ato, name="",shape="arrow",background.title="white",transcriptAnnotation="symbol",collapseTranscripts = "shortest",arrowHeadMaxWidth=8)
bmtMotifTrack <- OverlayTrack(trackList=list(bmt,motifTrack),background.title="white")
#feature(bmt) <- rep("region",18)
#plotTracks(list(iTrack,gTrack,aTrack,clipperTrack,pirTrack1p,pirTrack1m,pirTrack2p,pirTrack2m,pirTrack3p,pirTrack3m,bmt),from = afrom,to = ato,chromosome = "chr13",type="coverage",background.panel = "#FFFEDB",sizes=c(0.1,0.1,0.1,0.1,0.1,0.033,0.1,0.033,0.1,0.033,0.1))
plotTracks(list(iTrack,gTrack,bmtMotifTrack,otcov,otstarts,clipperTrack,blockTrack,pirTrack1p),protein_coding=gene_col,utr3=gene_col, from = afrom,to = ato,chromosome = "chr1",background.panel = "#FFFEDB",sizes=c(0.05,0.1,0.05,0.15,0.15,0.1,0.1,0.1))
#plotTracks(list(iTrack,gTrack,aTrack),from = afrom,to = ato,chromosome = "chr1",type="coverage",background.panel = "#FFFEDB",sizes=c(0.1,0.1,0.1,0.1))

#dTrack <- DataTrack(range=bamFile, genome="hg19", name="Coverage", window=-1, chromosome="chr1", importFunction=strandedBamImport, stream=TRUE)
#plotTracks(aTrack, from = 1, to = 100000, col=c("red", "blue"), groups=c("+", "-"), type="coverage", col.histogram=NA)
