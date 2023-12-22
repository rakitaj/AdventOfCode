import os
from pathlib import Path
from abc import ABC, abstractmethod


class DataLoader:
    def __init__(self, year: int, filename: str):
        self.filename = filename
        self.filepath = Path(self._get_current_dir(), "../../data", str(year), filename)

    def _get_current_dir(self) -> Path:
        path = Path(os.path.dirname(os.path.realpath(__file__)))
        return path

    def readlines_str(self, trim_newlines: bool = False) -> list[str]:
        with open(self.filepath, "r") as fp:
            lines = fp.readlines()
            if trim_newlines:
                lines = [line.strip() for line in lines]
            return lines

    def read(self) -> str:
        with open(self.filepath, "r") as fp:
            return fp.read()


class Answers(ABC):
    @abstractmethod
    def part1(self) -> str:
        pass

    @abstractmethod
    def part2(self) -> str:
        pass
