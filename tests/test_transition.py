from dataclasses import FrozenInstanceError

import pytest

from tmpy.alphabet import Symbol
from tmpy.transition import Direction, Transition


@pytest.fixture
def t():
    return Transition(
        state="q0",
        symbol=Symbol("0"),
        new_state="q1",
        new_symbol=Symbol("1"),
        direction=Direction.RIGHT,
    )


def test_transition_creation(t):

    assert t.state == "q0"
    assert t.symbol == Symbol("0")
    assert t.new_state == "q1"
    assert t.new_symbol == Symbol("1")
    assert t.direction == Direction.RIGHT


def test_transition_is_immutable(t):

    with pytest.raises(FrozenInstanceError):
        t.state = "q2"


def test_transition_str(t):

    result = str(t)

    assert "q0" in result
    assert "q1" in result


def test_transition_str_exact(t):

    assert t.state == "q0"
    assert t.symbol == Symbol("0")
    assert t.new_state == "q1"
    assert t.new_symbol == Symbol("1")
    assert t.direction == Direction.RIGHT
    assert str(t) == "δ(q0, 0) → (q1, 1, RIGHT)"


def test_transition_equality():

    t1 = Transition("q0", Symbol("0"), "q1", Symbol("1"), Direction.RIGHT)
    t2 = Transition("q0", Symbol("0"), "q1", Symbol("1"), Direction.RIGHT)

    assert t1 == t2
