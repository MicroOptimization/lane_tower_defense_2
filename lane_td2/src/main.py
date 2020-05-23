"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""
import tkinter as tk
from tkinter import Canvas, PhotoImage
from copy import deepcopy


debugging = True


root = tk.Tk()

window_width = 1000
window_height = 700


canvas = Canvas(root, width=window_width, height=window_height)
canvas.pack()

grid = []
row = []



def fill_grid_with_default_vals():
    for i in range(9):
        row.append(0)
    
    for i in range(6):
        grid.append(deepcopy(row))

fill_grid_with_default_vals()

def print_grid_status():
    for i in range(len(grid)):
        for j in range(len(row)):
            print(grid[i][j],end=" ")
        print()
if debugging:       
    print_grid_status()


xoffset = 125
yoffset = 200
"""
img = PhotoImage(file='sprites/sprite_bg_grass.png')

for i in range(len(grid)):
    for j in range(len(row)):
        canvas.create_image(j * 76 + xoffset, i * 76 + yoffset, image=img)
"""


sprites = []

def draw_lawn():
    img = PhotoImage(file='sprites/sprite_bg_grass.png')
    canvas.image = img
    sprites.append(img)
    for i in range(len(grid)):
        for j in range(len(row)):
            canvas.create_image(j * 76 + xoffset, i * 76 + yoffset, image=img, anchor="center")
    
    

def draw_turret_on_grid(turret_id, gridx, gridy):
    path = 'sprites/sprite_' + turret_id + '.png'
    img = PhotoImage(file=path)
    canvas.image = img
    sprites.append(img)
    canvas.create_image(gridx * 76 + xoffset, gridy * 76 + yoffset, image=img)
    
draw_lawn()

for i in range(6):
    draw_turret_on_grid("a2", 0, i)
    draw_turret_on_grid("a1", 1, i)
 



palette_turrets = []
palette_turrets = ["a1", "a2", "a3"]


palette_sprites = [] #keeps reference to the sprites



def draw_palette():
    
    palette_dim = 75
    palette_start = 50
    palette_end = palette_start + palette_dim # = 125
    palette_size = 10
    
    canvas.create_rectangle(xoffset, palette_start, window_width - xoffset, palette_end, fill="#848482")
    
    for i in range(palette_size):
        canvas.create_line(i * palette_dim + xoffset, palette_start, i * palette_dim + xoffset, palette_end)
        
    for i in range(len(palette_turrets)):
        path = 'sprites/sprite_' + palette_turrets[i] + '.png'
        
        img = PhotoImage(file=path)
        canvas.image = img
        palette_sprites.append(img)
        
        #canvas.create_image(gridx * 76 + xoffset, gridy * 76 + yoffset, image=img)
        #canvas.create_line(i * palette_dim + xoffset, palette_start, i * palette_dim + xoffset, palette_end)
        canvas.create_image(i * palette_dim + xoffset, palette_start, image=img, anchor="nw")
        
draw_palette()

def draw_stuff():
    draw_palette()
    draw_lawn()
    for i in range(6):
        draw_turret_on_grid("a2", 0, i)
        draw_turret_on_grid("a1", 1, i)
class Game(tk.Frame):
    
    cid = 10 #Click indicator diameter
    cic = 1 #click indicator circle #placeholder val
    cric = 1 #click release indicator circle #placeholder val
    
    def key(self, event):
        print("pressed", repr(event.char))

    def click(self, event):
        
        canvas.delete("all")
        draw_stuff()
        if debugging:
            print("clicked at", event.x, event.y)
            canvas.create_oval(event.x - self.cid, event.y - self.cid, event.x + self.cid, event.y + self.cid, fill="white")
        
        
        
    def release(self, event):
        
        if debugging:
            print("released at", event.x, event.y)
            canvas.create_oval(event.x - self.cid, event.y - self.cid, event.x + self.cid, event.y + self.cid, fill="black")
        
    def __init__(self, master=None):    
        canvas.bind("<Key>", self.key)
        canvas.bind("<Button-1>", self.click)
        canvas.bind("<ButtonRelease-1>", self.release)
    
game = Game(master=root)



continuing_game_loop = True
while continuing_game_loop:
    try:
        root.update_idletasks()
        root.update()
    except:
        print()
        print("Excepted")
        continuing_game_loop = False