# Write a Prolog program to implement GCD of two numbers

% -------------------------------------------
% gcd(A, B, GCD) :-
%     GCD is the greatest common divisor of A and B.
%     Uses the Euclidean algorithm.
% -------------------------------------------

gcd(A, 0, A).            % Base case: gcd(A, 0) = A
gcd(0, B, B).            % Base case: gcd(0, B) = B
gcd(A, B, GCD) :-        % Recursive case: gcd(A, B)
    A > B,                % If A > B
    A1 is A - B,          % Subtract B from A
    gcd(A1, B, GCD).      % Recursively calculate gcd(A1, B)

gcd(A, B, GCD) :-        % Recursive case: gcd(A, B)
    B > A,                % If B > A
    B1 is B - A,          % Subtract A from B
    gcd(A, B1, GCD).      % Recursively calculate gcd(A, B1)
