import tkinter as tk

class CalculatorUI:
    def __init__(self, controller):
        self.controller = controller
        
        self.window = tk.Tk()
        self.window.title("Calculadora POO")
        self.window.geometry("300x380")

        # Display
        self.display = tk.Entry(self.window, font=("Arial", 20), justify="right")
        self.display.pack(fill="both", padx=10, pady=10)

        # Botões
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        frame = tk.Frame(self.window)
        frame.pack()

        for row in buttons:
            line = tk.Frame(frame)
            line.pack()
            for text in row:
                btn = tk.Button(
                    line,
                    text=text,
                    width=5,
                    height=2,
                    font=("Arial", 16),
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.pack(side="left", padx=3, pady=3)

    def on_button_click(self, value):
        if value == "=":
            self.calculate()
        else:
            self.display.insert(tk.END, value)

    def calculate(self):
        expression = self.display.get()

        # Normaliza símbolos para o Python (× -> *, ÷ -> /)
        expression = expression.replace('×', '*').replace('÷', '/')

        # Super simples: só soma/sub/mult/div
        try:
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Erro")

    def run(self):
        self.window.mainloop()
