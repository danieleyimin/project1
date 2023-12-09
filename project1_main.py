import tkinter as tk
from project1_gui import CalculatorGUI

def create_window():
    window = tk.Tk()
    window.title("Calculator app")
    window.geometry("500x300")
    return window

if __name__ == "__main__":
    window = create_window()
    calculator_gui = CalculatorGUI(window)
    window.mainloop()