
% Calculate partition function Z
u = (0.01:0.01:3.0);

Z = zeros(length(u),1);

j = linspace(0,1000, 1001);

for i = 1:length(u)
    Z(i) = sum( (2*j + 1).*exp(-(j.*(j + 1))/u(i)));
end

% User Z as partition function
du = u(2:end)-u(1:end-1);
u_1 = (u(1:end-1)+u(2:end))*0.5;

logZ = log(Z);

U = u_1.^2.*diff(logZ)'./du;
ddu = 0.5*(du(1:end-1)+du(2:end));
CV = diff(U)./ddu;
u2 = u(2:end-1);

%plot(u_1,U);
%xlabel('u')
%ylabel('U(u)')

plot(u2,CV);
xlabel('u')
ylabel('C_V(u)');

pause();
