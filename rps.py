from tkinter import *
from tkinter import scrolledtext
import random

root = Tk()
root.title('Rock Paper Scissors')
root.geometry('300x400')
root.configure(bg='light grey')


app_header = Label(root,bg='Light Grey', text="Rock Paper Scissors",fg="Blue", font=('Georgia', 21), padx=10, pady=30)
app_header.pack()


choices = ['Rock', 'Paper', 'Scissors']

# function to handle the game
def to_win(user_choice):
    computer_choice = random.choice(choices)
    display.configure(state=NORMAL)
    display.delete(0, END)
    if user_choice == computer_choice:
        result.set(f"Its a tie! Both chose {user_choice}")
    elif user_choice == 'Rock':
        if computer_choice == 'Scissors':
            result.set(f'You win: Rock crushes Scissors')
        else:
            result.set(f'You lose: Paper covers Rock')
    elif user_choice == 'Paper':
        if computer_choice == 'Rock':
            result.set(f'You win: Paper covers Rock')
        else:
            result.set(f'You lose: Scissors cut Paper')
    elif user_choice == 'Scissors':
        if computer_choice == 'Paper':
            result.set(f'You win: Scissors cut Paper')
        else:
            result.set(f'You lose: Rock crushes Scissors')
    else:
        result.set('Enter a valid play')

    onee.set(user_choice)
    threee.set(computer_choice)
    display.insert(0, result.get())
    display.configure(state=DISABLED)


# handle the reset button
def reset():
    onee.set("Player")
    threee.set("Computer")
    display.configure(state=NORMAL)
    display.delete(0, END)
    display.configure(state=DISABLED)


# containers that houses the
frame1 = Frame(root, width=40)
frame1.pack()

onee = StringVar()
onee.set("Player")
threee = StringVar()
threee.set("Computer")

one = Label(frame1, textvariable=onee)
two = Label(frame1, text="Vs", fg="Blue")
three = Label(frame1, textvariable=threee)

one.pack(side=LEFT)
two.pack(side=LEFT)
three.pack()


frame = Frame(root, bg='light grey')
frame.pack(pady=10)


result = StringVar()
display = Entry(frame, font=('Verdana', 10), width=28, state=DISABLED, justify="center")
display.grid(row=0, columnspan=3, padx=1, pady=1)


rock = Button(frame, text="Rock", command=lambda: to_win("Rock"))
paper = Button(frame, text='Paper', command=lambda: to_win('Paper'))
scissors = Button(frame, text='Scissors', command=lambda: to_win('Scissors'))

reset_button = Button(frame, text='Reset Game', bg='Black', fg='red', command=reset)

rock.grid(row=1, column=0, padx=5, pady=5)
paper.grid(row=1, column=1, padx=5, pady=5)
scissors.grid(row=1, column=2, padx=5, pady=5)
reset_button.grid(row=2, column=1, padx=5, pady=5)



root.mainloop()