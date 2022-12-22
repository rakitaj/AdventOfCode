from src.common.dataload import DataLoader


class ElfPacket:
    def __init__(self, packet: str):
        self.packet = packet

    def start_index(self, num_look_ahead: int) -> int | None:
        for i in range(len(self.packet)):
            s: set[str] = set()
            for ii in range(i, i + num_look_ahead):
                s.add(self.packet[ii])
                if len(s) == num_look_ahead:
                    return ii + 1
        return None


def part01_answer() -> str:
    loader = DataLoader(2022, "day06.txt")
    data = loader.read()
    elf_packet = ElfPacket(data)
    result = elf_packet.start_index(4)
    if result is None:
        return "No answer"
    else:
        return str(result)


def part02_answer() -> str:
    loader = DataLoader(2022, "day06.txt")
    data = loader.read()
    elf_packet = ElfPacket(data)
    result = elf_packet.start_index(14)
    if result is None:
        return "No answer"
    else:
        return str(result)
