from tkinter import *
root = Tk()
root.title("TicTacToe")

def zoneButton(index ,row, column):
    print(index, row, column)
    global player
    global zones
    if player == 0:
        zones[index].configure(text="X", padx=28 ,state=DISABLED)
        player += 1
    else:
        zones[index].configure(text="O", padx=23 ,state=DISABLED)
        player -= 1
    count = 0
    for i in range(0, 3):
        for k in range(0, 3):
            zones[count].grid_forget()
            zones[count].grid(row=i+1, column=k)
            count += 1

def game3x3():
    global player
    global zones
    gamemode = "3x3"
    player = 0
    zones = []

    count = 0
    for i in range(0, 3):
        for k in range(0, 3):
            zones.append(Button(root, text=" ", font=("Arial", 50), padx=40, command=lambda count=count, i=i, k=k, :zoneButton(count, i, k)))
            zones[count].grid(row=i+1, column=k)
            count += 1



newGame = Button(root, text="Új játék", font=("Arial", 10), command=game3x3)


newGame.grid(row=0, column=0)





root.mainloop()