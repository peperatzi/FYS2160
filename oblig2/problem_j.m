
u = (0.01:0.01:3.0);

Z = zeros(length(u),1);

j = linspace(0,1000, 1000);

for i = 1:length(u)
    Z(i) = sum( (2*j + 1).*exp(-(j.*(j + 1))/u(i)));
end

plot(u,Z,'-b');
hold on
plot(u,u,'-r');
xlabel('T/\theta_r');
ylabel('Z');

pause();
