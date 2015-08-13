from models import Paper,Scissors,Rock
from draw_imperative import draw
#from draw_fp import draw
import random

if __name__ == '__main__':
    options = [Paper,Scissors,Rock]
    for i in range(1000):
        player1 = random.choice(options)
        player2 = random.choice(options)
        print "[ PLAYER 1 ]: plays %s" % player1.__name__
        print "[ PLAYER 2 ]: plays %s" % player2.__name__
        winner = draw(player1(),player2())


        winner_is_player_1 = True
        if winner is None:
            print "[ WINNER ]: No winner -- DRAW\n------\n"
            continue
        elif isinstance(winner,player2):
            winner_is_player_1 = False
        print "[ WINNER ]: %s with %s\n------\n" % (
            'player1' if winner_is_player_1 else 'player2',
            winner.__class__.__name__
        )

