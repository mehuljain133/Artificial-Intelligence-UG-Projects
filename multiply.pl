# Prolog program to implement multi (N1, N2, R) : where N1 and N2 denotes the numbers to be multiplied and R represents the result

% --------------------------------------------
% multi(N1, N2, R) :-
%     R is the result of multiplying N1 and N2.
% --------------------------------------------

multi(0, _, 0).          % Base case: Any number multiplied by 0 is 0
multi(_, 0, 0).          % Base case: Any number multiplied by 0 is 0
multi(N1, N2, R) :-
    N2 > 0,              % If N2 is greater than 0
    N2_1 is N2 - 1,      % Decrease N2 by 1
    multi(N1, N2_1, R1), % Recursively calculate multi(N1, N2-1, R1)
    R is R1 + N1.        % The result is R1 + N1

multi(N1, N2, R) :-
    N2 < 0,              % If N2 is less than 0 (handle negative multiplier)
    N2_1 is N2 + 1,      % Increase N2 by 1 (making it less negative)
    multi(N1, N2_1, R1), % Recursively calculate multi(N1, N2+1, R1)
    R is R1 - N1.        % The result is R1 - N1 (since N2 is negative)
