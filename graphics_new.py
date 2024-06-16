import tkinter
from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import filedialog
import timer # type: ignore
import PIL


win = Tk()
win.geometry("1920x1080")
win.title("Graphics")
win.config(bg = "white")
win.iconphoto(True, PhotoImage(file="Transgender.png"))


canvas = Canvas(win, bg = "#28384A",)
canvas.config(width = 1920, height = 1080)
canvas.pack()

#################### Constants ####################
scene_counter = 0
get_width = 1920
get_height = 1080
angle = 0
#################### Image Imports ####################
rod_sterling = Image.open("rod_sterling.png")
rod_sterling_link = "rod_sterling.png"
reverse_spear = Image.open("reverse_spear.png")
reverse_spear_link = "reverse_spear.png"
spear = Image.open("spear.png")
spear_link = "spear.png"
shield = Image.open("tortured_soul.png")
shield_link = "tortured_soul.png"
troll = Image.open("sad.png")
troll_link = "sad.png"
oolong = Image.open("true_oolong.png")
oolong_link = "true_oolong.png"
#################### Functions ####################

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

def open_img(image_link, width, height, x, y):
    img = Image.open(image_link)
    img = img.resize((width, height))
    img = ImageTk.PhotoImage(img)
    canvas.create_image(x, y, image=img)
    return img

def rotate():
        global new_btn
        global angle
        global spear_temp_2
        # If the program has loaded, stop the loop
        if angle > -136:
            # Rotate the original image
            spear_temp = reverse_spear.rotate(angle)
            spear_temp_2 = ImageTk.PhotoImage(spear_temp)

            # put the rotated image inside the canvas
            canvas.delete("spear_temp_2")
            canvas.create_image(500, 350, image = spear_temp_2)

            # Call `loading_loop(i - 1)` after 2 milliseconds
            win.after(2, rotate)
            angle -= 1
        else:
            
            draw_scene5()
            new_btn.destroy()

def title():
    canvas.create_text(800, 300, text = "The Bad Vampire Movie Zone.", font = ('Times New Roman', 20), justify = 'center', fill='white')
    canvas.create_text(800, 330, text = "Made by two mentally ill people.", font = ('Times New Roman', 15), justify = 'center', fill='white')

def draw_scene1():
    global rod_sterling
    canvas.create_rectangle(0, 0, 1920, 150,
                                outline = "white", fill = "white",
                                width = 2)
    rod_sterling = open_img(rod_sterling_link, 500, 500, 800, 400)
    canvas.create_text(800, 30, text = "Imagine if you will: a fantastical world in which the divine", font = ('Times New Roman', 13), justify = 'center', fill='black')
    canvas.create_text(800, 49, text = "interacts with the mortal; a world in which the magical tales of", font = ('Times New Roman', 13), justify = 'center', fill='black')
    canvas.create_text(800, 68, text = "old are not merely shadows of a boundless immagination, but they", font = ('Times New Roman', 13), justify = 'center', fill='black')
    canvas.create_text(800, 87, text = "exist as a well formed gambit of a cosmic game. Well I'm both", font = ('Times New Roman', 13), justify = 'center', fill='black')
    canvas.create_text(800, 106, text = "glad, and frightened to inform you that this is the world in", font = ('Times New Roman', 13), justify = 'center', fill='black')
    canvas.create_text(800, 125, text = "which we live... This... is the Bad Vampire Movie Zone.", font = ('Times New Roman', 13), justify = 'center', fill='black')

def draw_scene2():
    global spear
    canvas.create_rectangle(0, 0, 1920, 1080,
                                outline = "#28384A", fill = "#28384A",
                                width = 2)
    canvas.create_rectangle(0, 0, 1920, 150,
                                outline = "white", fill = "white",
                                width = 2)
    
    spear = open_img(spear_link, 500, 500, 800, 400)
    canvas.create_text(800, 30, text = "I present to you now, a spear that is capable of piercing", font = ('Times New Roman', 13), justify = 'center', fill='black')
    canvas.create_text(800, 49, text = "through any object. Legend says that it was blessed by an ", font = ('Times New Roman', 13), justify = 'center', fill='black')
    canvas.create_text(800, 68, text = "ancient shaman, or maybe God was a little drunk, and thought it ", font = ('Times New Roman', 13), justify = 'center', fill='black')
    canvas.create_text(800, 87, text = "would be funny to make it; who knows, I'm making $#!% up at this", font = ('Times New Roman', 13), justify = 'center', fill='black')
    canvas.create_text(800, 106, text = "point...", font = ('Times New Roman', 13), justify = 'center', fill='black')

