from tkinter import *

root = Tk()
root.title("Tic-Tac-Toe")

def check_winner(event):
    b1text = b1.cget("text")
    b2text = b2.cget("text")
    b3text = b3.cget("text")
    b4text = b4.cget("text")
    b5text = b5.cget("text")
    b6text = b6.cget("text")
    b7text = b7.cget("text")
    b8text = b8.cget("text")
    b9text = b9.cget("text")

    if ( b1text == b2text == b3text == turn ):
        status["text"] = f"{turn} won the game!!"
    elif ( b4text == b5text == b6text == turn ): 
        status["text"] = f"{turn} won the game!!"
    elif ( b7text == b8text == b9text == turn ): 
        status["text"] = f"{turn} won the game!!"
    elif ( b1text == b4text == b7text == turn ): 
        status["text"] = f"{turn} won the game!!"
    elif ( b2text == b5text == b8text == turn ): 
        status["text"] = f"{turn} won the game!!"
    elif ( b3text == b6text == b9text == turn ): 
        status["text"] = f"{turn} won the game!!"
    elif ( b1text == b5text == b9text == turn ): 
        status["text"] = f"{turn} won the game!!"
    elif ( b3text == b5text == b7text == turn ): 
        status["text"] = f"{turn} won the game!!"

turn = "x"

def button_pressed(e):
    global turn

    clickedButton = e.widget

    if clickedButton.cget("text") != "":
        status["text"] = f"Choose a different button!!"
    else:    
        if turn == "x":
            clickedButton["text"] = "x"
            if check_winner(turn):
                print(f" {turn} wins the game!!")
            turn = "o"

        elif turn == "o":
            clickedButton["text"] = "o"
            if check_winner(turn):
                print(f" {turn} wins the game!!")
            turn = "x"

def reset():
    buttons = [b1,b2, b3, b4, b5, b6, b7, b8, b9, status]

    for button in buttons: 
        button["text"] = ""

b1 = Button(root, font=("Arial" , 15, "bold"), text="",height=5 ,width=10, justify = "center", bg="lightgreen")
b1.grid(row = 1, column = 28)
b1.bind("<Button-1>" , button_pressed)

b2 = Button(root, font=("Arial" , 15, "bold"), text="", height=5 ,width=10, justify = "center", bg="lightgreen")
b2.grid(row = 1, column = 29)
b2.bind("<Button-1>" , button_pressed)

b3 = Button(root,  font=("Arial" , 15, "bold"), text="",height=5 ,width=10, justify = "center", bg="lightgreen")
b3.grid(row = 1, column = 30)
b3.bind("<Button-1>" , button_pressed)

b4 = Button(root,  font=("Arial" , 15, "bold"), text="",height=5 ,width=10, justify = "center", bg="lightgreen")
b4.grid(row = 2, column=28)
b4.bind("<Button-1>" , button_pressed)

b5 = Button(root,  font=("Arial" , 15, "bold"), text="",height=5 ,width=10, justify = "center", bg="lightgreen")
b5.grid(row = 2, column=29)
b5.bind("<Button-1>" , button_pressed)

b6 = Button(root,  font=("Arial" , 15, "bold"), text="",height=5 ,width=10, justify = "center", bg="lightgreen")
b6.grid(row = 2, column=30)
b6.bind("<Button-1>" , button_pressed)

b7 = Button(root,  font=("Arial" , 15, "bold"), text="",height=5 ,width=10, justify = "center", bg="lightgreen")
b7.grid(row = 3, column=28)
b7.bind("<Button-1>" , button_pressed)

b8 = Button(root,  font=("Arial" , 15, "bold"), text="",height=5 ,width=10, justify = "center", bg="lightgreen")
b8.grid(row = 3, column=29)
b8.bind("<Button-1>" , button_pressed)

b9 = Button(root,  font=("Arial" , 15, "bold"), text="",height=5 ,width=10, justify = "center", bg="lightgreen")
b9.grid(row = 3, column=30)
b9.bind("<Button-1>" , button_pressed)

status = Label(root, font=("Arial", 15, "bold"), text="", height = 5, width = 25, justify="center")
status.grid(column = 28, columnspan=3, row = 10)

resetButton = Button(root, font=("Arial", 15, "bold"), text="Reset", height = 5, width = 10, justify = "center", command=reset, bg="firebrick4")
resetButton.grid(column = 28, columnspan=3, row = 11)


root.mainloop()
