from enum import Enum


class CustomEnumAuto(Enum):
    """
    Redefines method auto() of Enum class to use params as values, e.g.:
    usage:    param = auto()
    outcome:  param = 'param'
    """
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):

        return name
