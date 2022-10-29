module vmachine(cash_in, rst, clk, buy, chg);
/*
cash_in=0, 10, 20 TK
price = 15 TK
Return:
00 = 0tk
01 = 5tk
10 = 10tk
11 = 15tk 
*/
	input [1:0] cash_in;
	input rst, clk;
	output reg buy;
	output reg [1:0] chg;
	
	reg current_state;
	reg next_state;
	
	parameter state0 = 1'b0, state1 = 1'b1;

	always @(current_state, cash_in)
	case (current_state)
		// 0tk state
		state0:	if (cash_in == 2'b00)
				begin
					next_state = state0;
					buy = 0;
					chg = 2'b00;
				end
				else if (cash_in == 2'b01)
				begin
					next_state = state1;
					buy = 0;
					chg = 2'b00;
				end
				else if (cash_in == 2'b11)
				begin
					next_state = state0;
					buy = 1;
					chg = 2'b01;
				end				
				default: chg = 2'bxx;	
		
		// 10tk state
		state1:	if (cash_in == 2'b00)
				begin
					next_state = state0;
					buy = 0;
					chg = 2'b10;
				end
				else if (cash_in == 2'b01)
				begin
					next_state = state0;
					buy = 1;
					chg = 2'b01;
				end
				else if (cash_in == 2'b11)
				begin
					next_state = state0;
					buy = 1;
					chg = 2'b11;
				end				
	endcase
	
	always @(posedge rst, posedge clk)
	if (rst == 1)
		current_state <= state0;
	else
		current_state <= next_state;

endmodule