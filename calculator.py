import math


class Calculator:  
    
    def  __init__(self):
        self.result = 0
    
    def add(self, x, y): # Soma 
        return x + y
    def substract(self, x, y): # Subtração
        return x - y 
    def multiply(self, x, y): # Multiplicação
        return x * y
    def division(self, x, y): # Divisão
        if y == 0:
            raise ValueError("Erro")
        return x / y
    def square_root(self, x): # Raiz Quadrada
        return math.sqrt(x)
    def power(self, x, y):
        return math.pow(x, y)


# calcular = Calculator()
# resultado = calcular.add(100, 100)
# print(resultado)