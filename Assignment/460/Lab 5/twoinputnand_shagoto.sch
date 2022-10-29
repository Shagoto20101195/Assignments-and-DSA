DSCH 2.7a
VERSION 10/29/2022 9:26:32 AM
BB(-9,-35,164,80)
SYM  #button2
BB(-9,56,0,64)
TITLE -5 60  #button
MODEL 59
PROP                                                                                                                                                                                                           
REC(-8,57,6,6,r)
VIS 1
PIN(0,60,0.000,0.000)in2
LIG(-1,60,0,60)
LIG(-9,64,-9,56)
LIG(-1,64,-9,64)
LIG(-1,56,-1,64)
LIG(-9,56,-1,56)
LIG(-8,63,-8,57)
LIG(-2,63,-8,63)
LIG(-2,57,-2,63)
LIG(-8,57,-2,57)
FSYM
SYM  #nmos
BB(70,30,90,50)
TITLE 85 35  #nmos
MODEL 901
PROP   1.0u 0.12u                                                                                                                                                                                                       
REC(71,35,19,15,r)
VIS 2
PIN(90,50,0.000,0.000)s
PIN(70,40,0.000,0.000)g
PIN(90,30,0.030,0.210)d
LIG(80,40,70,40)
LIG(80,46,80,34)
LIG(82,46,82,34)
LIG(90,34,82,34)
LIG(90,30,90,34)
LIG(90,46,82,46)
LIG(90,50,90,46)
VLG  nmos nmos(drain,source,gate);
FSYM
SYM  #nmos
BB(70,50,90,70)
TITLE 85 55  #nmos
MODEL 901
PROP   1.0u 0.12u                                                                                                                                                                                                       
REC(71,55,19,15,r)
VIS 2
PIN(90,70,0.000,0.000)s
PIN(70,60,0.000,0.000)g
PIN(90,50,0.030,0.070)d
LIG(80,60,70,60)
LIG(80,66,80,54)
LIG(82,66,82,54)
LIG(90,54,82,54)
LIG(90,50,90,54)
LIG(90,66,82,66)
LIG(90,70,90,66)
VLG  nmos nmos(drain,source,gate);
FSYM
SYM  #pmos
BB(45,-10,65,10)
TITLE 60 -5  #pmos
MODEL 902
PROP   2.0u 0.12u                                                                                                                                                                                                       
REC(46,-5,19,15,r)
VIS 2
PIN(65,-10,0.000,0.000)s
PIN(45,0,0.000,0.000)g
PIN(65,10,0.030,0.210)d
LIG(45,0,51,0)
LIG(53,0,53,0)
LIG(55,6,55,-6)
LIG(57,6,57,-6)
LIG(65,-6,57,-6)
LIG(65,-10,65,-6)
LIG(65,6,57,6)
LIG(65,10,65,6)
VLG  pmos pmos(drain,source,gate);
FSYM
SYM  #pmos
BB(100,-10,120,10)
TITLE 115 -5  #pmos
MODEL 902
PROP   2.0u 0.12u                                                                                                                                                                                                       
REC(101,-5,19,15,r)
VIS 2
PIN(120,-10,0.000,0.000)s
PIN(100,0,0.000,0.000)g
PIN(120,10,0.030,0.210)d
LIG(100,0,106,0)
LIG(108,0,108,0)
LIG(110,6,110,-6)
LIG(112,6,112,-6)
LIG(120,-6,112,-6)
LIG(120,-10,120,-6)
LIG(120,6,112,6)
LIG(120,10,120,6)
VLG  pmos pmos(drain,source,gate);
FSYM
SYM  #vss
BB(85,72,95,80)
TITLE 89 77  #vss
MODEL 0
PROP                                                                                                                                                                                                            
REC(85,70,0,0,b)
VIS 0
PIN(90,70,0.000,0.000)vss
LIG(90,70,90,75)
LIG(85,75,95,75)
LIG(85,78,87,75)
LIG(87,78,89,75)
LIG(89,78,91,75)
LIG(91,78,93,75)
FSYM
SYM  #button1
BB(-9,36,0,44)
TITLE -5 40  #button
MODEL 59
PROP                                                                                                                                                                                                           
REC(-8,37,6,6,r)
VIS 1
PIN(0,40,0.000,0.000)in1
LIG(-1,40,0,40)
LIG(-9,44,-9,36)
LIG(-1,44,-9,44)
LIG(-1,36,-1,44)
LIG(-9,36,-1,36)
LIG(-8,43,-8,37)
LIG(-2,43,-8,43)
LIG(-2,37,-2,43)
LIG(-8,37,-2,37)
FSYM
SYM  #light1
BB(158,10,164,24)
TITLE 160 24  #light
MODEL 49
PROP                                                                                                                                                                                                           
REC(159,11,4,4,r)
VIS 1
PIN(160,25,0.000,0.000)out1
LIG(163,16,163,11)
LIG(163,11,162,10)
LIG(159,11,159,16)
LIG(162,21,162,18)
LIG(161,21,164,21)
LIG(161,23,163,21)
LIG(162,23,164,21)
LIG(158,18,164,18)
LIG(160,18,160,25)
LIG(158,16,158,18)
LIG(164,16,158,16)
LIG(164,18,164,16)
LIG(160,10,159,11)
LIG(162,10,160,10)
FSYM
SYM  #vdd
BB(80,-35,90,-25)
TITLE 83 -29  #vdd
MODEL 1
PROP                                                                                                                                                                                                           
REC(0,0,0,0,)
VIS 0
PIN(85,-25,0.000,0.000)vdd
LIG(85,-25,85,-30)
LIG(85,-30,80,-30)
LIG(80,-30,85,-35)
LIG(85,-35,90,-30)
LIG(90,-30,85,-30)
FSYM
CNC(90 10)
CNC(90 25)
CNC(25 40)
CNC(65 60)
CNC(85 -10)
LIG(65,-10,85,-10)
LIG(65,10,90,10)
LIG(90,30,90,25)
LIG(90,10,120,10)
LIG(0,40,25,40)
LIG(0,60,65,60)
LIG(90,25,160,25)
LIG(90,25,90,10)
LIG(25,40,25,0)
LIG(25,40,70,40)
LIG(25,0,45,0)
LIG(65,60,65,20)
LIG(65,60,70,60)
LIG(65,20,80,20)
LIG(80,20,80,0)
LIG(80,0,100,0)
LIG(85,-10,85,-25)
LIG(85,-10,120,-10)
FFIG D:\Shagoto\twoinputnand_shagoto.sch
