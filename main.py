import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw() # hide main window

month = simpledialog.askinteger("Input", "Enter month (1-12):")