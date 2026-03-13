from tmpy import Parser, Token, TokenType


def test_parse_machine():

    tokens = [Token(TokenType.MACHINE, "machine"), Token(TokenType.IDENTIFIER, "tm"), Token(TokenType.EOF, None)]

    parser = Parser(tokens)
    machine = parser.parse()

    assert machine.name == "tm"


def test_parse_start_state():

    tokens = [
        Token(TokenType.MACHINE, "machine"),
        Token(TokenType.IDENTIFIER, "tm"),
        Token(TokenType.START, "start"),
        Token(TokenType.IDENTIFIER, "q0"),
        Token(TokenType.EOF, None),
    ]

    parser = Parser(tokens)
    machine = parser.parse()

    assert machine.start == "q0"


def test_parse_accept_state():

    tokens = [
        Token(TokenType.MACHINE, "machine"),
        Token(TokenType.IDENTIFIER, "tm"),
        Token(TokenType.ACCEPT, "accept"),
        Token(TokenType.IDENTIFIER, "qf"),
        Token(TokenType.EOF, None),
    ]

    parser = Parser(tokens)
    machine = parser.parse()

    assert machine.accept == "qf"


def test_parse_blank():

    tokens = [
        Token(TokenType.MACHINE, "machine"),
        Token(TokenType.IDENTIFIER, "tm"),
        Token(TokenType.BLANK, "blank"),
        Token(TokenType.IDENTIFIER, "_"),
        Token(TokenType.EOF, None),
    ]

    parser = Parser(tokens)
    machine = parser.parse()

    assert machine.blank == "_"


def test_parse_transition():

    tokens = [
        Token(TokenType.MACHINE, "machine"),
        Token(TokenType.IDENTIFIER, "tm"),
        Token(TokenType.IDENTIFIER, "q0"),
        Token(TokenType.IDENTIFIER, "1"),
        Token(TokenType.ARROW, "->"),
        Token(TokenType.IDENTIFIER, "q1"),
        Token(TokenType.IDENTIFIER, "0"),
        Token(TokenType.MOVE, "R"),
        Token(TokenType.EOF, None),
    ]

    parser = Parser(tokens)
    machine = parser.parse()

    transition = machine.transitions[0]

    assert transition.state == "q0"
    assert transition.read == "1"
    assert transition.next_state == "q1"
    assert transition.write == "0"
    assert transition.move == "R"


def test_full_machine():

    tokens = [
        Token(TokenType.MACHINE, "machine"),
        Token(TokenType.IDENTIFIER, "exemple"),
        Token(TokenType.START, "start"),
        Token(TokenType.IDENTIFIER, "q0"),
        Token(TokenType.ACCEPT, "accept"),
        Token(TokenType.IDENTIFIER, "qf"),
        Token(TokenType.BLANK, "blank"),
        Token(TokenType.IDENTIFIER, "_"),
        Token(TokenType.IDENTIFIER, "q0"),
        Token(TokenType.IDENTIFIER, "1"),
        Token(TokenType.ARROW, "->"),
        Token(TokenType.IDENTIFIER, "q1"),
        Token(TokenType.IDENTIFIER, "0"),
        Token(TokenType.MOVE, "R"),
        Token(TokenType.EOF, None),
    ]

    parser = Parser(tokens)
    machine = parser.parse()

    assert machine.name == "exemple"
    assert machine.start == "q0"
    assert machine.accept == "qf"
    assert machine.blank == "_"
    assert len(machine.transitions) == 1
