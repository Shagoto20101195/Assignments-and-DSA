// 2 to 1 mux
module mux(w, s, y);
	input [1:0] w;
	input s;
	output y;
	
	assign g = ~s & w[0];
	assign h = s & w[1];
	assign y = g | h;
endmodule
