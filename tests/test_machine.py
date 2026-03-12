import pytest

from tmpy import (
    Alphabet,
    Direction,
    MaxStepsExceededError,
    States,
    Symbol,
    TapeAlphabet,
    Transition,
    TransitionFunction,
    TuringMachine,
)


@pytest.fixture
def states():
    return States("q0", "qf", initial_state="q0", final_states={"qf"})


@pytest.fixture
def alphabets():
    return (
        Alphabet(Symbol("0"), Symbol("1")),
        TapeAlphabet(Symbol("B"), Symbol("0"), Symbol("1"), Symbol("x"), Symbol("B")),
    )


@pytest.fixture
def delta():
    return TransitionFunction()


@pytest.fixture
def transition():
    return [
        Transition("q0", Symbol("0"), "q0", Symbol("x"), Direction.RIGHT),
        Transition("q0", Symbol("1"), "q0", Symbol("x"), Direction.RIGHT),
        Transition("q0", Symbol("B"), "qf", Symbol("B"), Direction.STAY),
    ]


@pytest.fixture
def tm(states, alphabets, delta, transition):

    alphabet, tape_alphabet = alphabets

    delta.add(*transition)

    return TuringMachine(
        states=states,
        alphabet=alphabet,
        tape_alphabet=tape_alphabet,
        delta=delta,
        blank=Symbol("B"),
    )


def test_tm_run(tm):
    tm.run("000")

    assert tm.result == "xxx"


def test_tm_run_empty(tm):
    tm.run("")

    assert tm.result == ""


def test_tm_run_mixed(tm):
    tm.run("0101")

    assert tm.result == "xxxx"


def test_tm_run_exceed_max_steps(tm):
    with pytest.raises(MaxStepsExceededError):
        tm.run("0" * 100, max_steps=10)


def test_tm_run_debug(tm):
    tm.run("000", debug=True)

    assert tm.result == "xxx"


def test_tm_run_final_state(tm):
    tm.run("000")

    assert tm.states.current_state == "qf"


def test_tm_run_blank(tm):
    tm.run("000")

    assert tm.tape[3] == Symbol("B")


def test_tm_run_head_position(tm):
    tm.run("000")

    assert tm.head == 3


def test_tm_str(tm):

    tm.run("000")

    expected = str(tm)

    assert "State" in expected
    assert "Tape" in expected
    assert "Head" in expected
