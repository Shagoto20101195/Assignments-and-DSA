// 4 bit adder
module adder(a, b, sum);
  input [3:0] a;
  input [3:0] b;
  output [4:0] sum;

  assign carry0 = 0;

  assign sum[0] = a[0] ^ b[0] ^ carry0;
  assign carry1 = (a[0] & b[0]) | ((a[0] ^ b[0]) & carry0);

  assign sum[1] = a[1] ^ b[1] ^ carry1;
  assign carry2 = (a[1] & b[1]) | ((a[1] ^ b[1]) & carry1);

  assign sum[2] = a[2] ^ b[2] ^ carry2;
  assign carry3 = (a[2] & b[2]) | ((a[2] ^ b[2]) & carry2);

  assign sum[3] = a[3] ^ b[3] ^ carry3;
  assign carry4 = (a[3] & b[3]) | ((a[3] ^ b[3]) & carry3);

  assign sum[4] = carry4;
endmodule
