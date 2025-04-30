% 1. Sum of Two Numbers
% Question: Write a Prolog program to calculate the sum of two numbers X and Y and store the result in Z.
sum(X, Y, Z) :- Z is X + Y.

% 2. Maximum of Two Numbers
% Question: Write a Prolog program to implement max(X, Y, M) where M is the maximum of two numbers X and Y.
max(X, Y, M) :-
    (X > Y -> M = X; M = Y).

% 3. Factorial of a Number
% Question: Write a Prolog program to implement factorial(N, F) where F represents the factorial of a number N.
factorial(0, 1).
factorial(N, F) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, F1),
    F is N * F1.

% 4. Nth Term of the Fibonacci Series
% Question: Write a Prolog program to implement generate_fib(N, T) where T represents the Nth term of the Fibonacci series.
generate_fib(0, 0).
generate_fib(1, 1).
generate_fib(N, T) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    generate_fib(N1, T1),
    generate_fib(N2, T2),
    T is T1 + T2.

% 5. GCD of Two Numbers (Euclidean Algorithm)
% Question: Write a Prolog program to implement GCD(A, B, GCD) where GCD is the greatest common divisor of two numbers A and B.
gcd(A, 0, A).
gcd(0, B, B).
gcd(A, B, GCD) :-
    A > B,
    A1 is A - B,
    gcd(A1, B, GCD).
gcd(A, B, GCD) :-
    B > A,
    B1 is B - A,
    gcd(A, B1, GCD).

% 6. Power of a Number
% Question: Write a Prolog program to implement power(Num, Pow, Ans) where Num is raised to the power Pow to get Ans.
power(_, 0, 1).
power(Num, Pow, Ans) :-
    Pow > 0,
    Pow1 is Pow - 1,
    power(Num, Pow1, Ans1),
    Ans is Num * Ans1.

% 7. Multiplication of Two Numbers
% Question: Write a Prolog program to implement multi(N1, N2, R) where N1 and N2 denote the numbers to be multiplied and R represents the result.
multi(0, _, 0).
multi(_, 0, 0).
multi(N1, N2, R) :-
    N2 > 0,
    N2_1 is N2 - 1,
    multi(N1, N2_1, R1),
    R is R1 + N1.
multi(N1, N2, R) :-
    N2 < 0,
    N2_1 is N2 + 1,
    multi(N1, N2_1, R1),
    R is R1 - N1.

% 8. Member Check
% Question: Write a Prolog program to implement memb(X, L) to check whether X is a member of list L.
memb(X, [X|_]).
memb(X, [_|Tail]) :-
    memb(X, Tail).

% 9. Concatenate Two Lists
% Question: Write a Prolog program to implement conc(L1, L2, L3) where L1 is the first list and L2 is the second list to be concatenated to get the list L3.
conc([], L, L).
conc([H|T], L, [H|R]) :-
    conc(T, L, R).

% 10. Reverse a List
% Question: Write a Prolog program to implement reverse(L, R) where L is the original list and R is the reversed list.
reverse([], []).
reverse([H|T], R) :-
    reverse(T, R1),
    conc(R1, [H], R).

% 11. Check if a List is a Palindrome
% Question: Write a Prolog program to implement palindrome(L) which checks whether a list L is a palindrome or not.
palindrome(L) :-
    reverse(L, L).

% 12. Sum of a List
% Question: Write a Prolog program to implement sumlist(L, S) where S is the sum of the elements in list L.
sumlist([], 0).
sumlist([H|T], S) :-
    sumlist(T, S1),
    S is H + S1.

% 13. Even-Length and Odd-Length Lists
% Question: Write a Prolog program to implement two predicates evenlength(List) and oddlength(List) to check if the list has even or odd length respectively.
evenlength([]).
evenlength([_,_|T]) :-
    evenlength(T).

oddlength([_]).
oddlength([_,_|T]) :-
    oddlength(T).

% 14. Nth Element of a List
% Question: Write a Prolog program to implement nth_element(N, L, X) where N is the desired position, L is a list, and X is the Nth element of L.
nth_element(1, [X|_], X).
nth_element(N, [_|T], X) :-
    N > 1,
    N1 is N - 1,
    nth_element(N1, T, X).

% 15. Maximum in a List
% Question: Write a Prolog program to implement maxlist(L, M) where M is the maximum number in the list L.
maxlist([X], X).
maxlist([H|T], M) :-
    maxlist(T, M1),
    (H > M1 -> M = H; M = M1).

% 16. Insert Element at Nth Position
% Question: Write a Prolog program to implement insert_nth(I, N, L, R) that inserts an item I into the Nth position of list L to generate list R.
insert_nth(1, I, L, [I|L]).
insert_nth(N, I, [H|T], [H|R]) :-
    N > 1,
    N1 is N - 1,
    insert_nth(N1, I, T, R).

% 17. Delete Element from Nth Position
% Question: Write a Prolog program to implement delete_nth(N, L, R) that removes the element at the Nth position from list L to generate list R.
delete_nth(1, [_|T], T).
delete_nth(N, [H|T], [H|R]) :-
    N > 1,
    N1 is N - 1,
    delete_nth(N1, T, R).

% 18. Merge Two Ordered Lists
% Question: Write a Prolog program to implement merge(L1, L2, L3) where L1 is the first ordered list, L2 is the second ordered list, and L3 is the merged list.
merge([], L, L).
merge(L, [], L).
merge([H1|T1], [H2|T2], [H1|T3]) :-
    H1 =< H2,
    merge(T1, [H2|T2], T3).
merge([H1|T1], [H2|T2], [H2|T3]) :-
    H1 > H2,
    merge([H1|T1], T2, T3).

% 19. List Length
% Question: Write a Prolog program to calculate the length of a list.
length_list([], 0).
length_list([_|T], L) :-
    length_list(T, L1),
    L is L1 + 1.

% 20. Check if a List is Empty
% Question: Write a Prolog program to check if a list is empty.
empty_list([]).

% 21. Find Element by Index
% Question: Write a Prolog program to find the element in a list by its index.
find_element(Index, List, Element) :-
    nth_element(Index, List, Element).

% 22. Sum of Squares of List Elements
% Question: Write a Prolog program to calculate the sum of squares of elements in a list.
sum_of_squares([], 0).
sum_of_squares([H|T], S) :-
    sum_of_squares(T, S1),
    S is S1 + H*H.

% 23. Remove Duplicates from List
% Question: Write a Prolog program to remove duplicates from a list.
remove_duplicates([], []).
remove_duplicates([H|T], [H|R]) :-
    \+ memb(H, T),
    remove_duplicates(T, R).
remove_duplicates([H|T], R) :-
    memb(H, T),
    remove_duplicates(T, R).

% 24. Flatten a Nested List
% Question: Write a Prolog program to flatten a nested list into a single list.
flatten([], []).
flatten([H|T], R) :-
    flatten(H, R1),
    flatten(T, R2),
    append(R1, R2, R).
flatten(H, [H]) :- atomic(H).
