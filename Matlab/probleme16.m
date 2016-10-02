% 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
% What is the sum of the digits of the number 21000?

%% Initialisation
clear all; clc;

puissance = 1000; %2^puissance

add = 0; %initialisation de la retenue

%Initialisation des matrices
M = zeros(1,1000); %matrice des nombres
M(1) = 2;
nc = zeros(1,1000); %matrice qui compte le nb de chiffre dans les nombres
nc(1) = 1;

for y = 1:puissance-1
    x = 1;
    while x <= sum(nc)

        M(x) = 2 * M(x)+ add;
        add = 0;

        if M(x) >= 10
            nc(x+1) = 1;
            M(x) = M(x) - 10;
            add = 1;
        end
        x = x+1;
    end
    
end
sum(M)