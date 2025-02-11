import tkinter as tk

# Window settings
W_TITLE = "Password Manager"
W_PADX = 20
W_PADY = 20

# BGR image path
BGR_IMAGE = "logo.png"

# Canvas settings
C_WIDTH = 200
C_HEIGHT = 200

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(W_TITLE)
        self.window.config(padx=W_PADX, pady=W_PADY)

        self.bgr_image = tk.PhotoImage(file=BGR_IMAGE)

        self.canvas = tk.Canvas(width=C_WIDTH, height=C_HEIGHT, highlightthickness=0)
        self.canvas.create_image(C_WIDTH / 2, C_HEIGHT / 2, image=self.bgr_image)

        self.canvas.grid(row=0, column=0)
