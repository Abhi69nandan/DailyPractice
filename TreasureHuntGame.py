# TREASURE HUNT GAME
import random

def print_map(game_map, reveal=False):
    print("\n  1   2   3")
    for i, row in enumerate(game_map, 1):
        display_row = []
        for cell in row:
            if reveal:
                display_row.append(cell)
            else:
                display_row.append("⬜" if cell in ["💰", "💣", ""] else cell)
        print(f"{i} {' | '.join(display_row)}")

def create_map():
    return [["" for _ in range(3)] for _ in range(3)]

def place_items(game_map, emoji, count):
    spots = [(r, c) for r in range(3) for c in range(3)]
    random.shuffle(spots)
    for _ in range(count):
        r, c = spots.pop()
        game_map[r][c] = emoji

def play_game():
    game_map = create_map()

    place_items(game_map, "💰", 2)
    place_items(game_map, "💣", 1)

    print("🏴‍☠️ Welcome to the EMOJI TREASURE HUNT! 🪙")
    print("Try to find the treasure without hitting a trap!")
    print_map(game_map)

    while True:
        position = input("\nPick a spot to dig (e.g. 23 = column 2, row 3): ")
        if len(position) == 2 and position.isdigit():
            col = int(position[0]) - 1
            row = int(position[1]) - 1
            if 0 <= col <= 2 and 0 <= row <= 2:
                result = game_map[row][col]
                if result == "💰":
                    print("\n🎉 You found a TREASURE! 💰💰💰")
                    game_map[row][col] = "⭐"
                elif result == "💣":
                    print("\n💥 Boom! You hit a TRAP! 💣 Game over!")
                    game_map[row][col] = "💥"
                else:
                    print("\n😅 Just empty sand... Try again next time!")
                    game_map[row][col] = "❌"
                break
            else:
                print("⛔ Coordinates out of range! Use numbers 1-3.")
        else:
            print("⛔ Invalid input! Use two digits like 23 (column then row).")

    print("\n🗺️ Final Map Reveal:")
    print_map(game_map, reveal=True)

play_game()

while input("\nPlay again? (y/n): ").lower() == "y":
    play_game()

print("\n🏁 Thanks for playing the Emoji Treasure Hunt! See you next time! 👋")
