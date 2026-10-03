from abc import ABC, abstractmethod
from typing import Any


class HealCapability(ABC):
    def __init__(self, target: Any) -> None:
        self.target = target

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
