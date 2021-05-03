import random

deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

class Player():
    def __init__(self, hand, score):
        self.hand = hand
        self.score = score

    def hit(self):
        self.draw = random.choice(deck)
        self.hand.append(self.draw)
        print(self)

    def check(self):
        # face cards
        global score
        if (self.draw == 'J' or self.draw == 'Q' or self.draw == 'K'):
            self.score = self.score + 10
            score = self.score
            return score
        # A.
        elif (self.draw == "A"):
            if not self.score + 11 > 21:
                self.score = self.score + 11
                score = self.score
                return score
            else:
                self.score = self.score + 1
                score = self.score
                return score
        # numbers
        elif (type(self.draw) == int):
            self.score = self.score + self.draw
            score = self.score
            return score

    def __str__(self):
        return f"You drew: " + str(self.draw) + "\n" + "Your hand: " + str(self.hand)


class Computer():
    def __init__(self, hand, computer_score):
        self.hand = hand
        self.score = computer_score
        self.hit()

    def hit(self):
        self.draw = random.choice(deck)
        self.hand.append(self.draw)
        self.check()

    def check(self):
        # face cards
        global computer_score
        if (self.draw == 'J' or self.draw == 'Q' or self.draw == 'K'):
            if ((not self.score > 17) or self.score == 21):
                self.score = self.score + 10
                computer_score = self.score
        # A.
        elif (self.draw == "A"):
            if ((not self.score > 17) or self.score == 21):
                if not self.score + 11 > 21:
                    self.score = self.score + 11
                    computer_score = self.score
                else:
                    self.score = self.score + 1
                    computer_score = self.score
            # numbers
            elif (type(self.draw) == int):
                self.score = self.score + self.draw
                computer_score = self.score
            else:
                return computer_score

        self.hit()

    __hash__ = None
