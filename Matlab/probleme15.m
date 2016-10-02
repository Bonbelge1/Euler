clear all;clc
%Création de la matrice
matrice = 5;
M = ones(matrice+1, matrice+1);
format long g
%
for x = 2:matrice+1
    M(x,x) = M(x-1,x) + M(x,x-1);
    for xx = x+1:matrice+1
        M(xx,x) = M(xx-1,x) + M(xx,x-1);
        M(x,xx) = M(x,xx-1) + M(x-1,xx);
    end
    M(matrice+1,matrice+1);
end
M
M(matrice+1, matrice+1)









