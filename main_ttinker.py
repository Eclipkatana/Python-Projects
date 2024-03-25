import tkinter as tk
from currency_GUI_ttinker import Currency_GUI
from base_GUI_ttinker import BaseGui

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Main Program")

        self.label = tk.Label(self, text="This is the main window")
        self.label.pack()

        self.Currency_converter_button = tk.Button(self, text="Currency Converter", command=self.show_next_gui)
        self.Currency_converter_button.pack()

        self.Currency_Test_button = tk.Button(self, text="Test", command=self.show_Test_gui)
        self.Currency_Test_button.pack()

        self.GUIs = [Test_GUI, Currency_GUI]  # List of different GUI classes

    def show_Test_gui(self):
        Test_gui = self.GUIs[0]
        Test_gui(self).show()
        
        
    def show_next_gui(self):
        currency_gui = self.GUIs[1]
        currency_gui(self).show()

# class BaseGui(tk.Toplevel):
#     def __init__(self, master=None):
#         tk.Toplevel.__init__(self, master)

#     def show(self):
#         self.grab_set()
#         self.wait_window()

# class currency_GUI(BaseGui):
#     def __init__(self, master=None):
#         BaseGui.__init__(self, master)

#         self.title("Currency Converter GUI")

#         self.label = tk.Label(self, text="This is GUI 1")
#         self.label.pack()

class Test_GUI(BaseGui):
    def __init__(self, master=None):
        BaseGui.__init__(self, master)

        self.title("Test GUI")

        self.label = tk.Label(self, text="This is Test GUI")
        self.label.pack()
        
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
