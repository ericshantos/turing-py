"""
@author: Eric Santos <ericshantos13@gmail.com>

Turing Machine implementation.
"""


from ..alphabet import Alphabet, TapeAlphabet, Symbol
from .tape import Tape
from ..transition import TransitionFunction


class TuringMachine:
    def __init__(
        self,
        states: str,
        alphabet: Alphabet,
        tape_alphabet: TapeAlphabet,
        delta: TransitionFunction,
        blank: Symbol
    ):
        self.states = states
        self.alphabet = alphabet
        self.tape_alphabet = tape_alphabet
        self.delta = delta
        self.blank = blank

        self.head: int = 0

    def run(
      self,
      input: str,
      debug: bool = False,
      max_steps: int = 10000
    ) -> None:

        steps = 0

        self.states.current_state = self.states.initial_state
        self._load_tape(input)

        while self.states.current_state not in self.states.final_states:

          if steps > max_steps:
            raise RuntimeError("Max steps exceeded")

          steps += 1

          if debug:
            print(self)

          if not self._step():
            break

        if debug:
          print(self)

    def _load_tape(self, input: str) -> None:
        alphabet = self.alphabet | self.tape_alphabet
        self.tape = Tape(input, alphabet, self.blank)
        self.head = 0

    def _step(self) -> bool:
        symbol = self.tape[self.head]

        t = self.delta(self.states.current_state, symbol)

        if t is None:
            return False

        self.tape[self.head] = t.new_symbol
        self.states.current_state = t.new_state

        self.head = t.direction.move(self.head)

        return True

    def __str__(self) -> str:

      tape_str = "".join(str(s) for s in self.tape)

      head_indicator = " " * self.head + "^"

      return f"""
        State : {self.states.current_state}
        Head  : {self.head}
        Tape  : {tape_str}
                {head_indicator}
      """

    @property
    def result(self) -> str:

        tape = "".join(str(s) for s in self.tape)

        return tape.rstrip(str(self.blank))
    