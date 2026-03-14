from tmpy.dsl import Token, TokenType


def test_token_creation():

    token = Token(TokenType.MACHINE, "machine")

    assert token.type == TokenType.MACHINE
    assert token.value == "machine"


def test_token_equality():

    token1 = Token(TokenType.START, "start")
    token2 = Token(TokenType.START, "start")
    token3 = Token(TokenType.ACCEPT, "accept")

    assert token1.type == token2.type
    assert token1.value == token2.value
    assert token1.type != token3.type
    assert token1.value != token3.value


def test_token_repr():

    token = Token(TokenType.MACHINE, "machine")

    assert repr(token) == "Token(MACHINE, machine)"


def test_token_eof():

    token = Token(TokenType.EOF, None)

    assert token.type == TokenType.EOF
    assert token.value is None


def test_token_move():

    token = Token(TokenType.MOVE, "R")

    assert token.type == TokenType.MOVE
    assert token.value == "R"


def test_token_identifier():

    token = Token(TokenType.IDENTIFIER, "q0")

    assert token.type == TokenType.IDENTIFIER
    assert token.value == "q0"


def test_token_blank():

    token = Token(TokenType.BLANK, "blank")

    assert token.type == TokenType.BLANK
    assert token.value == "blank"


def test_token_arrow():

    token = Token(TokenType.ARROW, "->")

    assert token.type == TokenType.ARROW
    assert token.value == "->"


def test_token_accept():

    token = Token(TokenType.ACCEPT, "accept")

    assert token.type == TokenType.ACCEPT
    assert token.value == "accept"


def test_token_start():

    token = Token(TokenType.START, "start")

    assert token.type == TokenType.START
    assert token.value == "start"


def test_token_machine():

    token = Token(TokenType.MACHINE, "machine")

    assert token.type == TokenType.MACHINE
    assert token.value == "machine"


def test_token_move_L():

    token = Token(TokenType.MOVE, "L")

    assert token.type == TokenType.MOVE
    assert token.value == "L"


def test_token_move_S():

    token = Token(TokenType.MOVE, "S")

    assert token.type == TokenType.MOVE
    assert token.value == "S"


def test_token_move_R():

    token = Token(TokenType.MOVE, "R")

    assert token.type == TokenType.MOVE
    assert token.value == "R"


def test_token_identifier_q1():

    token = Token(TokenType.IDENTIFIER, "q1")

    assert token.type == TokenType.IDENTIFIER
    assert token.value == "q1"


def test_token_identifier_a():

    token = Token(TokenType.IDENTIFIER, "a")

    assert token.type == TokenType.IDENTIFIER
    assert token.value == "a"


def test_token_identifier_b():

    token = Token(TokenType.IDENTIFIER, "b")

    assert token.type == TokenType.IDENTIFIER
    assert token.value == "b"


def test_token_identifier_q2():

    token = Token(TokenType.IDENTIFIER, "q2")

    assert token.type == TokenType.IDENTIFIER
    assert token.value == "q2"
