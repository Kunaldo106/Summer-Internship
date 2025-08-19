import random
import tkinter as tk
from tkinter import ttk, Frame, Label



def rock():
    choice=['Rock', 'Paper', 'Scissor']
    user_input= 'Rock'
    bot_input= random.choice(choice)

    logic(user_input, bot_input)


def paper():
    choice = ['Rock', 'Paper', 'Scissor']
    user_input = 'Paper'
    bot_input= random.choice(choice)

    logic(user_input, bot_input)


def scissor():
    choice = ['Rock', 'Paper', 'Scissor']
    user_input = 'Scissor'
    bot_input= random.choice(choice)

    logic(user_input, bot_input)


def logic(value1, value2):
    global output
    if value1 == value2:
        output.set("It's a tie")
    elif value1== 'Scissor' and value2== 'Paper':
        output.set("You Win")
    elif value1== 'Rock' and value2== 'Scissor':
        output.set("You Win")
    elif value1=='Paper' and value2 =='Rock':
        output.set("You Win")
    else:
        output.set("You Lose")


window= tk.Tk()
output= tk.StringVar()
window.geometry('300x300')
window.title('Rock Paper Scissor')

canvas1= tk.Canvas(master= window)
frame= ttk.Frame(master= window, )

label1= ttk.Label(master= frame,
              text='Rock Paper Scissor',
              font=('Arial', 20,),

              )
label1.pack()

frame.pack()

frame2= ttk.Frame(master= window)
button1= ttk.Button(master=frame2,
                text='Rock',
                command= rock
                )
button1.pack(side="left"  )

button2= ttk.Button(master=frame2,
                text='Paper',
                command= paper
                )
button2.pack(side="left")

button3= ttk.Button(master=frame2,
                text='Scissor',
                command= scissor
                )
button3.pack(side="left")

frame2.pack()

frame3= Frame(master=window)



label2= Label(master=frame3,
              text='Output',
              textvariable= output
              )
label2.pack()


frame3.pack()











window.mainloop()