class TuringMachineError(Exception):
    """Base class for exceptions in this module."""

    pass


class AlphabetError(TuringMachineError):
    """Exception raised for errors in the input alphabet."""

    pass


class EmptyAlphabetError(AlphabetError):
    """Exception raised for errors in the empty alphabet."""

    pass


class BlankSymbolError(AlphabetError):
    """Exception raised for errors related to the blank symbol."""

    pass


class DuplicateSymbolError(AlphabetError):
    """Exception raised for duplicate symbols in the alphabet."""

    pass


class StateError(TuringMachineError):
    """Exception raised for errors in the states of the Turing machine."""

    pass


class InvalidInitialStateError(StateError):
    """Exception raised for invalid states."""

    pass


class InvalidFinalStateError(StateError):
    """Exception raised for invalid final states."""

    pass


class TapeError(TuringMachineError):
    """Exception raised for errors related to the tape."""

    pass


class TapeOutOfBoundsError(TapeError):
    """Exception raised when the tape head moves out of bounds."""

    pass


class InvalidSymbolError(AlphabetError):
    """Exception raised for invalid symbols on the tape."""

    pass


class TransitionError(TuringMachineError):
    """Exception raised for errors in the transition function."""

    pass


class TransitionNotDefinedError(TransitionError):
    """Exception raised when a transition is not defined for a given state and symbol."""

    pass


class MaxStepsExceededError(TuringMachineError):
    """Exception raised when the maximum number of steps is exceeded."""

    pass
