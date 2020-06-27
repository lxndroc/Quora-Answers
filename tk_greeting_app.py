# Repeated greeting example
# @lxndroc 2020

import tkinter as tk

class GreetingApp:
    def __init__(self):
        self.init_window()
        self.init_components()
        self.window.mainloop()

    def init_window(self):
        self.window = tk.Tk()
        self.window.title("Tkinter Greeting App")
        self.window.geometry("300x300")

    def init_components(self):
        self.hello_label = tk.Label(self.window, text="Hello example\n\nPlease enter your name below\n& press the Hello button\n")
        self.name_entry = tk.Entry(self.window)
        self.name_entry.insert(0, "Name")
        self.hello_button = tk.Button(self.window, text="Hello", command = self.say_hello)
        self.hello_name_label = tk.Label(self.window, text="\n\n")
        self.quit_button = tk.Button(self.window, text="Quit", fg="red", command=quit)
        self.hello_label.pack()
        self.name_entry.pack()
        self.hello_button.pack()
        self.hello_name_label.pack()
        self.quit_button.pack()

    def say_hello(self):
        name = self.name_entry.get()
        self.hello_name_label.configure(text=f"\nHello {name}!\n")    

GreetingApp()
