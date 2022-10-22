// 4 bit counter
module counter(direction, reset, clock, count);

input direction;
input reset;
input clock;
output reg [3:0] count;

always@(posedge clock)
begin
	if(reset == 1)
		count <= 0;
	else if(direction == 1)
		count <= count + 1;
	else if(direction == 0)
		count <= count - 1;
end
endmodule
