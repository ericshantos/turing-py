from tmpy.dsl import Lexer, TokenType


def test_machine_keyword():

    text = "machine my_tm"

    lexer = Lexer(text)
    tokens = lexer.tokenize()

    assert tokens[0].type == TokenType.MACHINE
    assert tokens[0].value == "machine"

    assert tokens[1].type == TokenType.IDENTIFIER
    assert tokens[1].value == "my_tm"


def test_ignore_comments():

    text = """
    # this is a comment
    machine tm1
    """

    lexer = Lexer(text)
    tokens = lexer.tokenize()

    assert tokens[0].type == TokenType.MACHINE
    assert tokens[1].type == TokenType.IDENTIFIER


def test_move_tokens():

    text = "L R S"

    lexer = Lexer(text)
    tokens = lexer.tokenize()

    assert tokens[0].type == TokenType.MOVE
    assert tokens[0].type == TokenType.MOVE
    assert tokens[1].type == TokenType.MOVE


def test_arrow_token():

    text = "q0 a -> q1 b R"

    lexer = Lexer(text)
    tokens = lexer.tokenize()

    assert tokens[2].type == TokenType.ARROW
    assert tokens[2].value == "->"


def test_eof_token():

    text = "machine tm"

    lexer = Lexer(text)
    tokens = lexer.tokenize()

    assert tokens[-1].type == TokenType.EOF
    assert tokens[-1].value is None


def test_full_machine():

    text = """
    machine exemple
    start q0
    accept qf
    blank _

    Q0 1 -> q1 0 R
    """

    lexer = Lexer(text)
    tokens = lexer.tokenize()

    types = set(t.type for t in tokens)

    assert TokenType.MACHINE in types
    assert TokenType.START in types
    assert TokenType.ACCEPT in types
    assert TokenType.BLANK in types
    assert TokenType.ARROW in types
    assert TokenType.IDENTIFIER in types
    assert TokenType.MOVE in types
    assert TokenType.EOF in types
