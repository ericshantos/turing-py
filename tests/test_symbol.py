from tmpy import Symbol


def test_setup_symbol():

    Symbol._instances.clear()


def test_symbol_same_instance():

    s1 = Symbol("a")
    s2 = Symbol("a")

    assert s1 is s2


def test_symbol_different_instances():

    s1 = Symbol("a")
    s2 = Symbol("b")

    assert s1 is not s2


def test_symbol_str():

    s = Symbol("x")

    assert str(s) == "x"


def test_symbol_repr():

    s = Symbol("x")

    assert repr(s) == "Symbol(x)"


def test_symbol_equality():

    s1 = Symbol("a")
    s2 = Symbol("a")
    s3 = Symbol("b")

    assert s1 == s2
    assert s1 != s3


def test_symbol_hash():

    s1 = Symbol("a")

    assert hash(s1) == hash("a")


def test_symbol_dict_usage():

    s1 = Symbol("a")
    s2 = Symbol("a")

    d = {s1: "test"}

    assert d[s2] == "test"
