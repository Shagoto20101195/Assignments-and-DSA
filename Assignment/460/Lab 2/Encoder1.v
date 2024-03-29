// 4 to 2 encoder
module Encoder1(in, out);
input [3:0] in;
output reg [1:0] out;

always@(*)
begin
	// 4'b = 4 bit binary 2'b = 2 bit binary
	case(in)
		4'b0001: out = 2'b00;
		4'b0010: out = 2'b01;
		4'b0100: out = 2'b10;
		4'b1000: out = 2'b11;
		default: out = 2'bzz;
	endcase
end
endmodule
