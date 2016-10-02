%The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
%Find the sum of all the primes below two million.


clear all;clc
b=1; %Nb a regarder sil est premier
a=1; %Combien de nombre premiers jai trouvé
M = [2 3]; %Matrice des nombre premier
while a~=10001
   b = b+2;
   k = 0;
   x = 1;
   while (k == 0)  && (x <= a) && (M(x) <= (sqrt(b)))
      k = ~mod(b,M(x));
      x=x+1;
   end
   if (k == 0)
      a=a+1;
      M(a)=b;
   end
end
M(a)
