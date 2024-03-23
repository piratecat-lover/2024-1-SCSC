import tkinter as tk
from PIL import Image, ImageTk
import json
import os

def display_scene(config_file):
    # Load scene information from JSON configuration file
    with open(config_file, 'r') as f:
        scene_info = json.load(f)
    # Create Tkinter window
    root = tk.Tk()
    root.title("Dating Sim")

    # Load and display background image
    background_img = Image.open(scene_info['background_image'])
    background_img = background_img.resize((800, 600))  # Adjust size as needed
    background_photo = ImageTk.PhotoImage(background_img)
    background_label = tk.Label(root, image=background_photo)
    background_label.pack()

    # Load and display character image
    character_img = Image.open(scene_info['character_image'])
    character_img = character_img.resize((200, 300))  # Adjust size as needed
    character_photo = ImageTk.PhotoImage(character_img)
    character_label = tk.Label(root, image=character_photo)
    character_label.place(x=50, y=100)  # Adjust position as needed

    # Display dialogue and dialogue options
    dialogue_text = scene_info['dialogue']
    dialogue_label = tk.Label(root, text=dialogue_text, wraplength=700)
    dialogue_label.place(x=100, y=400)  # Adjust position as needed

    # Display dialogue options
    for i, option in enumerate(scene_info['dialogue_options']):
        option_label = tk.Label(root, text=f"{i+1}. {option}")
        option_label.place(x=100, y=430 + i*30)  # Adjust position as needed

    root.mainloop()

# Example usage

config_file = './src/scene1.json'
display_scene(config_file)