

library(VennDiagram)

#library(Vennerable);

# SLBP p=0.01
overlap <- 482
p_cli <- 5920
p_pir <- 1212

# SLBP p=0.01 piranha_onENSBML
#overlap <- 436
#p_cli <- 5920
#p_pir <- 1119


# SLBP clipper 10p = 2.5, l2f>1
all_overlap <- 3217
overlap_cli_pir <- 195
overlap_cli_bbp <- 1778
overlap_pir_bbp <- 2248
p_cli <- 6319
p_pir <- 696
p_bbp <- 9823
#a <- Venn(SetNames = c("CLIPper", "Piranha","BBP"), Weight = c(0, p_cli, p_pir, overlap_cli_pir,p_bbp, overlap_cli_bbp,overlap_pir_bbp,all_overlap))

# SLBP clipper with deseq, l2f>1
all_overlap <- 3217
overlap_cli_pir <- 174
overlap_cli_bbp <- 1778
overlap_pir_bbp <- 2248
p_cli <- 2803
p_pir <- 717
p_bbp <- 9823

fr_cli <- p_cli/(p_cli+overlap_cli_bbp+overlap_cli_pir+all_overlap)
fr_pir <- p_pir/(p_pir+overlap_pir_bbp+overlap_cli_pir+all_overlap)
fr_bbp <- p_bbp/(p_bbp+overlap_cli_bbp+overlap_pir_bbp+all_overlap)

grid.newpage()
draw.triple.venn(area1 = all_overlap+p_cli+overlap_cli_bbp+overlap_cli_pir, area2 = all_overlap+p_pir+overlap_pir_bbp+overlap_cli_pir, area3 = all_overlap+p_bbp+overlap_pir_bbp+overlap_cli_bbp, n12 = all_overlap+overlap_cli_pir, n23 = all_overlap+overlap_pir_bbp, n13 = all_overlap+overlap_cli_bbp, 
                 n123 = all_overlap, category = c("CLIPper", "Piranha", "Ext. blockbuster"), lty = "blank", 
                 fill = c("#D7B174", "#A18C69", "#EBCC9A"), print.mode = c("raw","percent"),cat.cex=rep(1.5,3),cex=rep(1.5,7))



p_pira <- p_pir - overlap_pir_bbp - overlap_cli_pir - all_overlap
p_clia <- p_cli - overlap_cli_bbp - overlap_cli_pir - all_overlap
p_bbpa <- p_bbp - overlap_cli_bbp - overlap_pir_bbp - all_overlap

#b <- Venn(SetNames = c("CLIPper", "Piranha","BBP"), Weight = c(0, p_cli, p_pir, overlap_cli_pir,p_bbp, overlap_cli_bbp,overlap_pir_bbp,all_overlap))


#attach(mtcars)
#par(mfrow=c(1,2))
#plot(a)
#plot(b)

