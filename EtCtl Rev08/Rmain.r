rm(list=ls())
cat("\014") 

library(ggplot2)
library(gridExtra)
library(grid)
library(reticulate)
use_python(Sys.which('python'))
library(cowplot)
library(png)
library(reshape2)

p = import("rf_main")
doc_title = p$user_inp()
fileFolder = p$rf_fun()
print(fileFolder)
file_names = dir(fileFolder)

doc_name = paste0(doc_title,".pdf")

source("RScripts/Pdf_Init.R")


pdf(doc_name,width = 16,height = 9)
grid.arrange(my_g,k,heights =c (0.1,0.99))
offg = grid.arrange(tg,heights =c (0.1,0.99))


lay2 = rbind(c(1,1,1),c(2,3,4))
arrGrob2 = arrangeGrob(RDPlot,T5Plot,P1avplot,P1lplot,layout_matrix = lay2)
grid.arrange(my_g3,arrGrob2,heights =c (0.1,0.99))


for(i in 1:length(file_names)){
  
  print(file_names[i])
  data = read.delim(paste0(fileFolder,"/",file_names[i]),sep = ",");
  fsb = substr(file_names[i],1,nchar(file_names[i])-4)
  
  tt<- grobTree(textGrob(fsb,gp=gpar(fontsize=15,fontface="bold",col = "black")),
                   rasterGrob(img, x = 0.01,hjust = 0))
  source("RScripts/Line_Plots.R")
  l1 = cowplot::plot_grid(T5_line, vr_line, qp_line,m_line, align = "v", ncol = 1, rel_heights = c(2,1,1,1))
  #figure2 = grid.arrange(tt,l1,heights =c (0.1,0.99))
  
  source("RScripts/Hist_plots.R")

  lay = rbind(c(1,1,1,10,2,3),c(1,1,1,4,5,6),c(1,1,1,7,8,9))
  arrGrob = arrangeGrob(l1,t5_bar,t4_bar,veh_bar,poi1_bar,epm_bar,volflw_bar,injqnt_bar,stage_bar,op_scat,layout_matrix = lay)
  figure = grid.arrange(tt,arrGrob,heights =c (0.1,0.99))
  
}
dev.off()