# -*- coding: utf-8 -*-
"""
Symbol implementation for the Turing machine.

@author: Eric Santos <ericshantos13@gmail.com>
"""


class Symbol:

    _instances: dict[str, "Symbol"] = {}

    def __new__(cls, value: str):

      if value not in cls._instances:

        instance = super().__new__(cls)
        instance.value = value

        cls._instances[value] = instance

      return cls._instances[value]

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"Symbol({self.value})"

    def __hash__(self) -> int:
        return hash(self.value)

    def __eq__(self, other) -> bool:
        return isinstance(other, Symbol) and self.value == other.value
    