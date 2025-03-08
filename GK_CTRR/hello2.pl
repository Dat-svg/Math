:- initialization(main).

main :-
    writeln("Enter your name: "),
    read_line_to_string(user_input, Name),
    format("Hello ~s", [Name]).
