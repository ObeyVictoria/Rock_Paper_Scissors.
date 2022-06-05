import random

print("WELCOME, This is a Rock, Paper and Scissors game between you and the CPU.")
print("Follow the input instruction and ENJOY IT!")
possible_actions = ["R", "P", "S"]
computer_action = random.choice(possible_actions)

game_over = "false"
while True:
    user_action = input("Enter a choice (R, P, S) ")

    if user_action == computer_action:
        print(f"Both players selected {user_action}, It's a tie!")
    elif user_action == "R":
        if computer_action == "S":
            print("Player (Rock) : CPU (Scissors).")
            print("Rock smashes scissors! you win.!")
            print("Congratulations, You Won this Round")
        else:
            print("Player (Rock):CPU (Paper).")
            print("Paper covers rock! You lose.")
            print("Oops, Computer Wins")
        break

    elif user_action == "P":
        if computer_action == "R":
            print("Player (Paper):CPU (Rock).")
            print("Paper covers rock! you win.!")
            print("Congratulations, You Won this Round")
        else:
            print("Player (Paper):CPU (Scissors).")
            print("Scissors cuts Paper! You lose.")
            print("Oops, Computer Wins")
        break

    elif user_action == "S":
        if computer_action == "P":
            print("Player (Scissors):CPU (Paper).")
            print("Scissors cuts Paper! you win.!")
            print("Congratulations, You Won this Round")
        else:
            print("Player (Scissors):CPU (Rock).")
            print("Rock smashes scissors! You lose.")
            print("Oops, Computer Wins")
        break
    elif user_action != possible_actions:
        print("Error,you took a wrong action, follow instructions")
