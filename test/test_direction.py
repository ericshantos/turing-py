from tmpy.transition import Direction


def test_direction_enum():
    assert Direction.LEFT.value == -1
    assert Direction.RIGHT.value == 1

def test_direction_move():
    head = 0
    new_head = Direction.RIGHT.move(head)
    assert new_head == 1

    head = 1
    new_head = Direction.LEFT.move(head)
    assert new_head == 0

def test_direction_str():
    assert str(Direction.LEFT) == "LEFT"
    assert str(Direction.RIGHT) == "RIGHT"