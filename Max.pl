# Write a Prolog program to implement max(X, Y, M) so that M is the maximum of two numbers X and Y

% --------------------------------------------
% max(X, Y, M) :-
%     M is the maximum of the two numbers X and Y.
% --------------------------------------------

max(X, Y, X) :- X >= Y.
max(X, Y, Y) :- Y > X.
