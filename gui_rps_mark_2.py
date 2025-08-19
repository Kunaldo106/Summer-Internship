import random
import tkinter as tk
from PIL import ImageTk, Image

from tkinter import ttk, Frame, Label, PhotoImage

username= None
def takeusername():
    global username
    username= entry1.get()




def rock():
    choice=['Rock', 'Paper', 'Scissor']
    user_input= 'Rock'
    bot_input= random.choice(choice)

    logic(user_input, bot_input, username)


def paper():
    choice = ['Rock', 'Paper', 'Scissor']
    user_input = 'Paper'
    bot_input= random.choice(choice)

    logic(user_input, bot_input, username)


def scissor():
    choice = ['Rock', 'Paper', 'Scissor']
    user_input = 'Scissor'
    bot_input= random.choice(choice)

    logic(user_input, bot_input, username)


def logic(value1, value2, username):
    global output
    if value1 == value2:
        output2.set(f"{username}: {value1}     Computer: {value2}")
        output.set("It's a tie")
    elif value1== 'Scissor' and value2== 'Paper':
        output2.set(f"{username}: {value1}     Computer: {value2}")
        output.set("You Win")
    elif value1== 'Rock' and value2== 'Scissor':
        output2.set(f"{username}: {value1}     Computer: {value2}")
        output.set("You Win")
    elif value1=='Paper' and value2 =='Rock':
        output2.set(f"{username}: {value1}     Computer: {value2}")
        output.set("You Win")
    else:
        output2.set(f"{username}: {value1}     Computer: {value2}")
        output.set("You Lose")

def show_frame(frame_variable):
    frame_variable.tkraise()



window= tk.Tk()
output= tk.StringVar()
output2= tk.StringVar()
window.geometry('300x300')
window.title('Rock Paper Scissor')


#Changing Icon
icon= PhotoImage(file="winicon1.png")
window.iconphoto(False, icon)

main_canvas= tk.Canvas(master=window)
main_canvas.pack()

# Creating Frame1
frame1= tk.Frame(master=main_canvas)
button1= ttk.Button(master=frame1, text="Log in", command= lambda: show_frame(frame2))
button1.pack(side="top",pady=80)


frame1.pack()

#Creating Frame2
frame2= tk.Frame(master= main_canvas)
label1= ttk.Label(master= frame2, text="Enter Username:")
label1.pack(pady= 5)

entry1= ttk.Entry(master=frame2, width=20)
entry1.pack(pady= 3)

button2= ttk.Button(master=frame2, text= "Enter", command= lambda: (takeusername, show_frame(frame3)))
button2.pack()


frame2.pack()

#Creating Frame3
frame3= ttk.Frame(master= main_canvas)

start_button= ttk.Button(master=frame3, text="Start", command=lambda: show_frame(frame4))
start_button.pack(pady=5,)

option_button= ttk.Button(master=frame3, text="Option")
option_button.pack(pady=5)

exit_button= ttk.Button(master=frame3, text="Exit", command= window.quit)
exit_button.pack(pady=5)

frame3.pack()

#Creating Frame4

frame4= ttk.Frame(master=main_canvas)

frame_frame4= ttk.Frame(master=frame4)

rock_button= ttk.Button(master=frame_frame4, text="Rock", command= rock)
rock_button.pack(side="left",)

paper_button= ttk.Button(master=frame_frame4, text="Paper", command= paper)
paper_button.pack(side="left")

scissor_button= ttk.Button(master=frame_frame4, text="Scissor", command= scissor)
scissor_button.pack(side="left")

home_button= ttk.Button(master=frame4, text= "Home", command=lambda: show_frame(frame3))
home_button.pack()

frame_frame4.pack(padx= 20, pady= (150,20))

output_label2= ttk.Label(master= frame4, text= "Output", textvariable= output2)
output_label2.pack()

output_label= ttk.Label(master= frame4, text="Output", textvariable= output)
output_label.pack()




frame4.pack()


#Switch from one frame to another
for frame in (frame1, frame2, frame3,frame4):
    frame.place(x= 0, y=0, width=300, height=300)
show_frame(frame1)






window.mainloop()
print(username)

