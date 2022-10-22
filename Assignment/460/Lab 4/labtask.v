module labtask(cash_in, rst, clk, purchase, cash_return);
/*
cash_in=0,5,10,20 TK
price = 20 TK
*/
	input [1:0] cash_in;
	input rst, clk;
	output reg purchase;
	output reg [1:0] cash_return;
	
	reg [1:0] current_state;
	reg [1:0] next_state;
	
	parameter state0 = 2'b00, state1 = 2'b01, state2 = 2'b10, state3 = 2'b11;

	always @(current_state, cash_in)
	case (current_state)
		// 0tk state
		state0:	if (cash_in == 2'b00)
				begin
					next_state = state0;
					purchase = 0;
					cash_return = 2'b00;
				end
				else if (cash_in ==2'b01)
				begin
					next_state = state1;
					purchase = 0;
					cash_return = 2'b00;
				end
				else if (cash_in ==2'b10)
				begin
					next_state = state2;
					purchase = 0;
					cash_return = 2'b00;
				end				
				else if (cash_in ==2'b11)
				begin
					next_state = state0;
					purchase = 1;
					cash_return = 2'b00;
				end		
		
		// 5tk state
		state1:	if (cash_in == 2'b00)
				begin
					next_state = state0;
					purchase = 0;
					cash_return = 2'b01;
				end
				else if (cash_in ==2'b01)
				begin
					next_state = state2;
					purchase = 0;
					cash_return = 2'b00;
				end
				else if (cash_in ==2'b10)
				begin
					next_state = state3;
					purchase = 0;
					cash_return = 2'b00;
				end				
				else if (cash_in ==2'b11)
				begin
					next_state = state0;
					purchase = 1;
					cash_return = 2'b01;
				end
		
		// 10tk state	
		state2:	if (cash_in == 2'b00)
				begin
					next_state = state0;
					purchase = 0;
					cash_return = 2'b10;
				end
				else if (cash_in ==2'b01)
				begin
					next_state = state3;
					purchase = 0;
					cash_return = 2'b00;
				end
				else if (cash_in ==2'b10)
				begin
					next_state = state0;
					purchase = 1;
					cash_return = 2'b00;
				end				
				else if (cash_in ==2'b11)
				begin
					next_state = state0;
					purchase = 1;
					cash_return = 2'b10;
				end
		
		// 15tk state
		state3:	if (cash_in == 2'b00)
				begin
					next_state = state0;
					purchase = 0;
					cash_return = 2'b11;
				end
				else if (cash_in ==2'b01)
				begin
					next_state = state0;
					purchase = 1;
					cash_return = 2'b00;
				end
				else if (cash_in ==2'b10)
				begin
					next_state = state0;
					purchase = 1;
					cash_return = 2'b01;
				end				
				else if (cash_in ==2'b11)
				begin
					next_state = state0;
					purchase = 1;
					cash_return = 2'b11;
				end

	endcase
	
	always @(posedge rst, posedge clk)
	if (rst == 1)
		current_state <= state0;
	else
		current_state <= next_state;

endmodule
