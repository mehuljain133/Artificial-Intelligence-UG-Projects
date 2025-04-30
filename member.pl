# Write a Prolog program to implement memb(X, L): to check whether X is a member of L or not.

% --------------------------------------------
% memb(X, L) :-
%     Succeeds if X is a member of list L.
% --------------------------------------------

memb(X, [X|_]).          % Base case: X is the head of the list
memb(X, [_|Tail]) :-     % Recursive case: Check the tail of the list
    memb(X, Tail).
