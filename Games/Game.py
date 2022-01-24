from abc import ABC, abstractclassmethod
from typing import Any, Tuple


@abstractclassmethod
class Game(ABC):
    @abstractclassmethod
    def step(self, action: Any) -> Tuple(Any, float, bool):
        pass
