import pytest

from tmpy import InvalidSymbolError, TapeOutOfBoundsError
from tmpy.alphabet import Alphabet, Symbol
from tmpy.machine import Tape


@pytest.fixture
def alphabet():
    return Alphabet(Symbol("0"), Symbol("1"), Symbol("_"))


@pytest.fixture
def blank():
    return Symbol("_")


@pytest.fixture
def tape(alphabet, blank):
    return Tape("01", alphabet, blank)


def test_tape_initialization(tape):
    assert str(tape) == "01"
    assert len(tape) == 2


def test_getitem_valid_index(tape):
    assert tape[0] == Symbol("0")
    assert tape[1] == Symbol("1")


def test_getitem_expand_tape(tape):
    symbol = tape[5]
    assert symbol == Symbol("_")
    assert len(tape) == 6


def test_getitem_negative_index(tape):
    with pytest.raises(TapeOutOfBoundsError):
        tape[-1]


def test_setitem_valid_symbol(tape):
    tape[0] = Symbol("1")
    assert tape[0] == Symbol("1")


def test_setitem_invalid_symbol(tape):
    with pytest.raises(InvalidSymbolError):
        tape[0] = "X"


def test_setitem_expand_tape(tape):
    tape[4] = Symbol("1")
    assert tape[4] == Symbol("1")
    assert len(tape) == 5


def test_iter(tape):
    symbols = list(tape)
    assert symbols == [Symbol("0"), Symbol("1")]


def test_repr(tape):
    assert "Tape" in repr(tape)
