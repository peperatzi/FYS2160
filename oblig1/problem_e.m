% proglem_e.m


% Setup
q = 6;
N_A = 2;
N_B = 2;



% Setup 
P = zeros(q+1,1);
a_mult = zeros(q+1,1);
b_mult = zeros(q+1,1);
ab_mult = zeros(q+1,1);

disp('q_value   A_mult  B_mult  AB_mult P(q_A)')

% Calculate
tot_mult = nchoosek( (q+N_A+N_B-1) ,q);
for i=1:(q+1)
    q_A = q-(i-1);
    a_mult = nchoosek( (q_A+N_A-1) , q_A);
    b_mult = nchoosek( (q-q_A+N_B-1) ,(q-q_A));
    ab_mult = a_mult*b_mult;
    P = a_mult*b_mult/tot_mult;
    disp(sprintf('%i        %g      %g      %g      %g', i-1, a_mult, b_mult, ab_mult, P));
end


% Output:
% q_value   A_mult  B_mult  AB_mult P(q_A)
% 0         7       1        7      0.0833333
% 1         6       2       12      0.142857
% 2         5       3       15      0.178571
% 3         4       4       16      0.190476
% 4         3       5       15      0.178571
% 5         2       6       12      0.142857
% 6         1       7        7      0.0833333

