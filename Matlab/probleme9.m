% A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
% a2 + b2 = c2
% For example, 32 + 42 = 9 + 16 = 25 = 52.
% There exists exactly one Pythagorean triplet for which a + b + c = 1000.
% Find the product abc.


clear all; clc
nb = 1000;
cotesMin = round(nb/(sqrt(2)+2));
rep = 0;
for a = 1:cotesMin
    for b = cotesMin:nb/2
        if ((a+b+sqrt((a^2)+(b^2))) == nb)
            rep = a * b * sqrt((a^2)+(b^2));
        end
    end
end
rep
disp 'end'