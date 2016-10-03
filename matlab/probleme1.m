%If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
%Find the sum of all the multiples of 3 or 5 below 1000.

clc; clear all;
nb = 1000;
R = 0;

for i = 1:nb-1
    R = R + i*~((mod(i,3))&& (mod(i,5)));
end

R