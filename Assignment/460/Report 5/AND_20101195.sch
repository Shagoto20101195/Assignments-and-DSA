DSCH 2.7a
VERSION 11/6/2022 6:46:08 PM
BB(6,-20,199,90)
SYM  #button1
BB(6,36,15,44)
TITLE 10 40  #button
MODEL 59
PROP                                                                                                                                                                                                            
REC(7,37,6,6,r)
VIS 1
PIN(15,40,0.000,0.000)inp1
LIG(14,40,15,40)
LIG(6,44,6,36)
LIG(14,44,6,44)
LIG(14,36,14,44)
LIG(6,36,14,36)
LIG(7,43,7,37)
LIG(13,43,7,43)
LIG(13,37,13,43)
LIG(7,37,13,37)
FSYM
SYM  #light1
BB(193,10,199,24)
TITLE 195 24  #light
MODEL 49
PROP                                                                                                                                                                                                            
REC(194,11,4,4,r)
VIS 1
PIN(195,25,0.000,0.000)out
LIG(198,16,198,11)
LIG(198,11,197,10)
LIG(194,11,194,16)
LIG(197,21,197,18)
LIG(196,21,199,21)
LIG(196,23,198,21)
LIG(197,23,199,21)
LIG(193,18,199,18)
LIG(195,18,195,25)
LIG(193,16,193,18)
LIG(199,16,193,16)
LIG(199,18,199,16)
LIG(195,10,194,11)
LIG(197,10,195,10)
FSYM
SYM  #pmos
BB(50,0,70,20)
TITLE 65 5  #pmos
MODEL 902
PROP   2.0u 0.12u                                                                                                                                                                                                        
REC(51,5,19,15,r)
VIS 2
PIN(70,0,0.000,0.000)s
PIN(50,10,0.000,0.000)g
PIN(70,20,0.030,0.280)d
LIG(50,10,56,10)
LIG(58,10,58,10)
LIG(60,16,60,4)
LIG(62,16,62,4)
LIG(70,4,62,4)
LIG(70,0,70,4)
LIG(70,16,62,16)
LIG(70,20,70,16)
VLG   pmos pmos(drain,source,gate);
FSYM
SYM  #pmos
BB(100,0,120,20)
TITLE 115 5  #pmos
MODEL 902
PROP   2.0u 0.12u                                                                                                                                                                                                        
REC(101,5,19,15,r)
VIS 2
PIN(120,0,0.000,0.000)s
PIN(100,10,0.000,0.000)g
PIN(120,20,0.030,0.280)d
LIG(100,10,106,10)
LIG(108,10,108,10)
LIG(110,16,110,4)
LIG(112,16,112,4)
LIG(120,4,112,4)
LIG(120,0,120,4)
LIG(120,16,112,16)
LIG(120,20,120,16)
VLG   pmos pmos(drain,source,gate);
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
PIN(90,30,0.030,0.280)d
LIG(80,40,70,40)
LIG(80,46,80,34)
LIG(82,46,82,34)
LIG(90,34,82,34)
LIG(90,30,90,34)
LIG(90,46,82,46)
LIG(90,50,90,46)
VLG   nmos nmos(drain,source,gate);
FSYM
SYM  #nmos
BB(70,55,90,75)
TITLE 85 60  #nmos
MODEL 901
PROP   1.0u 0.12u                                                                                                                                                                                                        
REC(71,60,19,15,r)
VIS 2
PIN(90,75,0.000,0.000)s
PIN(70,65,0.000,0.000)g
PIN(90,55,0.030,0.070)d
LIG(80,65,70,65)
LIG(80,71,80,59)
LIG(82,71,82,59)
LIG(90,59,82,59)
LIG(90,55,90,59)
LIG(90,71,82,71)
LIG(90,75,90,71)
VLG   nmos nmos(drain,source,gate);
FSYM
SYM  #vss
BB(85,82,95,90)
TITLE 89 87  #vss
MODEL 0
PROP                                                                                                                                                                                                            
REC(85,80,0,0,b)
VIS 0
PIN(90,80,0.000,0.000)vss
LIG(90,80,90,85)
LIG(85,85,95,85)
LIG(85,88,87,85)
LIG(87,88,89,85)
LIG(89,88,91,85)
LIG(91,88,93,85)
FSYM
SYM  #Inverter_20101195
BB(140,15,180,35)
TITLE 150 13  #Inverter_20101195
MODEL 6000
PROP                                                                                                                                                                                                            
REC(145,20,30,10,r)
VIS 5
PIN(140,25,0.000,0.000)inp
PIN(180,25,0.060,0.210)out
LIG(140,25,145,25)
LIG(175,25,180,25)
LIG(145,20,145,30)
LIG(145,20,175,20)
LIG(175,20,175,30)
LIG(175,30,145,30)
VLG   module Inverter_20101195( inp,out);
VLG    input inp;
VLG    output out;
VLG    nmos #(17) nmos(out,vss,inp); // 1.0u 0.12u
VLG    pmos #(17) pmos(out,vdd,inp); // 2.0u 0.12u
VLG   endmodule
FSYM
SYM  #button2
BB(6,61,15,69)
TITLE 10 65  #button
MODEL 59
PROP                                                                                                                                                                                                            
REC(7,62,6,6,r)
VIS 1
PIN(15,65,0.000,0.000)inp2
LIG(14,65,15,65)
LIG(6,69,6,61)
LIG(14,69,6,69)
LIG(14,61,14,69)
LIG(6,61,14,61)
LIG(7,68,7,62)
LIG(13,68,7,68)
LIG(13,62,13,68)
LIG(7,62,13,62)
FSYM
SYM  #vdd
BB(105,-20,115,-10)
TITLE 108 -14  #vdd
MODEL 1
PROP                                                                                                                                                                                                            
REC(0,0,0,0,)
VIS 0
PIN(110,-10,0.000,0.000)vdd
LIG(110,-10,110,-15)
LIG(110,-15,105,-15)
LIG(105,-15,110,-20)
LIG(110,-20,115,-15)
LIG(115,-15,110,-15)
FSYM
CNC(90 25)
CNC(120 25)
CNC(45 40)
CNC(30 65)
CNC(110 -5)
LIG(90,80,90,75)
LIG(110,-5,120,-5)
LIG(70,20,70,25)
LIG(70,25,90,25)
LIG(120,25,120,20)
LIG(90,30,90,25)
LIG(90,25,120,25)
LIG(90,55,90,50)
LIG(120,25,140,25)
LIG(180,25,195,25)
LIG(15,40,45,40)
LIG(15,65,30,65)
LIG(45,40,45,10)
LIG(45,40,70,40)
LIG(45,10,50,10)
LIG(30,65,30,-10)
LIG(30,65,70,65)
LIG(30,-10,100,-10)
LIG(100,-10,100,10)
LIG(70,0,70,-5)
LIG(70,-5,110,-5)
LIG(120,-5,120,0)
LIG(110,-5,110,-10)
FFIG D:\Program Files\DSCH2\AND_20101195.sch
