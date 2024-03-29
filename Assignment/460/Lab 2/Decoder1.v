// 3 to 8 decoder
module Decoder1(in, out);
input [2:0] in;
output reg [7:0] out;

always@(*)
begin
	out = 0;
	case(in)
		0:
			out[0] = 1;
		1:
			out[1] = 1;
		2:
			out[2] = 1;
		3:
			out[3] = 1;
		4:
			out[4] = 1;
		5:
			out[5] = 1;
		6:
			out[6] = 1;
		7:
			out[7] = 1;
	endcase
end
endmodule
