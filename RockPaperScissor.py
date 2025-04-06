import random

name = input("Enter your name: ")
print("Hello!", name)

option = ["Rock", "Paper", "Scissor"]
winning_cases = {
    "Rock": "Scissor",
    "Paper": "Rock",
    "Scissor": "Paper"
}

while True:
    user = input("\nLet's play Rock, Paper & Scissors!\nChoose Rock, Paper or Scissor: ").capitalize()

    if user not in option:
        print("Invalid choice. Please choose Rock, Paper, or Scissor.")
        continue

    comp = random.choice(option)
    print("Computer Picked:", comp)

    if user == comp:
        print("TIE!!")
    elif winning_cases[user] == comp:
        print("YOU WIN!!!")
    else:
        print("COMPUTER WINS!!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("THANK YOU FOR PLAYING!")
        break
