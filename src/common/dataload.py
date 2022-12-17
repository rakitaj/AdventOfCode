import os
from pathlib import Path


class DataLoader:
    def __init__(self, year: int, filename: str):
        self.filename = filename
        self.filepath = Path(self._get_current_dir(), "../../data", f"aoc{year}", filename)

    def _get_current_dir(self) -> Path:
        path = Path(os.path.dirname(os.path.realpath(__file__)))
        return path

    def readlines_str(self) -> list[str]:
        with open(self.filepath, "r") as fp:
            return fp.readlines()
