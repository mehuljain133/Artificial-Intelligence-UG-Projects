% Write a program in PROLOG to implement generate_fib(N,T) where T represents the Nth term of the fibonacci series

% ---------------------------------------------
% generate_fib(N, T) :-
%     T is the Nth term of the Fibonacci series.
%     Base cases:
%     fib(0) = 0, fib(1) = 1
% ---------------------------------------------

generate_fib(0, 0).      % Base case: The 0th Fibonacci number is 0
generate_fib(1, 1).      % Base case: The 1st Fibonacci number is 1
generate_fib(N, T) :-
    N > 1,               % N must be greater than 1 for recursion
    N1 is N - 1,         % Decrement N by 1
    N2 is N - 2,         % Decrement N by 2
    generate_fib(N1, T1),% Recursively get the (N-1)th Fibonacci number
    generate_fib(N2, T2),% Recursively get the (N-2)th Fibonacci number
    T is T1 + T2.        % The Nth term is the sum of the previous two terms
