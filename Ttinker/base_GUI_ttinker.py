import tkinter as tk

class BaseGui(tk.Toplevel):
    def __init__(self, master=None):
        tk.Toplevel.__init__(self, master)

    def show(self):
        self.grab_set()
        self.wait_window()