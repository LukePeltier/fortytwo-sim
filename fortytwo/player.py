from fortytwo.domino import Domino


class Player:
    def __init__(self, name: str):
        self.name: str = name
        self.hand: list[Domino] = []
        self.partner: Player | None = None
