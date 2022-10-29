DSCH 2.7a
VERSION 10/29/2022 10:17:36 AM
BB(-109,-45,239,60)
SYM  #twoinputnand_shagoto
BB(120,-40,160,-10)
TITLE 130 -42  #twoinputnand_shagoto
MODEL 6000
PROP                                                                                                                                                                                                           
REC(125,-35,30,20,r)
VIS 5
PIN(120,-20,0.000,0.000)B
PIN(120,-30,0.000,0.000)A
PIN(160,-30,0.060,0.420)Y
LIG(120,-20,125,-20)
LIG(120,-30,125,-30)
LIG(155,-30,160,-30)
LIG(125,-35,125,-15)
LIG(125,-35,155,-35)
LIG(155,-35,155,-15)
LIG(155,-15,125,-15)
VLG  module twoinputnand_shagoto( B,A,Y);
VLG   input B,A;
VLG   output Y;
VLG   nmos #(24) nmos(Y,w2,A); // 1.0u 0.12u
VLG   nmos #(10) nmos(w2,vss,B); // 1.0u 0.12u
VLG   pmos #(24) pmos(Y,vdd,A); // 2.0u 0.12u
VLG   pmos #(24) pmos(Y,vdd,B); // 2.0u 0.12u
VLG  endmodule
FSYM
SYM  #twoinputnand_shagoto
BB(15,-40,55,-10)
TITLE 25 -42  #twoinputnand_shagoto
MODEL 6000
PROP                                                                                                                                                                                                           
REC(20,-35,30,20,r)
VIS 5
PIN(15,-20,0.000,0.000)B
PIN(15,-30,0.000,0.000)A
PIN(55,-30,0.060,0.350)Y
LIG(15,-20,20,-20)
LIG(15,-30,20,-30)
LIG(50,-30,55,-30)
LIG(20,-35,20,-15)
LIG(20,-35,50,-35)
LIG(50,-35,50,-15)
LIG(50,-15,20,-15)
VLG module twoinputnand_shagoto( B,A,Y);
VLG  input B,A;
VLG  output Y;
VLG  nmos #(24) nmos(Y,w2,A); // 1.0u 0.12u
VLG  nmos #(10) nmos(w2,vss,B); // 1.0u 0.12u
VLG  pmos #(24) pmos(Y,vdd,A); // 2.0u 0.12u
VLG  pmos #(24) pmos(Y,vdd,B); // 2.0u 0.12u
VLG endmodule
FSYM
SYM  #twoinputnand_shagoto
BB(15,10,55,40)
TITLE 25 8  #twoinputnand_shagoto
MODEL 6000
PROP                                                                                                                                                                                                           
REC(20,15,30,20,r)
VIS 5
PIN(15,30,0.000,0.000)B
PIN(15,20,0.000,0.000)A
PIN(55,20,0.060,0.350)Y
LIG(15,30,20,30)
LIG(15,20,20,20)
LIG(50,20,55,20)
LIG(20,15,20,35)
LIG(20,15,50,15)
LIG(50,15,50,35)
LIG(50,35,20,35)
VLG  module twoinputnand_shagoto( B,A,Y);
VLG   input B,A;
VLG   output Y;
VLG   nmos #(24) nmos(Y,w2,A); // 1.0u 0.12u
VLG   nmos #(10) nmos(w2,vss,B); // 1.0u 0.12u
VLG   pmos #(24) pmos(Y,vdd,A); // 2.0u 0.12u
VLG   pmos #(24) pmos(Y,vdd,B); // 2.0u 0.12u
VLG  endmodule
FSYM
SYM  #twoinputnand_shagoto
BB(115,10,155,40)
TITLE 125 8  #twoinputnand_shagoto
MODEL 6000
PROP                                                                                                                                                                                                           
REC(120,15,30,20,r)
VIS 5
PIN(115,30,0.000,0.000)B
PIN(115,20,0.000,0.000)A
PIN(155,20,0.060,0.420)Y
LIG(115,30,120,30)
LIG(115,20,120,20)
LIG(150,20,155,20)
LIG(120,15,120,35)
LIG(120,15,150,15)
LIG(150,15,150,35)
LIG(150,35,120,35)
VLG  module twoinputnand_shagoto( B,A,Y);
VLG   input B,A;
VLG   output Y;
VLG   nmos #(24) nmos(Y,w2,A); // 1.0u 0.12u
VLG   nmos #(10) nmos(w2,vss,B); // 1.0u 0.12u
VLG   pmos #(24) pmos(Y,vdd,A); // 2.0u 0.12u
VLG   pmos #(24) pmos(Y,vdd,B); // 2.0u 0.12u
VLG  endmodule
FSYM
SYM  #clock1
BB(-15,-3,0,3)
TITLE -10 0  #clock
MODEL 69
PROP   10.00 10.00                                                                                                                                                                                                       
REC(-13,-2,6,4,r)
VIS 1
PIN(0,0,1.500,0.280)clk1
LIG(-5,0,0,0)
LIG(-10,-2,-12,-2)
LIG(-6,-2,-8,-2)
LIG(-5,-3,-5,3)
LIG(-15,3,-15,-3)
LIG(-10,2,-10,-2)
LIG(-8,-2,-8,2)
LIG(-8,2,-10,2)
LIG(-12,2,-14,2)
LIG(-12,-2,-12,2)
LIG(-5,3,-15,3)
LIG(-5,-3,-15,-3)
FSYM
SYM  #inverter_shagoto
BB(-50,40,-10,60)
TITLE -40 38  #inverter_shagoto
MODEL 6000
PROP                                                                                                                                                                                                           
REC(-45,45,30,10,r)
VIS 5
PIN(-50,50,0.000,0.000)A
PIN(-10,50,0.060,0.280)Y
LIG(-50,50,-45,50)
LIG(-15,50,-10,50)
LIG(-45,45,-45,55)
LIG(-45,45,-15,45)
LIG(-15,45,-15,55)
LIG(-15,55,-45,55)
VLG  module inverter_shagoto( A,Y);
VLG   input A;
VLG   output Y;
VLG   pmos #(17) pmos(Y,vdd,A); // 2.0u 0.12u
VLG   nmos #(17) nmos(Y,vss,A); // 1.0u 0.12u
VLG  endmodule
FSYM
SYM  #light2
BB(233,10,239,24)
TITLE 235 24  #light
MODEL 49
PROP                                                                                                                                                                                                           
REC(234,11,4,4,r)
VIS 1
PIN(235,25,0.000,0.000)Q_inv
LIG(238,16,238,11)
LIG(238,11,237,10)
LIG(234,11,234,16)
LIG(237,21,237,18)
LIG(236,21,239,21)
LIG(236,23,238,21)
LIG(237,23,239,21)
LIG(233,18,239,18)
LIG(235,18,235,25)
LIG(233,16,233,18)
LIG(239,16,233,16)
LIG(239,18,239,16)
LIG(235,10,234,11)
LIG(237,10,235,10)
FSYM
SYM  #button2
BB(-109,-34,-100,-26)
TITLE -105 -30  #button
MODEL 59
PROP                                                                                                                                                                                                           
REC(-108,-33,6,6,r)
VIS 1
PIN(-100,-30,0.000,0.000)D
LIG(-101,-30,-100,-30)
LIG(-109,-26,-109,-34)
LIG(-101,-26,-109,-26)
LIG(-101,-34,-101,-26)
LIG(-109,-34,-101,-34)
LIG(-108,-27,-108,-33)
LIG(-102,-27,-108,-27)
LIG(-102,-33,-102,-27)
LIG(-108,-33,-102,-33)
FSYM
SYM  #light1
BB(233,-45,239,-31)
TITLE 235 -31  #light
MODEL 49
PROP                                                                                                                                                                                                           
REC(234,-44,4,4,r)
VIS 1
PIN(235,-30,0.000,0.000)Q
LIG(238,-39,238,-44)
LIG(238,-44,237,-45)
LIG(234,-44,234,-39)
LIG(237,-34,237,-37)
LIG(236,-34,239,-34)
LIG(236,-32,238,-34)
LIG(237,-32,239,-34)
LIG(233,-37,239,-37)
LIG(235,-37,235,-30)
LIG(233,-39,233,-37)
LIG(239,-39,233,-39)
LIG(239,-37,239,-39)
LIG(235,-45,234,-44)
LIG(237,-45,235,-45)
FSYM
CNC(-65 -30)
CNC(185 -20)
CNC(185 15)
LIG(0,-20,0,20)
LIG(0,-20,15,-20)
LIG(235,30,235,25)
LIG(0,20,15,20)
LIG(-10,50,10,50)
LIG(10,50,10,30)
LIG(10,30,15,30)
LIG(220,30,235,30)
LIG(-100,-30,-65,-30)
LIG(-65,-30,-65,50)
LIG(-65,-30,15,-30)
LIG(-65,50,-50,50)
LIG(55,-30,120,-30)
LIG(55,20,115,20)
LIG(160,-30,185,-30)
LIG(185,-30,185,-20)
LIG(185,-10,85,-10)
LIG(85,-10,85,30)
LIG(85,30,115,30)
LIG(155,20,185,20)
LIG(185,20,185,15)
LIG(185,0,100,0)
LIG(100,0,100,-20)
LIG(100,-20,120,-20)
LIG(185,-20,235,-20)
LIG(185,-20,185,-10)
LIG(235,-20,235,-30)
LIG(185,15,220,15)
LIG(185,15,185,0)
LIG(220,15,220,30)
FFIG D:\Shagoto\plevel_dlatch_shagoto.sch
