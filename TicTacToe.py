# TIC TAC TOE WITH FRIEND
import tkinter as tk
from tkinter import messagebox

#  main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)

player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def is_draw():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

def on_click(row, col):
    global player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = player
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_board()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            player = "O" if player == "X" else "X"

def reset_board():
    global player
    player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""

# buttons grid
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Helvetica", 32), width=5, height=2,
                                  command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
