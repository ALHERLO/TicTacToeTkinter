import tkinter

def is_clicked(number):
    global clicked
    print(clicked)
    if number not in clicked:
        clicked.append(number)
        return True
    else:
        return False

def move(number):
    global player, player1_moves, player2_moves

    if player:
        player1_moves.append(number)
    else:
        player2_moves.append(number)
    print(f'Player 1 moves: {player1_moves}')
    print(f'Player 2 moves: {player2_moves}')
    check_win()

def check_win():
    global player, player1_moves, player2_moves, win_list, clicked, turn_label, is_winner
    for list in win_list:
        check1 = all(item in player1_moves for item in list)
        check2 = all(item in player2_moves for item in list)
        if check1:
            is_winner=True
            turn_label.config(text="Player 1 Wins!")
            print('Player 1 Wins')
            clicked = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            break
        if check2:
            is_winner = True
            print("Player 2 Wins")
            clicked = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            turn_label.config(text="Player 2 Wins!")
            break


def c1_clicked(event):
    if is_clicked(1):
        move(1)
        new_mark = mark()
        canvas1.itemconfig(text1, text=new_mark)
    else:
        print('already clicked')

def c2_clicked(event):
    if is_clicked(2):
        move(2)
        new_mark = mark()
        canvas2.itemconfig(text2, text=new_mark)
    else:
        print('already clicked')

def c3_clicked(event):
    if is_clicked(3):
        move(3)
        new_mark = mark()
        canvas3.itemconfig(text3, text=new_mark)
    else:
        print('already clicked')

def c4_clicked(event):
    if is_clicked(4):
        move(4)
        new_mark = mark()
        canvas4.itemconfig(text4, text=new_mark)
    else:
        print('already clicked')

def c5_clicked(event):
    if is_clicked(5):
        move(5)
        new_mark = mark()
        canvas5.itemconfig(text5, text=new_mark)
    else:
        print('already clicked')

def c6_clicked(event):
    if is_clicked(6):
        move(6)
        new_mark = mark()
        canvas6.itemconfig(text6, text=new_mark)
    else:
        print('already clicked')

def c7_clicked(event):
    if is_clicked(7):
        move(7)
        new_mark = mark()
        canvas7.itemconfig(text7, text=new_mark)
    else:
        print('already clicked')

def c8_clicked(event):
    if is_clicked(8):
        move(8)
        new_mark = mark()
        canvas8.itemconfig(text8, text=new_mark)
    else:
        print('already clicked')

def c9_clicked(event):
    if is_clicked(9):
        move(9)
        new_mark = mark()
        canvas9.itemconfig(text9, text=new_mark)
    else:
        print('already clicked')

def mark():
    global player, is_winner
    new_mark = ''
    if player == True:
        new_mark= 'X'
    else:
        new_mark= 'O'

    player = not player
    if is_winner==False:
        if player == True:
            turn_label.config(text="Player 1")
        else:
            turn_label.config(text="Player 2")
    return new_mark


def reset_all():
    global player, clicked, player1_moves, player2_moves, is_winner
    player = True
    clicked = []
    player1_moves=[]
    player2_moves=[]
    is_winner=False
    turn_label.config(text="Player 1")
    canvas1.itemconfig(text1, text="")
    canvas2.itemconfig(text2, text="")
    canvas3.itemconfig(text3, text="")
    canvas4.itemconfig(text4, text="")
    canvas5.itemconfig(text5, text="")
    canvas6.itemconfig(text6, text="")
    canvas7.itemconfig(text7, text="")
    canvas8.itemconfig(text8, text="")
    canvas9.itemconfig(text9, text="")
    player1_moves = []
    print('reset clicked')
    return

def reset_button(event):
    print('reset button clicked!')
    return

#PLAYER 1 === X TRUE, PLAYER 2 ++ O FALSE
is_winner=False
player = True
player1_moves= []
player2_moves=[]
clicked = []
win_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7]
]

sand = "#38b395"
green = "navy"
FONT_NAME = "Courier"

window = tkinter.Tk()
window.title("Gato")
window.config(padx=50, pady=50, bg=green)

