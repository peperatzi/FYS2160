% problem_m

%
N = 60;
n = 50000;
s = zeros(n, 1);

%
for i = 1:n
    A = randi([0,1],N,1);
    S_plus = sum(A);
    S_minus = N - S_plus;
    s(i) = (S_plus-S_minus)/2;
end

%
mean_s = -sum(s)/n;
n_vec = 1:n;
plot(n_vec, -s);
hold on
plot([0 n], [mean_s mean_s], 'r--')
xlabel('Microstate "')
ylabel('Energy')
legend('Total E in microstate', 'Mean energy')
hold off

%
figure()
hist(-s, 50)
xlabel('Energy of the system')
ylabel('Number of occurences')
hold on
plot_vec = linspace(-20,20,n);
y = 5150*exp(-2*plot_vec.^2/N);
plot(plot_vec, y, 'r--')
legend('Histogram of results','Normal distribution')


pause()



