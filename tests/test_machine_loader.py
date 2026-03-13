import tempfile

from tmpy import MachineLoader, Symbol, TransitionFunction


def test_machine_loader_integration():

    machine_code = """
    machine tm
    start q0
    accept qf
    blank _

    q0 1 -> q1 0 R
    """

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write(machine_code)
        f.flush()

        loader = MachineLoader()
        transitions = loader.load(f.name)

    delta = TransitionFunction(transitions)

    result = delta("q0", Symbol("1"))

    assert result is not None
    assert result.new_state == "q1"
    assert result.state == "q0"
