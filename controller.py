from calculator import Calculator

class COntroller:
    def __init__(self, ui):
        self.calc = Calculator()
        self.ui = ui 
    def process_operation(self, op, x, y=None):
        try: 
            x = float(x)
            if y is not None:
                y = float(y)
            if op == "+":
                return self.calc.add(x, y)
            elif op == "-":
                return self.calc.substract(x, y)
            elif op == "x":
                return self.calc.multiply(x, y)
            elif op == "÷":
                return self.calc.division(x, y)
            elif op == "√":
                return self.calc.square_root(x)
            elif op == "^":
                return self.calc.power(x, y)
        except ValueError:
            return "Erro"