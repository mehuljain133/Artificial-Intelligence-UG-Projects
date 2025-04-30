% Prolog Programming: Introduction to Programming in Logic (PROLOG), Lists, Operators,basic Input and Output.

% --- Introduction to PROLOG (Facts and Rules) ---
% Knowledge base
parent(john, mary).
parent(john, tom).
parent(mary, alice).
parent(tom, bob).

male(john).
male(tom).
male(bob).
female(mary).
female(alice).

% Rule: X is grandparent of Y
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Rule: X is sibling of Y
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% --- Lists in PROLOG ---
% Sum elements of a list
sum_list([], 0).
sum_list([H|T], Sum) :- sum_list(T, Rest), Sum is H + Rest.

% Check if an element exists in a list
member_of_list(X, [X|_]).
member_of_list(X, [_|T]) :- member_of_list(X, T).

% Append two lists
append_list([], L, L).
append_list([H|T], L2, [H|R]) :- append_list(T, L2, R).

% --- Operators ---
% Define custom infix operator for "likes"
:- op(500, xfx, likes).

john likes pizza.
alice likes sushi.

% Rule using custom operator
likes_food(X) :- X likes _.

% --- Basic Input/Output ---
% Print a message
say_hello :- write('Hello from Prolog!'), nl.

% Read input and print it back
echo_input :-
    write('Enter something: '),
    read(Input),
    write('You entered: '), write(Input), nl.

% --- Sample query usage ---
% Run this to test:
% ?- grandparent(john, X).
% ?- sum_list([1,2,3,4], X).
% ?- append_list([1,2], [3,4], X).
% ?- john likes What.
% ?- echo_input.
