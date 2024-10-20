from tkinter import *
from PIL import Image, ImageTk
from asteval import Interpreter
import os
import sys

class Calculator:
    def __init__(self, root):
        # ... (rest of your code remains unchanged)

        pil_image = Image.open(os.path.join(image_path, "PENTHOUSE.png"))
        background_photo = ImageTk.PhotoImage(pil_image)  # Directly use ImageTk.PhotoImage

        background_label = Label(self.root, image=background_photo)
        background_label.image = background_photo
        background_label.pack(x=0, y=0, relwidth=1, relheight=1)
        self.root.resizable(width=False, height=False)

        self.MainFrame = Frame(self.root, bd=8, relief=RIDGE)
        self.MainFrame.place(relx=0.5, rely=0.15, anchor=CENTER)
        self.WidgetFrame = Frame(self.root, bd=8, relief=RIDGE)
        self.WidgetFrame.place(relx=0.5, rely=0.65, anchor=CENTER)

        self.entry = Entry(self.MainFrame, font=("Arial", 16), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        button_labels = [
            ("←", 1, 0), ("C", 1, 1), ("CE", 1, 2), ("±", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("+", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("*", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("÷", 5, 3)
        ]

        for label, row, col in button_labels:
            self.create_button(label, row, col)

        for i in range(6):
            self.WidgetFrame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.WidgetFrame.grid_columnconfigure(i, weight=1)

        self.input_button = ""
        self.aeval = Interpreter()

    def create_button(self, text, row, column):
        base_path = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(__file__)
        image_path = os.path.join(base_path, 'calculator/img')
        button_bg_image = Image.open(os.path.join(image_path, "wushang.png"))
        button_bg_photo = ImageTk.PhotoImage(button_bg_image)

        buttonWidget = Button(
            self.WidgetFrame,
            text=text,
            font=("Times New Roman", 14, "bold"),
            fg="white",
            bg="white",
            relief=RAISED,
            bd=2,
            image=button_bg_photo,
            compound='center',
            command=lambda text=text: self.button_click(text),
        )
        buttonWidget.image = button_bg_photo
        buttonWidget.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

    def button_click(self, text):
        if text == "←":
            self.input_button = self.input_button[:-1]
        elif text == "CE" or text == "C":
            self.input_button = ""
        elif text == "=":
            try:
                result = self.aeval(self.input_button)
                self.input_button = str(result)
            except Exception:
                self.input_button = "Error"
        elif text == "±":
            try:
                self.input_button = str(float(self.input_button) * -1)
            except Exception:
                self.input_button = "Error"
        else:
            self.input_button += text
        self.entry.delete(0, END)
        self.entry.insert(0, self.input_button)

if __name__ == "__main__":
    root = Tk()
    app = Calculator(root)
    root.mainloop()