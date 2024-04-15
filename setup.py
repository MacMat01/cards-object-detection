import os

dirs = ['timer', 'timer/tests', 'player', 'player/tests', 'card', 'card/tests', 'game', 'game/tests']

files = ['timer/timer.py', 'timer/tests/test_timer.py', 'player/player.py', 'player/tests/test_player.py',
         'card/card.py', 'card/tests/test_card.py', 'game/game.py', 'game/tests/test_game.py']

for dir in dirs:
    os.makedirs(dir, exist_ok=True)

for file in files:
    open(file, 'a').close()
