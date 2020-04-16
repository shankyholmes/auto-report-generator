#T5 Line Graph

# temp_line = ggplot(data,aes(x = data$timestamps))+
#   geom_line(stat = "identity",aes(y=data$ETCtl_tOutrDes), size = 1, linetype = "dotted")+
#   geom_line(stat = "identity",aes(y = data$Exh_tPFltUs), size = 1, colour = "blue")+
#   scale_y_continuous("Temperature (deg)",sec.axis = sec_axis(trans = ~.*(12/600),name = "poi1 (mg)", breaks = c(0:12)), breaks = seq(0,700,100),limits = c(0,700))+
#   geom_line(stat = "identity",aes(y=(data$InjCrv_qPoI1Des_mp*(600/12))),size = 1, colour = "red")+
#   labs(y="Temperature", x="Time",title="T5 profile", subtitle = "black: T5 SetPoint | blue: T5 | red: POI1" )+theme_bw()

#T5 Histogram
t5_raw= cut(data$Exh_tPFltUs,seq(300,700,by = 50))
t5_table = table(t5_raw)
t5_table = transform(t5_table, Rel_Freq = prop.table(Freq))
t5_table = transform.data.frame(t5_table, percent = round(Rel_Freq*100,1))


t5_bar = ggplot(t5_table,aes(x = t5_table$t5_raw, y = t5_table$Rel_Freq))+
  geom_bar(fill = "red",stat = "identity", width = 0.75, colour ="black",position = position_nudge(x = 0.5))+
  geom_text(aes(label = t5_table$percent),hjust =1,angle = 90,fontface = "bold",position = position_nudge(0.5),size = 3.5)+
  scale_x_discrete(labels =  seq(from = 300, to = 700, by =50))+
  scale_y_continuous(labels = scales::percent_format(2))+
  labs(y=NULL, x="T5 (deg)",title="T5 Distribution" )+theme_bw() 

#Speed Histogram

veh_raw= cut(data$VehV_v,seq(0,120,by = 10))
veh_table = table(veh_raw)
veh_table = transform(veh_table, Rel_Freq = prop.table(Freq))
veh_table = transform.data.frame(veh_table, percent = round(Rel_Freq*100,1))


veh_bar = ggplot(veh_table,aes(x = veh_table$veh_raw, y = veh_table$Rel_Freq))+
  geom_bar(fill = "red",stat = "identity",width = 0.9,colour ="black", position = position_nudge(x = 0.5))+
  geom_text(aes(label = veh_table$percent),hjust =1,angle = 90,fontface = "bold",position = position_nudge(0.5),size = 3.5)+
  scale_x_discrete(labels =  seq(from = 0, to = 120, by =10))+
  scale_y_continuous(labels = scales::percent_format(2))+
  labs(y=NULL, x="vehicle Speed (km/hr)",title="Speed Distribution" )+theme_bw()

#T4 Histogram
t4_raw= cut(data$Exh_tOxiCatUs,seq(0,500,by = 50))
t4_table = table(t4_raw)
t4_table = transform(t4_table, Rel_Freq = prop.table(Freq))
t4_table = transform.data.frame(t4_table, percent = round(Rel_Freq*100,1))


t4_bar = ggplot(t4_table,aes(x = t4_table$t4_raw, y = t4_table$Rel_Freq))+
  geom_bar(fill = "red",stat = "identity", width = 0.9,colour ="black",  position = position_nudge(x = 0.5))+
  geom_text(aes(label = t4_table$percent),hjust =1,angle = 90,fontface = "bold",position = position_nudge(0.5),size = 3.5)+
  scale_x_discrete(labels =  seq(from = 0, to = 500, by = 50))+
  scale_y_continuous(labels = scales::percent_format(2))+
  labs(y=NULL, x="T4 (deg)",title="T4 Distribution" )+theme_bw()

#poi1 histogram
poi1_raw= cut(data$InjCrv_qPoI1Des_mp,seq(0,8,by = 1))
poi1_table = table(poi1_raw)
poi1_table = transform(poi1_table, Rel_Freq = prop.table(Freq))
poi1_table = transform.data.frame(poi1_table, percent = round(Rel_Freq*100,1))


poi1_bar = ggplot(poi1_table,aes(x = poi1_table$poi1_raw, y = poi1_table$Rel_Freq))+
  geom_bar(fill = "red",stat = "identity", width = 0.9,colour ="black",position = position_nudge(x = 0.5))+
  geom_text(aes(label = poi1_table$percent),hjust =1,angle = 90,fontface = "bold",position = position_nudge(0.5),size = 3.5)+
  scale_x_discrete(labels =  seq(from = 0, to = 9, by = 1))+
  scale_y_continuous(labels = scales::percent_format(2))+
  labs(y=NULL, x="poi1 (mg)",title="poi1 Distribution" )+theme_bw()  

#volume flow Histogram
volflw_raw= cut(data$ASMod_dvolPFltEG,seq(100,400,by = 50))
volflw_table = table(volflw_raw)
volflw_table = transform(volflw_table, Rel_Freq = prop.table(Freq))
volflw_table = transform.data.frame(volflw_table, percent = round(Rel_Freq*100,1))


