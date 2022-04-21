from enum import Enum


class SignalType(Enum):
    GARAGE = 1
    GATE = 2

    @staticmethod
    def from_str(str_input) -> Enum:
        if "GARAGE" in str_input:
            return SignalType.GARAGE
        if "GATE" in str_input:
            return SignalType.GATE

    def to_str(self) -> str:
        if self.GARAGE:
            return "GARAGE"
        if self.GATE:
            return "GATE"