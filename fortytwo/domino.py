from typing import override


class Domino:
    def __init__(self, sideOne: int, sideTwo: int):
        # Validate inputs are integers
        if not isinstance(sideOne, int) or not isinstance(sideTwo, int):
            raise TypeError("Domino values must be integers")

        # Validate values are between 0 and 6
        if not (0 <= sideOne <= 6) or not (0 <= sideTwo <= 6):
            raise ValueError("Domino values must be between 0 and 6")

        self.sideOne: int = sideOne
        self.sideTwo: int = sideTwo
        self.natural_suit: int = sideOne if sideOne > sideTwo else sideTwo

    def is_double(self) -> bool:
        return self.sideOne == self.sideTwo

    def get_suit(self, lead_suit: int | None) -> int:
        if lead_suit is None:
            return self.natural_suit

        if self.sideOne == lead_suit:
            return self.sideOne

        if self.sideTwo == lead_suit:
            return self.sideTwo

        return self.natural_suit

    def is_count(self) -> bool:
        return (self.sideOne + self.sideTwo) % 5 == 0

    def get_value(self) -> int:
        sum = self.sideOne + self.sideTwo
        if sum % 5 == 0:
            return sum
        return 0

    @override
    def __repr__(self):
        return f"Domino({self.sideOne}, {self.sideTwo})"

    @override
    def __str__(self) -> str:
        top_str = str(self.sideOne)
        bottom_str = str(self.sideTwo)

        width = max(len(top_str), len(bottom_str))

        padding = 2  # one space on each side
        box_width = width + padding

        domino_art = [
            f"+{'-' * box_width}+",
            f"|{top_str:^{box_width}}|",
            f"|{'-' * box_width}|",
            f"|{bottom_str:^{box_width}}|",
            f"+{'-' * box_width}+",
        ]

        return "\n".join(domino_art)
