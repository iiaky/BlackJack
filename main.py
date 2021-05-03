from BJ import *
score = 0
computer_score = 0
hand = []
computer_hand = []

def game_end():
    print ("Score: ", player.score, "Computer score: ", computer.score)
    if score == 21 and computer_score == 21:
        return "You tied!"
    elif score == 21 and computer_score != 21:
        return "You win!"
    elif score < 21 and computer_score < 21:
        if score > computer_score:
            return "You win!"
        elif score < computer_score:
            return "You lose!"
    elif score < 21 and computer_score > 21:
        return "You win!"
    elif score > 21 and computer_score < 21:
        return "You lose!"
    return "You both bust"

# playing ----------**------------

print("Press H to start")
start = input()
player = Player(hand, score)
computer = Computer(computer_hand, computer_score)

while start.upper() == "H":
    player.hit()
    print("Your score: " + str(player.check()))
    print("Press H to hit; S to stay")
    start = input()

    if start.upper() == "S":
        print(game_end())
        break

