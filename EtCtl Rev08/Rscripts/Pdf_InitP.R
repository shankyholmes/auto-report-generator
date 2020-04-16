#img <- readPNG("logo.png")
#k = textGrob(doc_title,gp=gpar(fontsize=25,col = "red",fontface = "bold"))
#my_g <- grobTree(rasterGrob(img, x = 0.01,hjust = 0))


ctdata = read.delim('out.csv',sep = ",")
#my_g2 = grobTree(textGrob("Files Analysed",gp=gpar(fontsize=15,fontface="bold",col = "black")),
#                 rasterGrob(img, x = 0.01,hjust = 0))

# myt <- ttheme_default(
#   colhead = list(fg_params=list(col="white"),
#                  bg_params=list(fill="red"))
# )


#tg = tableGrob(ctdata,theme = myt,row = NULL)
tgg = ggtexttable(ctdata, rows = NULL, theme = ttheme("mRed"))

# 
# my_g3 = grobTree(textGrob("Regen Duration and PoI1 Stats",gp=gpar(fontsize=15,fontface="bold",col = "black")),
#                  rasterGrob(img, x = 0.01,hjust = 0))

#extra plots
df1 = ctdata
df1$w1 = df1$T5_Avg*df1$ti.t5.550..s.
df1$w2 = df1$PoI1_a.mg.*df1$ti.poi1.0..s.

k1 = dplyr::group_by(df1,Strt.Count)
k2 = dplyr::summarise(k1,T5_Avg = round(sum(w1)/sum(ti.t5.550..s.),0),PoI1_avg = round(sum(w2)/sum(ti.poi1.0..s.),2),
                      RD_total = sum(ti_OnRoad.s.),RD_550=sum(ti.t5.550..s.),RD_poi1 = sum(ti.poi1.0..s.),
                      PoI1_lts = sum(PoI1_lts))

dfm <- melt(k2[,c('Strt.Count','RD_total','RD_poi1','RD_550')],id.vars = 1)

dfm$Strt.Count = as.factor(dfm$Strt.Count)
k2$Strt.Count = as.factor(k2$Strt.Count)

RDPlot = ggplot(dfm,aes(x=dfm$Strt.Count,y=value,fill = variable))+
  geom_bar(stat = "identity",position = 'dodge') +
  geom_text(aes(label=value),angle = 90,position = position_dodge(0.85),hjust =1)+
  theme_bw() +
  labs(x = "Regn Strt Cnt",title= "Regen Duration (secs)",y=NULL,subtitle = "pink: Total on-road regen duration| green: PoI1>0 Duration| blue: T5>550 Duration")+
  theme(axis.title.x = element_text(family = "serif"),axis.title.y = element_text(family = "serif"),
        title = element_text(family = "serif"),plot.title = element_text(face="bold"))


T5Plot = ggplot(k2,aes(x=k2$Strt.Count,y=k2$T5_Avg))+
  geom_bar(stat = "identity",position = 'dodge',fill = "red", color = "black") +
  geom_text(aes(label=round(k2$T5_Avg,0)),angle = 90,position = position_dodge(0.85),hjust =1)+
  theme_bw() +
  ylim(0,700)+
  labs(x = "Regn Strt Cnt",title= "T5 Average (degC)",y=NULL)+
  theme(axis.title.x = element_text(family = "serif"),axis.title.y = element_text(family = "serif"),
        title = element_text(family = "serif"),legend.position = "none",plot.title = element_text(face="bold"))

P1avplot = ggplot(k2,aes(x=k2$Strt.Count,y=k2$PoI1_avg))+
  geom_bar(stat = "identity",position = 'dodge',fill = "red", color = "black") +
  geom_text(aes(label=round(k2$PoI1_avg,2)),angle = 90,position = position_dodge(0.85),hjust =1)+
  theme_bw() +
  ylim(0,8)+
  labs(x = "Regn Strt Cnt",title= "Poi1 Average (mg/hub)",y=NULL)+
  theme(axis.title.x = element_text(family = "serif"),axis.title.y = element_text(family = "serif"),
        title = element_text(family = "serif"),legend.position = "none",plot.title = element_text(face="bold"))

str1= "Total PoI1 Consumed: "
str2 = toString(sum(k2$PoI1_lts))
str3 = " lts"
strf = paste(str1,str2,str3,sep = "",collapse = NULL)

P1lplot = ggplot(k2,aes(x=k2$Strt.Count,y=k2$PoI1_lts))+
  geom_bar(stat = "identity",position = 'dodge',fill = "red", color = "black") +
  geom_text(aes(label=round(k2$PoI1_lts,2)),angle = 90,position = position_dodge(0.85),hjust =1)+
  theme_bw() +
  labs(x = "Regn Strt Cnt",title= "Poi1 Integrated (lts)",y=NULL,subtitle = strf )+
  theme(axis.title.x = element_text(family = "serif"),axis.title.y = element_text(family = "serif"),
        title = element_text(family = "serif"),legend.position = "none",plot.title = element_text(face="bold"))