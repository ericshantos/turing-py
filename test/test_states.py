import pytest
from tmpy import States


@pytest.fixture
def states():
    return States(
        "q0", "q1", "q2",
        initial_state="q0",
        final_states={"q2"}
    )


def test_states_creation(states):
    assert states.initial_state == "q0"
    assert states.current_state == "q0"
    assert states.final_states == {"q2"}


def test_states_length(states):
    assert len(states) == 3


def test_states_contains(states):
    assert "q0" in states
    assert "q1" in states
    assert "q3" not in states


def test_states_iteration(states):
    collected = set()
    for s in states:
        collected.add(s)

    assert collected == {"q0", "q1", "q2"}


def test_invalid_initial_state():
    with pytest.raises(ValueError):
        States(
            "q0", "q1",
            initial_state="q2",
            final_states={"q1"}
        )


def test_invalid_final_states():
    with pytest.raises(ValueError):
        States(
            "q0", "q1",
            initial_state="q0",
            final_states={"q2"}
        )


def test_str(states):
    text = str(states)
    assert "Q =" in text