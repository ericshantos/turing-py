from tmpy.dsl import MachineNode, TransitionNode


def test_machine_node_creation():

    machine = MachineNode("exemple")

    assert machine.name == "exemple"
    assert machine.start is None
    assert machine.accept is None
    assert machine.blank is None
    assert machine.transitions == []


def test_machine_node_properties():

    machine = MachineNode("tm")

    machine.start = "q0"
    machine.accept = "qf"
    machine.blank = "_"

    assert machine.start == "q0"
    assert machine.accept == "qf"
    assert machine.blank == "_"


def test_transition_node_creation():

    transition = TransitionNode("q0", "1", "q1", "0", "R")

    assert transition.state == "q0"
    assert transition.read == "1"
    assert transition.next_state == "q1"
    assert transition.write == "0"
    assert transition.move == "R"


def test_add_transition_to_machine():

    machine = MachineNode("tm")

    transition = TransitionNode("q0", "1", "q1", "0", "R")

    machine.transitions.append(transition)

    assert len(machine.transitions) == 1
    assert machine.transitions[0].state == "q0"


def test_machine_with_transition():

    machine = MachineNode("tm")
    machine.start = "q0"
    machine.accept = "qf"
    machine.blank = "_"

    transition = TransitionNode("q0", "1", "q1", "0", "R")

    machine.transitions.append(transition)

    assert machine.name == "tm"
    assert machine.start == "q0"
    assert machine.accept == "qf"

    assert machine.transitions[0].next_state == "q1"
