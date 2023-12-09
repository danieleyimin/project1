import tkinter as tk
from tkinter import scrolledtext
from project1_logic import CalculatorApp

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator GUI")

        operator_frame = tk.Frame(root)
        operator_frame.pack(pady=10)

        operator_label = tk.Label(operator_frame, text="Operator")
        operator_label.pack(side="left")

        self.operator_var = tk.StringVar()
        self.operator_var.set(None)  # Initialize to None (no selection)

        operator_add = tk.Radiobutton(operator_frame, text="Add", variable=self.operator_var, value="add")
        operator_subtract = tk.Radiobutton(operator_frame, text="Subtract", variable=self.operator_var, value="subtract")
        operator_multiply = tk.Radiobutton(operator_frame, text="Multiply", variable=self.operator_var, value="multiply")
        operator_divide = tk.Radiobutton(operator_frame, text="Divide", variable=self.operator_var, value="divide")
        operator_choose = tk.Radiobutton(operator_frame, text="Choose", variable=self.operator_var, value="choose")
        
        input_frame = tk.Frame(root)
        input_frame.pack(pady=5)

        input_label = tk.Label(input_frame, text="Input")
        input_label.pack(side="left", padx=5)
        self.input_entry = tk.Entry(input_frame)
        self.input_entry.pack()

        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()
        
        self.result_display = tk.Label(self.root, text="", pady=10)
        self.result_display.pack()

        operator_add.pack(side="left")
        operator_subtract.pack(side="left")
        operator_multiply.pack(side="left")
        operator_divide.pack(side="left")
        operator_choose.pack(side="left")

    def calculate(self):
        user_input = self.input_entry.get()

        try:
            operator = self.operator_var.get()
            values = [float(val) for val in user_input.split()]
        except ValueError:
            self.result_display.config(text="Invalid input. Please enter valid numbers.")
            return

        calculator_app = CalculatorApp(operator, values)
        try:
            result = calculator_app.calculate()
            self.result_display.config(text=f"Answer = {result:.2f}")
        except Exception as e:
            self.result_display.config(text=str(e))

if __name__ == "__main__":
    root = tk.Tk()
    calculator_gui = CalculatorGUI(root)
    root.mainloop()
