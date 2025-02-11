import tkinter as tk

# Window settings
W_TITLE = "Password Manager"
W_PADX = 40
W_PADY = 40

# BGR image path
BGR_IMAGE = "logo.png"

# Canvas settings
C_WIDTH = 200
C_HEIGHT = 200

# Grid settings
G_PADX = 5
G_PADY = 5

# Labels settings
L_WEBSITE_TEXT = "Website:"
L_EMAIL_TEXT = "Email/Username:"
L_PASSWD_TEXT = "Password:"
L_FONT = ("Arial", 14, "normal")

# Entries settings
E_WEBSITE_WIDTH = 50
E_EMAIL_WIDTH = E_WEBSITE_WIDTH
E_PASSWD_WIDTH = 25

# Buttons settings
B_GEN_PASSWD_TEXT = "Generate Password"
B_ADD = "Add"
B_ADD_WIDTH = 36
B_FONT = ("Arial", 14, "normal")

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(W_TITLE)
        self.window.config(padx=W_PADX, pady=W_PADY)

        self.bgr_image = tk.PhotoImage(file=BGR_IMAGE)

        self.canvas = tk.Canvas(width=C_WIDTH, height=C_HEIGHT, highlightthickness=0)
        self.canvas.create_image(C_WIDTH / 2, C_HEIGHT / 2, image=self.bgr_image)

        self.website_label = tk.Label(text=L_WEBSITE_TEXT, font=L_FONT)
        self.email_label = tk.Label(text=L_EMAIL_TEXT, font=L_FONT)
        self.password_label = tk.Label(text=L_PASSWD_TEXT, font=L_FONT)

        self.website_entry = tk.Entry(width=E_WEBSITE_WIDTH)
        self.email_entry = tk.Entry(width=E_EMAIL_WIDTH)
        self.password_entry = tk.Entry(width=E_PASSWD_WIDTH)

        self.gen_passwd_btn = tk.Button(text=B_GEN_PASSWD_TEXT, font=B_FONT)
        self.add_btn = tk.Button(text=B_ADD, width=B_ADD_WIDTH, font=B_FONT)

        self.canvas.grid(row=0, column=1, padx=G_PADX, pady=G_PADY)
        self.website_label.grid(row=1, column=0, padx=G_PADX, pady=G_PADY)
        self.email_label.grid(row=2, column=0, padx=G_PADX, pady=G_PADY)
        self.password_label.grid(row=3, column=0, padx=G_PADX, pady=G_PADY)
        self.website_entry.grid(row=1, column=1, columnspan=2, padx=G_PADX, pady=G_PADY)
        self.email_entry.grid(row=2, column=1, columnspan=2, padx=G_PADX, pady=G_PADY)
        self.password_entry.grid(row=3, column=1, padx=G_PADX, pady=G_PADY)
        self.gen_passwd_btn.grid(row=3, column=2, padx=G_PADX, pady=G_PADY)
        self.add_btn.grid(row=4, column=1, columnspan=2, padx=G_PADX, pady=G_PADY)
