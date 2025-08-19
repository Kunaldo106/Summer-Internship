import random
import pygame
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk, PhotoImage



# Global variables

username = "Unknown"
score = 0
count = 0
window_size_1= 450
window_size_2= 450


# Initialize pygame mixer
pygame.mixer.init()

game_over_sound= pygame.mixer.Sound("Track_1.mp3")

def log_out():

    pygame.mixer.music.pause()
    entry1.delete(0,tk.END)
    reset_game()
    show_frame(frame1)

def play_temp_effect(effect_sound):
    pygame.mixer.music.pause()
    effect_sound.play()
    duration = int(effect_sound.get_length() * 1000)
    window.after(duration, pygame.mixer.music.unpause)




def sound():
    try:
        pygame.mixer.music.load("Track_2.mp3")
        pygame.mixer.music.play(-1)
    except Exception as e:
        print("Sound error:", e)


#change Background Music
def change_bg_music():
    list_music=['Track_3.mp3','Track_4.mp3','Track_2.mp3','Track_5.mp3','Track_6.mp3']
    var_music= random.choice(list_music)
    try:
        pygame.mixer.music.load(var_music)
        pygame.mixer.music.play(-1)
    except Exception as e:
        print("Sound error:", e)

#image function
def option_image(user_choice, bot_choice):
    # Clear previous images
    for widget in image_container.winfo_children():
        widget.destroy()

    # Map choice -> image file
    img_map = {
        "Rock": "rock.png",
        "Paper": "paper.png",
        "Scissor": "scissor.png"
    }

    # Load corresponding images
    user_img = Image.open(img_map[user_choice]).resize((100, 100))
    bot_img = Image.open(img_map[bot_choice]).resize((100, 100))
    user_photo = ImageTk.PhotoImage(user_img)
    bot_photo = ImageTk.PhotoImage(bot_img)

    # Keep refs alive
    image_container.user_photo = user_photo
    image_container.bot_photo = bot_photo

    # Show left = user, center = VS, right = bot
    tk.Label(image_container, image=user_photo, text="You", compound="top").pack(side="left", padx=20)
    tk.Label(image_container, text="VS", font=("Arial", 20, "bold"), fg="red").pack(side="left", padx=10)
    tk.Label(image_container, image=bot_photo, text="Bot", compound="top").pack(side="left", padx=20)

# default
def show_default_images():
    # Clear previous (just in case)
    for widget in image_container.winfo_children():
        widget.destroy()

    try:
        default_img = Image.open("question.png").resize((100, 100))
        user_photo = ImageTk.PhotoImage(default_img)
        bot_photo = ImageTk.PhotoImage(default_img)

        # Keep refs alive
        image_container.user_photo = user_photo
        image_container.bot_photo = bot_photo

        # Add images to the container
        tk.Label(image_container, image=user_photo, text="You", compound="top").pack(side="left", padx=20)
        tk.Label(image_container, text="VS", font=("Arial", 20, "bold"), fg="red").pack(side="left", padx=10)
        tk.Label(image_container, image=bot_photo, text="Bot", compound="top").pack(side="left", padx=20)
    except Exception as e:
        print("Default image load error:", e)

# Tkinter window setup
window = tk.Tk()
output = tk.StringVar()

output3 = tk.StringVar()
output4 = tk.StringVar()
username_var = tk.StringVar()
window.geometry(f'{window_size_1}x{window_size_2}')
window.title('Rock Paper Scissor')
window.resizable(False, False)

# Reset game function
def reset_game():

    global count, score
    enable_game_button()
    count = 0
    score = 0
    output.set("")

    output3.set("Score: 0")
    output4.set("Losses: 0")
    show_default_images()


#disable button of frame4
def disable_game_button():
    rock_button.config(state= "disabled")
    paper_button.config(state="disabled")
    scissor_button.config(state="disabled")

def enable_game_button():
    rock_button.config(state= "enabled")
    paper_button.config(state="enabled")
    scissor_button.config(state="enabled")

