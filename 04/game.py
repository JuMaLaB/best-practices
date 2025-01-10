"""Module gampe.py description"""

__author__ = "Ju MalaB"


import random


class Player:
    """Class Player"""

    def __init__(self, name: str, dice: int) -> None:
        self.name = name
        self.dice = dice

    def __repr__(self) -> str:
        return f"Player: {repr(self.name)} with {repr(self.dice)}"


class Game:
    """Class Game"""

    def __init__(self, player1: Player, player2: Player):
        """Create the player for the game"""
        self.player1 = player1
        self.player2 = player2

    def roll_dice(self):
        """Function rool_dice()"""
        dice_total = random.randint(1, 6) + random.randint(1, 6)
        return dice_total

    def run(self, player1: Player, player2: Player):
        """Function run()"""

        player1.dice = self.roll_dice()
        player2.dice = self.roll_dice()

        print(player1.name, "rolled", player1.dice)
        print(player2.name, "rolled", player2.dice)

        if player1.dice > player2.dice:
            print(player1, "wins the game")
        elif player2.dice > player1.dice:
            print(player2, "wins the game")
        else:
            print("Tie !")


if __name__ == "__main__":
    game = Game(
        Player(input("Enter player 1's name:\n"), 0),
        Player(input("Enter player 2's name:\n"), 0),
    )
    game.run(game.player1, game.player2)
