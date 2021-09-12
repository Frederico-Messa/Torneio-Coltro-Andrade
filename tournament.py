from match import Match
from copy import deepcopy

class Tournament:
    def __init__(self) -> None:
        self.matches: list[Match] = []

    def insert_match(self, match: Match) -> None:
        self.matches.append(match)

    def update_current_match(self, match: Match) -> None:
        self.matches[-1] = match

    @property
    def current_match(self) -> Match:
        return deepcopy(self.matches[-1])

    def __str__(self) -> str:
        string = ''
        for match_index in range(1, len(self.matches) + 1):
            string += f'### Match {match_index}:'
            string += '\n'
            string += f'{self.matches[match_index - 1]}'
            string += '\n'
            string += '\n'
        return string