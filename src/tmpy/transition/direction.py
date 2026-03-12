# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>

Module for the direction of the transition.
"""

from enum import Enum


class Direction(Enum):
    RIGHT = 1
    LEFT = -1
    STAY = 0

    def move(self, head: int) -> int:
        return head + self.value

    def __str__(self) -> str:
        return self.name
