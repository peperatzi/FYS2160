

N = 100;


T = linspace(.1,20, N);

C_v = zeros(N);

for i = 1:N-1
    C_v(i) = (3*exp(1/T(i))) / ((T(i)^2)*(1+3*exp(1/T(i)))^2);
end

plot(T, C_v)
xlabel('T');
ylabel('C_v');

pause()
