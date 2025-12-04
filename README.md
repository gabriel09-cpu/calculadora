# Projeto Calculadora 

Olá, fiz esse projeto para aperfeiçoar meus conhecimentos em python e também para aprender coias novas. Esse é meu primeiro projeto pessoal, que tem por objetivo construir uma calculadora básica em python, usando: Orientação a Objetos e as bibliotecas ``math`` e ``tkinter``. 


## Estrutura do Projeto:
````bash
calculadora/
│
├── main.py            
├── controller.py       
├── calculator.py        
├── ui.py                
└── utils.py             
````


# 🧠Calculator - Visão Geral

O arquivo ``calculator.py`` tem a classe pai ``Calculator``, que é um modelo de uma calculadora real, que efetua calculos com dois termos ``x`` e ``y``.

- A classe representa um **objeto calculadora**.
- Cada função dentro dela representa uma **operação que a calculadora sabe fazer**.
- Usei ``math`` para funções matemáticas mais avançadas.
---------------------------------------

# 🔍 Entendendo a Lógica do Projeto

Olhando o código: 

```python 
import math

class Calculator:
    def __init__(self):
        self.result = 0
```

✅ ``class Calculator:``
Define uma **classe**, ou seja, molde para criar objetos calculadora.

✅ ``__init__``
Método chamado quando a calculadora é criada.

✅``self.result = 0`` 
Cria um atributo interno para guardar o último resultado (mesmo que ainda não vá ser usado, é útil para expasões)
________________________________________

## Métodos básicos de operação
Cada método tem a mesma estrutura:
```python
def add(self, x, y):
    return x + y
```
#### **❔Porque ``self``?**
``self`` é a referencia ao objeto>
Permite basicamente que a gente use atributos da calculara.

#### **❔Porque que dois parâmetros?**
Porque operações como soma, subtração etc. precisam de dois números: ``x`` e ``y``.

**📌 add**
````python
return x + y
````

A função simplesmente devolve o resultado da soma.

**📌 subtract**
```python
return x - y
```

Retorna a subtração direta.

**📌 multiply**

```python
return x * y
```
**📌 divide**

```python
def divide(self, x, y):
    if y == 0:
        raise ValueError("Divisão por zero")
    return x / y
```

✔ Lógica importante aqui:

1. Verifica se o divisor (y) é 0

2. Se for, interrompe a execução e gera um erro intencional

3. Se não for 0 → realiza a divisão

4. Isso evita que sua calculadora quebre com erros inesperados.

**🧮 Funções usando math** 

Agora a parte que usa a biblioteca matemática.

**📌 Raiz quadrada**
```python def square_root(self, x):
    return math.sqrt(x)
```
✔ math.sqrt(x)

Calcula a raiz quadrada

mais rápido e confiável que (x ** 0.5)

**📌 Potência**
```python
def power(self, x, y):
    return math.pow(x, y)
```
✔ math.pow(x, y)

1. faz x elevado a y

2. funciona bem com floats

3. retorna sempre float

#### **🧱 Por que fazer assim?**

Esse código segue os princípios da POO:

**✔ 1. Encapsulamento**

Todas as operações matemáticas ficam dentro da classe.

**✔ 2. Reusabilidade**

Se a calculadora for usada na interface Tkinter, basta chamar:

```python
resultado = calc.add(2, 3)
```