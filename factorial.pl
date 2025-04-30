# Write a program in PROLOG to implement factorial (N, F) where F represents thefactorial of a number N.

% ---------------------------------------------
% factorial(N, F) :-
%     F is the factorial of N, i.e., N! = N * (N-1) * ... * 1.
% ---------------------------------------------

factorial(0, 1).               % Base case: factorial(0) is 1
factorial(N, F) :-
    N > 0,                     % Ensure N is a positive integer
    N1 is N - 1,               % Decrement N by 1
    factorial(N1, F1),         % Recursively compute factorial(N1)
    F is N * F1.               % Multiply N with factorial(N-1)
