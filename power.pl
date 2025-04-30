# Write a Prolog program to implement power (Num,Pow, Ans) : where Num is raised to the power Pow to get Ans.

% --------------------------------------------
% power(Num, Pow, Ans) :-
%     Num raised to the power Pow gives the result Ans.
% --------------------------------------------

power(_, 0, 1).          % Base case: Any number raised to the power 0 is 1
power(Num, Pow, Ans) :-
    Pow > 0,             % Ensure the exponent is positive
    Pow1 is Pow - 1,     % Decrease the exponent by 1
    power(Num, Pow1, Ans1),  % Recursively calculate power(Num, Pow1)
    Ans is Num * Ans1.   % Multiply Num by the result of power(Num, Pow1)
