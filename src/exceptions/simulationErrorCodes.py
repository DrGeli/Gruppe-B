from enum import Enum
from dataclasses import dataclass, field

class ErrorCodeDataMixin:
    errorcode: int
    message: str

class SimulationErrorCodes(ErrorCodeDataMixin, Enum):
    ExampleError = 1, "Example ErrorCode"

if __name__ == "__main__":
    example = SimulationErrorCodes.ExampleError
    print(example.value)