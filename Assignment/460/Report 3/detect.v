// Detect 101
module detect(Clock, Resetn, w, s);

input Clock;
input Resetn;
input w;
output s;

reg [2:0] next;
reg [2:0] current;

parameter [2:0] A = 3'b000;
parameter [2:0] B = 3'b001;
parameter [2:0] C = 3'b010;
parameter [2:0] D = 3'b011;

always@(*)
begin
	case(current)
		A:
			if(w == 1) next = B;
			else next = A;
		B:
			if(w == 0) next = C;
			else next = B;
		C:
			if(w == 1) next = D;
			else next = A;
		D:
			if(w == 1) next = B;
			else next = C;
		default: next = 3'bxxx;
	endcase
end

always@(posedge Clock, negedge Resetn)
begin
	if(Resetn == 0) current <= A;
	else current <= next;
end

assign s = (current == D);

endmodule