volflw_bar = ggplot(volflw_table,aes(x = volflw_table$volflw_raw, y = volflw_table$Rel_Freq))+
  geom_bar(fill = "red",stat = "identity",width = 0.9,colour ="black", position = position_nudge(x = 0.5))+
  geom_text(aes(label = volflw_table$percent),hjust =1,angle = 90,fontface = "bold",position = position_nudge(0.5),size = 3.5)+
  scale_x_discrete(labels =  seq(from = 100, to = 400, by = 50))+
  scale_y_continuous(labels = scales::percent_format(2))+
  labs(y=NULL, x="Volume Flow",title="Volume Flow Distribution" )+theme_bw() 

#RPM Histogram
epm_raw= cut(data$Epm_nEng,seq(1000,4000,by = 500))
epm_table = table(epm_raw)
epm_table = transform(epm_table, Rel_Freq = prop.table(Freq))
epm_table = transform.data.frame(epm_table, percent = round(Rel_Freq*100,1))


epm_bar = ggplot(epm_table,aes(x = epm_table$epm_raw, y = epm_table$Rel_Freq))+
  geom_bar(fill = "red",stat = "identity", width =0.9, colour ="black",position = position_nudge(x = 0.5))+
  geom_text(aes(label = epm_table$percent),hjust =1,angle = 90,fontface = "bold",position = position_nudge(0.5),size = 3.5)+
  scale_x_discrete(labels =  seq(from = 1000, to = 4000, by = 500))+
  scale_y_continuous(labels = scales::percent_format(2))+
  labs(y=NULL, x="RPM",title="Engine RPM Distribution" )+theme_bw()

 #Injection Quantity
 injqnt_raw= cut(data$InjCtl_qSetUnBal,seq(0,60,by = 5))
 injqnt_table = table(injqnt_raw)
 injqnt_table = transform(injqnt_table, Rel_Freq = prop.table(Freq))
 injqnt_table = transform.data.frame(injqnt_table, percent = round(Rel_Freq*100,1))


 injqnt_bar = ggplot(injqnt_table,aes(x = injqnt_table$injqnt_raw, y = injqnt_table$Rel_Freq))+
   geom_bar(fill = "red",stat = "identity", width =0.9, colour ="black",position = position_nudge(x = 0.5))+
   geom_text(aes(label = injqnt_table$percent),hjust =1,angle = 90,fontface = "bold",position = position_nudge(0.5),size = 3.5)+
   scale_x_discrete(labels =  seq(from = 0, to = 60, by = 5))+
   scale_y_continuous(labels = scales::percent_format(2))+
  labs(y=NULL, x="Injection Quantity (mg)",title="Injection Quantity Dist." )+theme_bw()

#stSuc Line Graph
# suc_line = ggplot(data,aes(x = data$timestamps))+
#   geom_line(stat = "identity",aes(y = data$PFltRgn_ctRgnSuc), size = 1, colour = "blue")+
#   labs(y="", x="Time",title="Count" )+theme_bw()

#stage histogram
stage_raw= cut(data$CoEOM_numStageActTSync,seq(0,4,by=1))
stage_table = table(stage_raw)
stage_table = transform(stage_table, Rel_Freq = prop.table(Freq))
stage_table = transform.data.frame(stage_table, percent = round(Rel_Freq*100,1))


stage_bar = ggplot(stage_table,aes(x = stage_table$stage_raw, y = stage_table$Rel_Freq))+
  geom_bar(fill = "red",stat = "identity", width =0.9, colour ="black",position = position_nudge(x = 0.5))+
  geom_text(aes(label = stage_table$percent),hjust =1,angle = 90,fontface = "bold",position = position_nudge(0.5),size = 3.5)+
  scale_x_discrete(labels =  seq(from = 1, to = 4, by = 1))+
  scale_y_continuous(labels = scales::percent_format(2))+
  labs(y=NULL, x="Regen Stages",title="Stage" )+theme_bw()  

#operating pointss scatter
#Gear = factor(data$Tra_numGear)
# op_scat = ggplot(data)+
#   geom_point(aes(x = data$Epm_nEng, y = data$InjCtl_qSetUnBal,colour = Gear))+
#   scale_x_continuous(breaks =  seq(from = 500, to = 4000, by = 500),limits = c(750,3500))+
#   scale_y_continuous(breaks  =  seq(from = 0, to = 70, by = 10),limits = c(0,70))+
#   labs(x="Engine Speed (rpm)", y="Injection Quantity (mg)",title="Operating Points" )+theme_bw()

op_scat = ggplot(data)+
  geom_hex(aes(x = data$Epm_nEng, y = data$InjCtl_qSetUnBal),bins =50,show.legend = FALSE)+
  scale_x_continuous(breaks =  seq(from = 500, to = 4000, by = 500),limits = c(750,3500),labels=function(x)x/1000)+
  scale_y_continuous(breaks  =  seq(from = 0, to = 70, by = 10),limits = c(0,70))+
  scale_fill_continuous(type = "viridis")+
  labs(x="x1000 RPM", y="Injection Quantity (mg)",title="Operating Points" )+
  theme_bw()