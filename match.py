from game import Game

class Match:
    def __init__(self) -> None:
        self.games: list[Game] = []

    def insert_game(self, game: Game) -> None:
        self.games.append(game)

    @property
    def has_ended(self) -> bool:
        if len(self.games) == 7:
            return True
        if len(self.games) in [1, 2, 5]:
            return False
        sum_f_result = 0
        sum_v_result = 0
        for game in self.games:
            sum_f_result += game.f_result
            sum_v_result += game.v_result
        if len(self.games) == 3:
            return abs(sum_f_result - sum_v_result) > 1
        else:
            return abs(sum_f_result - sum_v_result) > 0

    def __str__(self) -> str:
        string = ''
        if len(self.games) == 0:
            return string
        round_labels = []
        for round_index in range(1, 7 + 1):
            if len(self.games) < round_index:
                round_labels.append(f'{round_index}')
            else:
                round_labels.append(f'[{round_index}]({self.games[round_index - 1].link})')
        string += f'| | {" | ".join(round_labels)} | |'
        string += '\n'
        string += '| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |'
        string += '\n'
        f_results = []
        v_results = []
        for round_index in range(1, 7 + 1):
            if len(self.games) < round_index:
                if self.has_ended:
                    f_results.append('-')
                    v_results.append('-')
                else:
                    f_results.append('?')
                    v_results.append('?')
            else:
                f_results.append(f'{self.games[round_index - 1].f_result}')
                v_results.append(f'{self.games[round_index - 1].v_result}')
        sum_f_result = 0
        sum_v_result = 0
        for game in self.games:
            sum_f_result += game.f_result
            sum_v_result += game.v_result
        if self.games[0].result == self.games[0].f_result:
            string += f'| Frederico | {" | ".join(f_results)} | {sum_f_result} |'
            string += '\n'
            string += f'| Vicente | {" | ".join(v_results)} | {sum_v_result} |'
            string += '\n'
        if self.games[0].result == self.games[0].v_result:
            string += f'| Vicente | {" | ".join(v_results)} | {sum_v_result} |'
            string += '\n'
            string += f'| Frederico | {" | ".join(f_results)} | {sum_f_result} |'
            string += '\n'
        return string