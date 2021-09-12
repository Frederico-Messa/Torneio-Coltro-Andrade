import os
from tournament import Tournament
from match import Match
from game import Game

tournament = Tournament()
tournament.insert_match(Match())

links = [link for link in open(f'{os.path.dirname(__file__)}/links.txt').read().split('\n') if link != '']

for link in links:
    if tournament.current_match.has_ended:
        tournament.insert_match(Match())
    current_match = tournament.current_match
    current_match.insert_game(Game(link))
    tournament.update_current_match(current_match)

open(f'{os.path.dirname(__file__)}/index.md', 'w', encoding='utf-8').write(f'{tournament}')