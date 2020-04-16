#T5 Line Graph
T5_line = ggplot(data,aes(x = data$timestamps))+
  geom_line(stat = "identity",aes(y=data$ETCtl_tOutrDes), size = 1, linetype = "dotted")+
  geom_line(stat = "identity",aes(y = data$Exh_tPFltUs), size = 1, colour = "red")+
  geom_line(stat = "identity",aes(y = data$Exh_tOxiCatUs), size = 1, colour = "green")+
  scale_y_continuous("Temperature (deg)",sec.axis = sec_axis(trans = ~.*(8/250),name = "poi1 (mg)", breaks = c(0:16)), breaks = seq(0,725,100),limits = c(0,725))+
  geom_line(stat = "identity",aes(y=(data$InjCrv_qPoI1Des_mp*(250/8))),size = 1, colour = "blue")+
  labs( x = "time",subtitle = "black: T5 SetPoint | red: T5 | green: T4 | blue: POI1" )+theme_bw()+
  theme(axis.title.x=element_blank())+
  theme(axis.title.y = element_text(size=10),plot.title = element_text(size=12))
  
vr_line = ggplot(data,aes(x = data$timestamps))+
  geom_line(stat = "identity",aes(y=data$VehV_v), size = 1, color= "black")+
  scale_y_continuous("Veh. Speed (km/h)",sec.axis = sec_axis(trans = ~.*(4000/100),name = "RPM", breaks = seq(0,4000,1000)), breaks = seq(0,100,25),limits = c(0,100))+
  geom_line(stat = "identity",aes(y=(data$Epm_nEng*(100/4000))),size = 1, colour = "red")+
  labs(x="Time",subtitle = "black: Vehicle Speed | red: Engine Speed")+theme_bw()+
  theme(axis.title.x=element_blank())+
  theme(axis.title.y = element_text(size=10),plot.title = element_text(size=12))
  

m_line = ggplot(data,aes(x = data$timestamps))+
  geom_line(stat = "identity",aes(y=data$PFltLd_mSot), size = 1, colour = "black")+
  geom_line(stat = "identity",aes(y = data$PFltLd_mSotMeasBas_mp), size = 1, colour = "red")+
  scale_y_continuous("Soot (g)",sec.axis = sec_axis(trans = ~.*(7/25),name = "Gear", breaks = c(0:6)), breaks = seq(0,25,5),limits = c(0,25))+
  geom_line(stat = "identity",aes(y=(data$Tra_numGear*(25/7))),size = 1, colour = "blue")+
  labs(x = "Time",subtitle= "black: PFLtLd_mSot | red: PFltLd_mSotMeasbas | blue: Gear")+theme_bw()+
  theme(axis.title.x=element_blank())+
  theme(axis.title.y = element_text(size=10),plot.title = element_text(size=12))

qp_line = ggplot(data,aes(x = data$timestamps))+
  geom_line(stat = "identity",aes(y=data$InjCtl_qSetUnBal), size = 1, color= "red")+
  #geom_line(stat = "identity",aes(y = data$APP_r), size = 1, colour = "blue")+
  scale_y_continuous("Quantity",sec.axis = sec_axis(trans = ~.*(1100/75),name = "EnvP_p(hpa)", breaks = seq(0,1100,200)), breaks = seq(0,100,25),limits = c(0,75))+
  geom_line(stat = "identity",aes(y=(data$EnvP_p*(75/1100))),size = 1, colour = "blue")+
  labs(x="Time",subtitle = "red: Quantity| blue: Env Pressure")+theme_bw()+
  theme(axis.title.x=element_blank())+
  theme(axis.title.y = element_text(size=10),plot.title = element_text(size=12))