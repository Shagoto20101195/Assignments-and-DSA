DSCH 2.7a
VERSION 11/6/2022 6:45:20 PM
BB(-4,-40,204,80)
SYM  #nmos
BB(40,45,60,65)
TITLE 55 50  #nmos
MODEL 901
PROP   1.0u 0.12u                                                                                                                                                                                                       
REC(41,50,19,15,r)
VIS 2
PIN(60,65,0.000,0.000)s
PIN(40,55,0.000,0.000)g
PIN(60,45,0.030,0.280)d
LIG(50,55,40,55)
LIG(50,61,50,49)
LIG(52,61,52,49)
LIG(60,49,52,49)
LIG(60,45,60,49)
LIG(60,61,52,61)
LIG(60,65,60,61)
VLG  nmos nmos(drain,source,gate);
FSYM
SYM  #nmos
BB(95,45,115,65)
TITLE 110 50  #nmos
MODEL 901
PROP   1.0u 0.12u                                                                                                                                                                                                       
REC(96,50,19,15,r)
VIS 2
PIN(115,65,0.000,0.000)s
PIN(95,55,0.000,0.000)g
PIN(115,45,0.030,0.280)d
LIG(105,55,95,55)
LIG(105,61,105,49)
LIG(107,61,107,49)
LIG(115,49,107,49)
LIG(115,45,115,49)
LIG(115,61,107,61)
LIG(115,65,115,61)
VLG  nmos nmos(drain,source,gate);
FSYM
SYM  #vss
BB(80,72,90,80)
TITLE 84 77  #vss
MODEL 0
PROP                                                                                                                                                                                                            
REC(80,70,0,0,b)
VIS 0
PIN(85,70,0.000,0.000)vss
LIG(85,70,85,75)
LIG(80,75,90,75)
LIG(80,78,82,75)
LIG(82,78,84,75)
LIG(84,78,86,75)
LIG(86,78,88,75)
FSYM
SYM  #pmos
BB(75,5,95,25)
TITLE 90 10  #pmos
MODEL 902
PROP   2.0u 0.12u                                                                                                                                                                                                       
REC(76,10,19,15,r)
VIS 2
PIN(95,5,0.000,0.000)s
PIN(75,15,0.000,0.000)g
PIN(95,25,0.030,0.280)d
LIG(75,15,81,15)
LIG(83,15,83,15)
LIG(85,21,85,9)
LIG(87,21,87,9)
LIG(95,9,87,9)
LIG(95,5,95,9)
LIG(95,21,87,21)
LIG(95,25,95,21)
VLG  pmos pmos(drain,source,gate);
FSYM
SYM  #pmos
BB(75,-25,95,-5)
TITLE 90 -20  #pmos
MODEL 902
PROP   2.0u 0.12u                                                                                                                                                                                                       
REC(76,-20,19,15,r)
VIS 2
PIN(95,-25,0.000,0.000)s
PIN(75,-15,0.000,0.000)g
PIN(95,-5,0.030,0.070)d
LIG(75,-15,81,-15)
LIG(83,-15,83,-15)
LIG(85,-9,85,-21)
LIG(87,-9,87,-21)
LIG(95,-21,87,-21)
LIG(95,-25,95,-21)
LIG(95,-9,87,-9)
LIG(95,-5,95,-9)
VLG  pmos pmos(drain,source,gate);
FSYM
SYM  #vdd
BB(90,-40,100,-30)
TITLE 93 -34  #vdd
MODEL 1
PROP                                                                                                                                                                                                           
REC(0,0,0,0,)
VIS 0
PIN(95,-30,0.000,0.000)vdd
LIG(95,-30,95,-35)
LIG(95,-35,90,-35)
LIG(90,-35,95,-40)
LIG(95,-40,100,-35)
LIG(100,-35,95,-35)
FSYM
SYM  #Inverter_20101195
BB(140,20,180,40)
TITLE 150 18  #Inverter_20101195
MODEL 6000
PROP                                                                                                                                                                                                           
REC(145,25,30,10,r)
VIS 5
PIN(140,30,0.000,0.000)inp
PIN(180,30,0.060,0.210)out
LIG(140,30,145,30)
LIG(175,30,180,30)
LIG(145,25,145,35)
LIG(145,25,175,25)
LIG(175,25,175,35)
LIG(175,35,145,35)
VLG  module Inverter_20101195( inp,out);
VLG   input inp;
VLG   output out;
VLG   nmos #(17) nmos(out,vss,inp); // 1.0u 0.12u
VLG   pmos #(17) pmos(out,vdd,inp); // 2.0u 0.12u
VLG  endmodule
FSYM
SYM  #light1
BB(198,15,204,29)
TITLE 200 29  #light
MODEL 49
PROP                                                                                                                                                                                                           
REC(199,16,4,4,r)
VIS 1
PIN(200,30,0.000,0.000)out
LIG(203,21,203,16)
LIG(203,16,202,15)
LIG(199,16,199,21)
LIG(202,26,202,23)
LIG(201,26,204,26)
LIG(201,28,203,26)
LIG(202,28,204,26)
LIG(198,23,204,23)
LIG(200,23,200,30)
LIG(198,21,198,23)
LIG(204,21,198,21)
LIG(204,23,204,21)
LIG(200,15,199,16)
LIG(202,15,200,15)
FSYM
SYM  #button2
BB(-4,11,5,19)
TITLE 0 15  #button
MODEL 59
PROP                                                                                                                                                                                                           
REC(-3,12,6,6,r)
VIS 1
PIN(5,15,0.000,0.000)inp2
LIG(4,15,5,15)
LIG(-4,19,-4,11)
LIG(4,19,-4,19)
LIG(4,11,4,19)
LIG(-4,11,4,11)
LIG(-3,18,-3,12)
LIG(3,18,-3,18)
LIG(3,12,3,18)
LIG(-3,12,3,12)
FSYM
SYM  #button1
BB(-4,-19,5,-11)
TITLE 0 -15  #button
MODEL 59
PROP                                                                                                                                                                                                           
REC(-3,-18,6,6,r)
VIS 1
PIN(5,-15,0.000,0.000)inp1
LIG(4,-15,5,-15)
LIG(-4,-11,-4,-19)
LIG(4,-11,-4,-11)
LIG(4,-19,4,-11)
LIG(-4,-19,4,-19)
LIG(-3,-12,-3,-18)
LIG(3,-12,-3,-12)
LIG(3,-18,3,-12)
LIG(-3,-18,3,-18)
FSYM
CNC(85 65)
CNC(95 40)
CNC(95 30)
CNC(20 -15)
CNC(65 15)
LIG(60,65,85,65)
LIG(85,70,85,65)
LIG(85,65,115,65)
LIG(95,-25,95,-30)
LIG(95,5,95,-5)
LIG(60,45,60,40)
LIG(60,40,95,40)
LIG(115,40,115,45)
LIG(95,40,95,30)
LIG(95,40,115,40)
LIG(95,30,140,30)
LIG(95,30,95,25)
LIG(180,30,200,30)
LIG(5,-15,20,-15)
LIG(5,15,65,15)
LIG(20,-15,20,55)
LIG(20,-15,75,-15)
LIG(20,55,40,55)
LIG(65,15,65,55)
LIG(65,15,75,15)
LIG(65,55,95,55)
FFIG D:\Program Files\DSCH2\OR_20101195.sch
