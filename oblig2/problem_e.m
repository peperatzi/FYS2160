

N = 100;

Ttheta = [0.01 0.025 0.1 0.5 0.75 1.0];
C = ['-r' '-g' '-b' 'c' 'm' 'y'];

F = zeros(N);

for i=1:length(Ttheta)
    j = linspace(1,20,N);
    F = (2*j + 1).*exp(-j.*(j + 1)*Ttheta(i));
    plot(j, F, C(i))
    hold on
end

xlabel('j')
ylabel('T/\theta_r')
legend('T/\theta=0.01','T/\theta0.025', 'T/\=theta0.1','T/\theta=0.5','T/\theta=0.75','T/\theta=1.0')

pause()
