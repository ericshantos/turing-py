import pytest
from tmpy import Symbol, Alphabet, TapeAlphabet


def setup_function():
    Symbol._instances.clear()

def test_alphabet_cannot_be_empty():
    with pytest.raises(ValueError):
        Alphabet()

def test_alphabet_cannot_have_duplicates():
    a = Symbol("a")
    b = Symbol("b")

    with pytest.raises(ValueError):
        Alphabet(a, b, a)

def test_symbol_membership():
    a = Symbol("a")
    b = Symbol("b")

    alphabet = Alphabet(a, b)

    assert a in alphabet
    assert b in alphabet

    assert Symbol("c") not in alphabet

def test_alphabet_interation():
    a = Symbol("a")
    b = Symbol("b")

    alphabet = Alphabet(a, b)

    symbols = list(alphabet)

    assert len(symbols) == 2
    assert a in symbols
    assert b in symbols

def test_alphabet_union():
    a = Symbol("a")
    b = Symbol("b")
    c = Symbol("c")

    alphabet1 = Alphabet(a, b)
    alphabet2 = Alphabet(b, c)

    union_alphabet = alphabet1 | alphabet2

    assert a in union_alphabet
    assert b in union_alphabet
    assert c in union_alphabet

def test_union_with_invalid_type():
    a = Symbol("a")
    alphabet = Alphabet(a)

    with pytest.raises(TypeError):
        alphabet | "not an alphabet"

def test_alphabet_str():
    a = Symbol("a")
    b = Symbol("b")

    alphabet = Alphabet(a, b)

    assert "Σ" in str(alphabet)
    assert "a" in str(alphabet)
    assert "b" in str(alphabet)

def test_tape_alphabet():
    a = Symbol("a")
    b = Symbol("b")
    blank = Symbol("_")

    tape_alphabet = TapeAlphabet(blank, a, b, blank)

    assert a in tape_alphabet
    assert b in tape_alphabet
    assert blank in tape_alphabet

def test_tape_alphabet_str():
    a = Symbol("a")
    b = Symbol("b")
    blank = Symbol("_")

    tape_alphabet = TapeAlphabet(blank, a, b, blank)

    assert "Γ" in str(tape_alphabet)
    assert "a" in str(tape_alphabet)
    assert "b" in str(tape_alphabet)
    assert "_" in str(tape_alphabet)
    