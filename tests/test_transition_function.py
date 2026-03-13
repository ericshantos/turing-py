import pytest

from tmpy import Direction, Symbol, Transition, TransitionFunction


@pytest.fixture
def t():
    return Transition(
        state="q0",
        symbol=Symbol("0"),
        new_state="q1",
        new_symbol=Symbol("1"),
        direction=Direction.RIGHT,
    )


def test_add_and_get_transition(t):

    tf = TransitionFunction(t)

    result = tf("q0", Symbol("0"))

    assert result == t


def test_transition_not_found():

    tf = TransitionFunction()

    result = tf("q0", Symbol("1"))

    assert result is None


def test_add_multiple_transitions():

    t1 = Transition("q0", Symbol("0"), "q1", Symbol("1"), Direction.RIGHT)
    t2 = Transition("q1", Symbol("1"), "q2", Symbol("0"), Direction.LEFT)

    tf = TransitionFunction(t1, t2)

    assert tf("q0", Symbol("0")) == t1
    assert tf("q1", Symbol("1")) == t2


def test_add_iterable():

    t1 = Transition("q0", Symbol("0"), "q1", Symbol("1"), Direction.RIGHT)
    t2 = Transition("q1", Symbol("1"), "q2", Symbol("0"), Direction.LEFT)

    tf = TransitionFunction([t1, t2])

    assert tf("q0", Symbol("0")) == t1
    assert tf("q1", Symbol("1")) == t2


def test_str_output(t):

    tf = TransitionFunction(t)

    result = str(tf)

    assert str(t) in result


def test_contains_(t):

    tf = TransitionFunction(t)

    assert ("q0", Symbol("0")) in tf
