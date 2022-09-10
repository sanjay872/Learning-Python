from enum import Enum

class State(Enum):
    ACTIVE = 1
    INACTIVE = 0

print(State.ACTIVE.name)