% Write a prolog program to calculate the sum of two numbers.

% ------------------------------------------
% sum(X, Y, Result):-
%     This predicate succeeds if Result is the sum of X and Y.
%     X and Y must be numbers (integers or floats).
% ------------------------------------------

sum(X, Y, Result) :-
    number(X),            % Check X is a number
    number(Y),            % Check Y is a number
    Result is X + Y.      % Compute the sum using 'is' operator
