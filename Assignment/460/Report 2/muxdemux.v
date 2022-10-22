// 4 to 1 mux and 1 to 4 demux
module muxdemux(c, m_sel, d_sel, p);

input [3:0] c;
input [1:0] m_sel;
input [1:0] d_sel;
output reg [3:0] p;
reg a;

always@(*)
begin
	case(m_sel)
		0: a = c[0];
		1: a = c[1];
		2: a = c[2];
		3: a = c[3];
	endcase
	
	p = 4'bzzzz;
	case(d_sel)
		0: p[0] = a;
		1: p[1] = a;
		2: p[2] = a;
		3: p[3] = a;
	endcase
end

endmodule
