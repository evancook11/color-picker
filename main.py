import sys
import tkinter as tk
import pyautogui as pg

WINDOW_WIDTH, WINDOW_HEIGHT = 600, 400
BG_COLOR = "#D4E2EC"
REFRESH_TIME = 100


if __name__ == '__main__':
    def rgb_to_hex(r, g, b):
        return '#' + ('{:X}{:X}{:X}').format(r, g, b)

    def get_coords():
        global mouse_x
        global mouse_y
        mouse_x, mouse_y = pg.position()
        window.after(REFRESH_TIME, get_coords)

    def get_pixel(x, y):
        global color_hexcode
        im = pg.screenshot()
        color_hexcode = im.getpixel((x, y))
        color_hexcode = rgb_to_hex(int(color_hexcode[0]), int(color_hexcode[1]), int(color_hexcode[2]))
        color_label.config(text=f"Color hexcode: {color_hexcode}")
        color_canvas.config(bg=color_hexcode)
        window.after(REFRESH_TIME, get_pixel, mouse_x, mouse_y)


    mouse_x, mouse_y = 0, 0
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


    get_coords()
    get_pixel(mouse_x, mouse_y)
    window.mainloop()