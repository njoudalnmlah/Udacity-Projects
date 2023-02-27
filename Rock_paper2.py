import random


moves = ['rock', 'paper', 'scissors']


class Player:
    my_move = None
    their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            Choise = input("Choose Your move ")
            if Choise in moves:
                return Choise
            else:
                print("Error - wrong input!")

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):

    # Cons
    def __init__(self):
        super().__init__()
        self.moves_size = len(moves)
        self.my_next_move_index = random.randrange(self.moves_size)

    def move(self):
        my_next_move = moves[self.my_next_move_index]
        self.my_next_move_index = (
            self.my_next_move_index + 1) % self.moves_size
        return my_next_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def learn(self, my_move, their_move):
    self.my_move = my_move


class Game:
    player1score = 0
    player2score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print(" Equal ")

        elif beats(move1, move2) is True:
            self.player1score += 1
        else:
            print("player 2 Wins")
            self.player2score += 1
            print(f"Lost,{self.player1score}:{self.player2score}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Score: Player one{self.player1score}")
        print(f"Score: Player Two {self.player2score}")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            self.play_round()
            if self.player1score > self.player2score:
                print(" **** Congrats You Win ****")
            elif self.player1score == self.player2score:
                print(" **** Tie ****")
            else:
                print(" **** you lost ****")

        print("Game over!")
        print("General scores:")
        print(f"Player 1: {self.player1score}")
        print(f"Player 2: {self.player2score}")


if __name__ == '__main__':
    players = [

        RandomPlayer(),
        ReflectPlayer(),
        CyclePlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(players)
    game = Game(p1, p2)
    game.play_game().play_game()