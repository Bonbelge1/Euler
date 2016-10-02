%A palindromic number reads the same both ways.
%The largest palindrome made from the product of two 2-digit
%numbers is 9009 = 91 × 99.
%Find the largest palindrome made from the product
%of two 3-digit numbers.

clc; clear all;

for x = 9:-1:0
    for y = 9:-1:0
        for z = 9:-1:0
            M = [x y z];
            nb = M(1)*100000+M(2)*10000+ M(3)*1000+M(3)*100+M(2)*10+M(1);
            b = 1;
            i = round(sqrt(nb));
            while b && (i > 1)
                if ((mod(nb,i))==0) && (i>=100) && ((nb/i)<1000) && (nb>=100000)
                    b = 0;
                    fprintf('%d = %d * %d\n',nb,i,nb/i)
                end
                i = i-1;
            end
        end
    end
end