turn_label=tkinter.Label(text="Player 1", pady=10,  bg=green, fg="white", font=("Arial", 20, "italic"))
turn_label.grid(column=0, row=3, columnspan=3)

canvas1 = tkinter.Canvas(width=100, height=100, bg=sand,  highlightthickness=0)
canvas1.create_image(100, 112)
text1 = canvas1.create_text(50, 50, text="", fill="white", font=(FONT_NAME, 100, "bold"))
canvas1.bind('<Button>', c1_clicked)
canvas1.grid(padx=5, pady=5, column=0, row=0)


canvas2 = tkinter.Canvas(width=100, height=100, bg=sand,  highlightthickness=0)
canvas2.create_image(100, 112)
text2 = canvas2.create_text(50, 50, text="", fill="white", font=(FONT_NAME, 100, "bold"))
canvas2.bind('<Button>', c2_clicked)
canvas2.grid(padx=5, pady=5, column=1, row=0)

canvas3 = tkinter.Canvas(width=100, height=100, bg=sand,  highlightthickness=0)
canvas3.create_image(100, 112)
text3 = canvas3.create_text(50, 50, text="", fill="white", font=(FONT_NAME, 100, "bold"))
canvas3.bind('<Button>', c3_clicked)
canvas3.grid(padx=5, pady=5, column=2, row=0)

canvas4 = tkinter.Canvas(width=100, height=100, bg=sand,  highlightthickness=0)
canvas4.create_image(100, 112)
text4 = canvas4.create_text(50, 50, text="", fill="white", font=(FONT_NAME, 100, "bold"))
canvas4.bind('<Button>', c4_clicked)
canvas4.grid(padx=5, pady=5, column=0, row=1)

canvas5 = tkinter.Canvas(width=100, height=100, bg=sand,  highlightthickness=0)
canvas5.create_image(100, 112)
text5 = canvas5.create_text(50, 50, text="", fill="white", font=(FONT_NAME, 100, "bold"))
canvas5.bind('<Button>', c5_clicked)
canvas5.grid(padx=5, pady=5, column=1, row=1)

canvas6 = tkinter.Canvas(width=100, height=100, bg=sand,  highlightthickness=0)
canvas6.create_image(100, 112)
text6 = canvas6.create_text(50, 50, text="", fill="white", font=(FONT_NAME, 100, "bold"))
canvas6.bind('<Button>', c6_clicked)
canvas6.grid(padx=5, pady=5, column=2, row=1)

canvas7 = tkinter.Canvas(width=100, height=100, bg=sand,  highlightthickness=0)
canvas7.create_image(100, 112)
text7 = canvas7.create_text(50, 50, text="", fill="white", font=(FONT_NAME, 100, "bold"))
canvas7.bind('<Button>', c7_clicked)
canvas7.grid(padx=5, pady=5, column=0, row=2)

canvas8 = tkinter.Canvas(width=100, height=100, bg=sand,  highlightthickness=0)
canvas8.create_image(100, 112)
text8 = canvas8.create_text(50, 50, text="", fill="white", font=(FONT_NAME, 100, "bold"))
canvas8.bind('<Button>', c8_clicked)
canvas8.grid(padx=5, pady=5, column=1, row=2)

canvas9 = tkinter.Canvas(width=100, height=100, bg=sand,  highlightthickness=0)
canvas9.create_image(100, 112)
text9 = canvas9.create_text(50, 50, text="", fill="white", font=(FONT_NAME, 100, "bold"))
canvas9.bind('<Button>', c9_clicked)
canvas9.grid(padx=5, pady=5, column=2, row=2)

my_button = tkinter.Button(text="RESET", pady=10,  bg='grey', fg='black', bd='0', command=reset_all, font=("Arial", 15, "italic"), highlightthickness=0)
my_button.grid(column=0, row=5, columnspan=3)


# New Canvas Button Added
canvasButton = tkinter.Canvas(width=125, height=50, bg=sand,  highlightthickness=0)
canvasButton.create_image(100, 112)
textButton = canvasButton.create_text(63, 27, text="Reset", fill="white", font=(FONT_NAME, 40, "bold"))
canvasButton.bind('<Button>', reset_button)
canvasButton.grid(padx=5, pady=5, column=0, row=6, columnspan=3)


window.mainloop()