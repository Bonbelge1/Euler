%The prime factors of 13195 are 5, 7, 13 and 29.
%What is the largest prime factor of the number 600851475143 ?

clc; clear all;
nb = 600851475143;
M = []; nbFacteursTrouver = 0;
for i = 2: sqrt(nb)
    if (mod(nb,i)== 0)
        verification = 0; 
        for k = 1:nbFacteursTrouver
            verification = (verification + (mod(i,M(k)) == 0));
        end
        if ~verification
             nbFacteursTrouver = nbFacteursTrouver + 1;
             M(nbFacteursTrouver) = i;
        end
    end

end
M