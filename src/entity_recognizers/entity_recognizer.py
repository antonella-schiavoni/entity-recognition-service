from abc import ABC, abstractmethod
from typing import List

from src.entity import Entity


class EntityRecognizer(ABC):
    @abstractmethod
    def extract_entities(self, title: List[str]) -> List[Entity]:
        pass
