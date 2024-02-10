import tkinter as tk
from .components.authtab import AuthenticationTab as Tab
from .components.maintab import MainTab


# Running function for the Gui Application
def run_gui():
    root = tk.Tk()
    #Tab(root)
    MainTab(root)
    root.mainloop()