def draw_scene3():
    global shield
    canvas.create_rectangle(0, 0, 1920, 1080,
                                outline = "#28384A", fill = "#28384A",
                                width = 2)
    canvas.create_rectangle(0, 0, 1920, 150,
                                outline = "white", fill = "white",
                                width = 2)
    shield = open_img(shield_link, 500, 500, 800, 400)
    canvas.create_text(800, 30, text = "Similarly, a shield denoted as a symbol of great power in this", font = ('Times New Roman', 13), justify = 'center', fill='black')
    canvas.create_text(800, 49, text = "little blocky man's culture. unfortunatly for him, it was bound", font = ('Times New Roman', 13), justify = 'center', fill='black')
    canvas.create_text(800, 68, text = "to his very flesh by a curse. It also has the added affect of", font = ('Times New Roman', 13), justify = 'center', fill='black')
    canvas.create_text(800, 87, text = "being impenetrable somehow...? I guess God really had a rager", font = ('Times New Roman', 13), justify = 'center', fill='black')
    canvas.create_text(800, 106, text = "and decided to bless everything.", font = ('Times New Roman', 13), justify = 'center', fill='black')

def draw_scene4():
    global angle
    global reverse_spear
    global shield
    btn.destroy()
    canvas.create_rectangle(0, 0, 1920, 1080,
                                outline = "white", fill = "white",
                                width = 2)
    shield = open_img(shield_link, 500, 500, 1060, 400)
    
    new_btn = Button(win, text='Lets see what happens next', width=40,
                height=5, bd='10', command=rotate)
    new_btn.place(x=650, y=700)
    
    canvas.create_text(800, 30, text = "Let's see what happens when the two interact.", font = ('Times New Roman', 13), justify = 'center', fill='black')

def draw_scene5():
    global troll
    btn = Button(win, text='Press to go to next scene', width=40,
             height=5, bd='10', command=draw_next_screen)
    btn.place(x=650, y=700)
    
    canvas.create_rectangle(0, 0, 1920, 1080,
                                outline = "black", fill = "black",
                                width = 2)
    canvas.create_text(800, 30, text = "Uh oh! Unfortunatly, due to the paradoxical nature", font = ('Times New Roman', 13), justify = 'center', fill='white')
    canvas.create_text(800, 49, text = "of what we were about to show you, God has ", font = ('Times New Roman', 13), justify = 'center', fill='white')
    canvas.create_text(800, 68, text = "forbiden us from showing you what was about to", font = ('Times New Roman', 13), justify = 'center', fill='white')
    canvas.create_text(800, 87, text = "happen! He truly apologizes for his drunken", font = ('Times New Roman', 13), justify = 'center', fill='white')
    canvas.create_text(800, 106, text = "mistake.", font = ('Times New Roman', 13), justify = 'center', fill='white')
    troll = open_img(troll_link, 500, 500, 800, 400)
    

def draw_scene6():
    global oolong
    canvas.create_rectangle(0, 0, 1920, 150,
                                outline = "black", fill = "black",
                                width = 2)
    oolong = open_img(oolong_link, 500, 500, 800, 400)

def draw_next_screen():
    global scene_counter
    scene_counter += 1
    if scene_counter == 1:
        draw_scene1()
    elif scene_counter == 2:
        draw_scene2()
    elif scene_counter == 3:
        draw_scene3()
    elif scene_counter == 4:
        draw_scene4()
    elif scene_counter == 5:
        draw_scene6()

#################### Calling ####################
title()
btn = Button(win, text='Press to go to next scene', width=40,
             height=5, bd='10', command=draw_next_screen)
btn.place(x=650, y=700)

win.mainloop()
	
