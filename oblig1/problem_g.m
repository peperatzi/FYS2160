% problem_g

% Setup
N = 101;

N_A = 30;
N_B = 70;

% Setup
q_a = zeros(1,N);
P = zeros(1,N);

% Make it so
q_b = 0;
for i = 1:N
    q_a(i) = 100 - q_b;
    P(i) = (nchoosek(q_a(i) + N_A - 1, q_a(i))*nchoosek(q_b + N_B - 1, q_b)) / nchoosek((q_a(i) + q_b) + (N_A + N_B) - 1, q_a(i) + q_b);
    q_b++;
end

%q_a
%P
plot(q_a, P);
xlabel('q_a');
ylabel('P(q_a)')


pause()