# Read and display score
def score_show():
    for widget in frame6.winfo_children():
        if widget != label_score:
            widget.destroy()

    try:
        with open(f"{username}.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        content = "No score found yet."

    label_score_main = ttk.Label(master=frame6, text=content)
    label_score_main.pack(pady=10)

    back_button_score = ttk.Button(master=frame6, text="Back", command=lambda: show_frame(frame3))
    back_button_score.pack(pady=60)

# Set window icon
try:
    icon = PhotoImage(file="winicon1.png")
    window.iconphoto(False, icon)
except Exception as e:
    print("Icon not loaded:", e)

main_canvas = tk.Canvas(master=window)
main_canvas.pack(fill="both", expand=True)

# Load button images
try:
    rock_img = Image.open("rock.png").resize((50, 50))
    rock_photo = ImageTk.PhotoImage(rock_img)

    paper_img = Image.open("paper.png").resize((50, 50))
    paper_photo = ImageTk.PhotoImage(paper_img)

    scissor_img = Image.open("scissor.png").resize((50, 50))
    scissor_photo = ImageTk.PhotoImage(scissor_img)
except Exception as e:
    print("Image load error:", e)
    rock_photo = paper_photo = scissor_photo = None

# Function to take username
def takeusername():
    global username
    name = entry1.get().strip()
    if name:
        username = name
        username_var.set(f"Player: {username}")
    else:
        username = "Unknown"
        username_var.set("Player: Unknown")

# Game logic functions
def rock():
    play_game("Rock")

def paper():
    play_game("Paper")

def scissor():
    play_game("Scissor")

def play_game(user_input):
    choice = ['Rock', 'Paper', 'Scissor']
    bot_input = random.choice(choice)
    logic(user_input, bot_input, username)

def logic(value1, value2, username):
    global score, count

    if value1 == value2:
        output.set("It's a tie")
    elif (value1 == 'Scissor' and value2 == 'Paper') or \
         (value1 == 'Rock' and value2 == 'Scissor') or \
         (value1 == 'Paper' and value2 == 'Rock'):
        score += 100
        output.set("You Win")
    else:
        score -= 25
        count += 1
        output.set("You Lose")


    output3.set(f"Score: {score}")
    output4.set(f"Losses: {count}")

    option_image(value1, value2)

    if count >= 10:
        disable_game_button()
        output.set("Game Over")

        play_temp_effect(game_over_sound)



        # Save score
        try:
            with open(f"{username}.txt", "w") as f:
                f.write(f"{username}'s Final Score: {score}\n")
        except Exception as e:
            print("Error writing score:", e)





# Frame switcher
def show_frame(frame_variable):
    frame_variable.tkraise()

# Volume control
def set_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

# --- Frames Setup ---

# Frame 1 - Welcome
frame1 = tk.Frame(master=main_canvas, height=window_size_1, width=window_size_2)
button1 = ttk.Button(master=frame1, text="Log in", command=lambda: show_frame(frame2))
button1.pack(pady=80)
frame1.pack()

# Frame 2 - Username input
frame2 = tk.Frame(master=main_canvas,height=window_size_1, width=window_size_2)
label1 = ttk.Label(master=frame2, text="Enter Username:")
label1.pack(pady=5)

entry1 = ttk.Entry(master=frame2, width=20)
entry1.pack(pady=3)

button2 = ttk.Button(master=frame2, text="Enter", command=lambda: (takeusername(), show_frame(frame3), sound()))
button2.pack()
frame2.pack()

# Frame 3 - Main Menu
frame3 = tk.Frame(master=main_canvas,height=window_size_1, width=window_size_2)

start_button = ttk.Button(master=frame3, text="Start", command=lambda: show_frame(frame4))
start_button.pack(pady=5)

score_button = ttk.Button(master=frame3, text="Score", command=lambda: (score_show(), show_frame(frame6)))
score_button.pack(pady=5)

option_button = ttk.Button(master=frame3, text="Option", command=lambda: show_frame(frame5))
option_button.pack(pady=5)

log_out_button= ttk.Button(master=frame3, text="Log Out", command= lambda: log_out())
log_out_button.pack(pady=5)

exit_button = ttk.Button(master=frame3, text="Exit", command=window.quit)
exit_button.pack(pady=5)
frame3.pack()

# Frame 4 - Game
frame4 = tk.Frame(master=main_canvas,height=window_size_1, width=window_size_2)

username_label = ttk.Label(master=frame4, textvariable=username_var)
username_label.pack(pady=10)

output_label3 = ttk.Label(master=frame4, textvariable=output3)
output_label3.pack()

output_label4 = ttk.Label(master=frame4, textvariable=output4)
output_label4.pack()

image_container= ttk.Frame(master=frame4)
image_container.pack(pady=10)

show_default_images()

frame_frame4 = ttk.Frame(master=frame4)

rock_button = ttk.Button(master=frame_frame4, image=rock_photo, command=rock)
rock_button.image = rock_photo
rock_button.pack(side="left")

paper_button = ttk.Button(master=frame_frame4, image=paper_photo, command=paper)
paper_button.image = paper_photo
paper_button.pack(side="left")

scissor_button = ttk.Button(master=frame_frame4, image=scissor_photo, command=scissor)
scissor_button.image = scissor_photo
scissor_button.pack(side="left")

frame_frame4.pack(padx=20, pady=(20, 10))



output_label = ttk.Label(master=frame4, textvariable=output, font=("Arial",20))
output_label.pack()

home_button = ttk.Button(master=frame4, text="Home", command=lambda: show_frame(frame3))
home_button.pack(pady=5)
frame4.pack()

reset_button= ttk.Button(master=frame4, text="Reset", command= reset_game)
reset_button.pack(pady=5)

# Frame 5 - Options
frame5 = tk.Frame(master=main_canvas,height=window_size_1, width=window_size_2)

volume_label = ttk.Label(master=frame5, text="Music Volume")
volume_label.pack(pady=10)

vol_slider = ttk.Scale(master=frame5, from_=0, to=100, orient="horizontal", command=set_volume)
vol_slider.set(20)
vol_slider.pack(pady=10)

change_music= ttk.Button(master=frame5, text= "Change Music", command=change_bg_music)
change_music.pack(pady=5)



back_button = ttk.Button(master=frame5, text="Back", command=lambda: show_frame(frame3))
back_button.pack(pady=40)
frame5.pack()

# Frame 6 - Score Screen
frame6 = tk.Frame(master=main_canvas,height=window_size_1, width=window_size_2)

label_score = ttk.Label(master=frame6, text="Your Last Score")
label_score.pack(pady=10)
frame6.pack()

# Place all frames
frame_list=[frame1, frame2, frame3, frame4, frame5, frame6]
for frame in frame_list:
    frame.place(x=0, y=0, width=window_size_1, height=window_size_2)

# Start the app
show_frame(frame1)
window.mainloop()
