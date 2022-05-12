from enum import Enum


class SignalType(Enum):
    GARAGE = 1
    GATE = 2
    BOTH = 3

    @staticmethod
    def from_str(str_input) -> Enum:
        if "GARAGE" in str_input:
            return SignalType.GARAGE
        if "GATE" in str_input:
            return SignalType.GATE
        if "BOTH" in str_input:
            return SignalType.BOTH

    def to_str(self) -> str:
        result = "ERROR"

        if SignalType.GARAGE == self:
            result = "GARAGE"
        if SignalType.GATE == self:
            result = "GATE"
        if SignalType.BOTH == self:
            result = "BOTH"

        return result
