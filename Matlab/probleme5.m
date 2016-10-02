clc;clc; clear all;
tic
rep = 0;
a = 20;

while (mod(a,19)||mod(a,18)||mod(a,17)||mod(a,16)||mod(a,15)||mod(a,14)||mod(a,13)||mod(a,12)||mod(a,11))
    a = a + 20;
    rep = a;
    end
rep
toc

% 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
% What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
% 232792560

clc; clear all;
tic
tic
rep = 0;
a = 20;

while (a ~= 0)
    a = a + 20;
    rep = a;
    a = a * (mod(a,20)||mod(a,19)||mod(a,18)||mod(a,17)||mod(a,16)||mod(a,15)||mod(a,14)||mod(a,13)||mod(a,12)||mod(a,11));
end
rep
toc



k = 20-1;
v = 0;
for y = 1:20
    for x = k:-1:1
        M(1,x+v) = y;
        M(2,x+v) = 20-x+1;
        M(3,x+v) = y*(20-x+1);
    end
    v = v+k;
    k=k-1;
end

%% Identification des produits semblables

% for i=1:1
%
% g = 1;
% [nl,nc] = size(M);
% for x = 1:length(M)
%     for y = (x+1):length(M)
%
%         if (M(nl,x) == M(nl,y))
%
%             for h = 1:nl-1
%                 R(h,g) = M(h,y);
%             end
%
%             for h = 1:nl-1
%                 R(h+nl-1,g) = M(h,x);
%             end
%
%             R(2*nl-1,g) = M(nl,x);
%
%             g = g + 1;
%         end
%     end
% end
% M=R;
%
%
% end
% M



for i=1:1
    g = 1;
    [nl,nc] = size(M);
    for x = 1:length(M)
        for y = (x+1):length(M)

            if (M(nl,x) == M(nl,y))
                R(g) = union(M(x),M(y),'rows');
                g = g + 1;
            end
        end
    end
   
end
R
M

% 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
% What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
% 232792560


