from abc import abstractclassmethod
from typing import Any
from .Game import Game


class PerfectInfomationGame(Game):
    @abstractclassmethod
    def set_game_state(self, state: Any) -> None:
        pass

    @abstractclassmethod
    def get_game_state(self) -> Any:
        pass
