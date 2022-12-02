DSCH 2.7a
VERSION 11/6/2022 6:26:41 PM
BB(41,-10,114,65)
SYM  #nmos
BB(70,30,90,50)
TITLE 85 35  #nmos
MODEL 901
PROP   1.0u 0.12u                                                                                                                                                                                                       
REC(71,35,19,15,r)
VIS 2
PIN(90,50,0.000,0.000)s
PIN(70,40,0.000,0.000)g
PIN(90,30,0.030,0.140)d
LIG(80,40,70,40)
LIG(80,46,80,34)
LIG(82,46,82,34)
LIG(90,34,82,34)
LIG(90,30,90,34)
LIG(90,46,82,46)
LIG(90,50,90,46)
VLG  nmos nmos(drain,source,gate);
FSYM
SYM  #pmos
BB(70,5,90,25)
TITLE 85 10  #pmos
MODEL 902
PROP   2.0u 0.12u                                                                                                                                                                                                       
REC(71,10,19,15,r)
VIS 2
PIN(90,5,0.000,0.000)s
PIN(70,15,0.000,0.000)g
PIN(90,25,0.030,0.140)d
LIG(70,15,76,15)
LIG(78,15,78,15)
LIG(80,21,80,9)
LIG(82,21,82,9)
LIG(90,9,82,9)
LIG(90,5,90,9)
LIG(90,21,82,21)
LIG(90,25,90,21)
VLG  pmos pmos(drain,source,gate);
FSYM
SYM  #button1
BB(41,26,50,34)
TITLE 45 30  #button
MODEL 59
PROP                                                                                                                                                                                                           
REC(42,27,6,6,r)
VIS 1
PIN(50,30,0.000,0.000)inp
LIG(49,30,50,30)
LIG(41,34,41,26)
LIG(49,34,41,34)
LIG(49,26,49,34)
LIG(41,26,49,26)
LIG(42,33,42,27)
LIG(48,33,42,33)
LIG(48,27,48,33)
LIG(42,27,48,27)
FSYM
SYM  #vss
BB(85,57,95,65)
TITLE 89 62  #vss
MODEL 0
PROP                                                                                                                                                                                                            
REC(85,55,0,0,b)
VIS 0
PIN(90,55,0.000,0.000)vss
LIG(90,55,90,60)
LIG(85,60,95,60)
LIG(85,63,87,60)
LIG(87,63,89,60)
LIG(89,63,91,60)
LIG(91,63,93,60)
FSYM
SYM  #vdd
BB(85,-10,95,0)
TITLE 88 -4  #vdd
MODEL 1
PROP                                                                                                                                                                                                           
REC(0,0,0,0,)
VIS 0
PIN(90,0,0.000,0.000)vdd
LIG(90,0,90,-5)
LIG(90,-5,85,-5)
LIG(85,-5,90,-10)
LIG(90,-10,95,-5)
LIG(95,-5,90,-5)
FSYM
SYM  #light1
BB(108,10,114,24)
TITLE 110 24  #light
MODEL 49
PROP                                                                                                                                                                                                           
REC(109,11,4,4,r)
VIS 1
PIN(110,25,0.000,0.000)out
LIG(113,16,113,11)
LIG(113,11,112,10)
LIG(109,11,109,16)
LIG(112,21,112,18)
LIG(111,21,114,21)
LIG(111,23,113,21)
LIG(112,23,114,21)
LIG(108,18,114,18)
LIG(110,18,110,25)
LIG(108,16,108,18)
LIG(114,16,108,16)
LIG(114,18,114,16)
LIG(110,10,109,11)
LIG(112,10,110,10)
FSYM
CNC(70 30)
LIG(90,30,90,25)
LIG(90,55,90,50)
LIG(90,5,90,0)
LIG(90,25,110,25)
LIG(50,30,70,30)
LIG(70,30,70,15)
LIG(70,30,70,40)
FFIG D:\Program Files\DSCH2\Inverter_20101195.sch
