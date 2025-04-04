import random

def guess_the_number():
    print("🎯 Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 7 attempts to guess it correctly.")

    number_to_guess = random.randint(1, 100)
    attempts_left = 7

    while attempts_left > 0:
        try:
            guess = int(input(f"\nEnter your guess ({attempts_left} attempts left): "))
        except ValueError:
            print("🚫 Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("⚠️ Your guess must be between 1 and 100.")
            continue

        if guess == number_to_guess:
            print(f"🎉 Congratulations! You guessed the number {number_to_guess} correctly!")
            break
        elif guess < number_to_guess:
            print("📈 Too low!")
        else:
            print("📉 Too high!")

        attempts_left -= 1

    else:
        print(f"\n💥 You've run out of attempts! The number was {number_to_guess}. Better luck next time!")

if __name__ == "__main__":
    guess_the_number()
