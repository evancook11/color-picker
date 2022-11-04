import sys
import tkinter as tk
from pynput import mouse

WINDOW_WIDTH, WINDOW_HEIGHT = 600, 400
BG_COLOR = "#D4E2EC"


if __name__ == '__main__':

    mouse_controller = mouse.Controller()
    color_hexcode = "#FFFFFF"

    # sets up window
    window = tk.Tk() 
    window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT) 
    window.title("Color Selector")
    window.config(bg=BG_COLOR)

    # creates canvas to display selected color
    color_canvas = tk.Canvas(window, bg="blue", height=300, width=300, bd=0, highlightthickness=0)  
    color_canvas.pack(expand=True, padx=20, pady=20)

    # creates label to read off the selected color
    color_label = tk.Label(window, text=f"Color hexcode: {color_hexcode}", bg=BG_COLOR, font=('none 12 bold'), fg='black')
    color_label.pack(padx=20, pady=20)

    # creates button to copy to clipboard (does nothing currently)
    submit_btn = tk.Button(window, text="Copy hexcode to clipboard", background=BG_COLOR, activebackground=BG_COLOR)
    submit_btn.pack(padx=20, pady=20)

    window.mainloop()