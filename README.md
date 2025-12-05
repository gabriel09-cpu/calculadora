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

## 🎯 Resumo da lógica

Em poucas frases:

>A classe ``Calculator`` é um objeto que centraliza todas as operações matemáticas.
>Cada método representa uma função matemática específica.
>O método recebe entradas (``x, y``) e devolve um resultado.
>``math`` é usado para operações mais precisas e avançadas.

----------------------------------------------------------------
# Controller - Visão Geral

O ``Controller`` é a ponte entre:
- a interface gráfica (``ui``)
- a calculador de verdade(``Calculator``)

Ele recebe:
- qual operação o usuário escolheu (``op``)
- os valores digitados (``x`` e ``y``)
- e decide qual função da calculadora deve chamar
----------------------------------------------------------------
### 🧱 Construção do Controller

```python
def __init__(self, ui):
    self.calc = Calculator()
    self.ui = ui
```

✅ O Controller cria uma instância da calculadora real: 
``self.calc = Calculator()``

Assim, ele pode chamar métodos como: 

- ``self.calc.add()``
- ``self.calc.division()``
- ``self.calc.square_root()``
- etc.

✅Ele também guarda a interface (``ui``), caso precise atualizar o display.
----------------------------------------------------------------
### Método de Processamento de Operações

```python
def process_operation(self, op, x, y=None):
```

Quando a ``ui`` manda algo:

- operação:``+``
- valor1: ``10``
- valor2: ``5``

O controller recebe esses dados nele, e ``y=None``, deixa claro que **algumas operações só usam o elemento ``x``**(radiciação por exemplo).
--------------------------------------------------------------------

### Convertendo strings para números reais

```python 
x = float(x)
if y is not None:
    y = float(y)
```

Quando os valores vem da interface, eles vem como ``string`` e a função acima, os transforma de ``string`` para ``float``  o que permite que o calculo seja efetuado. 

Exemplo: 

- "10" => 10.0
- "4.7" => 4.7

Por isso a conversão é obrigatória. Se caso o usuario informar uma letra por exemplo, é mostrado o ``ValueError``, que no final será tratado.

### O “switch-case manual” das operações

Python não tem ``switch-case``, então usamos ``if / elif``.

```python
if op == "+":
    return self.calc.add(x, y)
```

O significado:

> “Se a operação recebida é +, chame o método de soma da classe Calculator.”

Assim para cada operação.

### Tratamento de erros

```python
except ValueError:
    return "Erro"
```
Se ocorrer qualquer erro de conversão:

- ``float("abc")``

- divisão inválida

- raiz de número negativo (em alguns casos)

o controller retorna "Erro" para a interface mostrar no display.

------------------------------------------

## 🎯 RESUMÃO DA LÓGICA

>O Controller recebe dados da UI, transforma esses dados, decide qual cálculo deve ser feito, chama o método correto da classe Calculator e retorna o resultado.
>Se qualquer coisa der errado, devolve "Erro".

Ele é literalmente o cérebro que traduz comandos da interface em cálculos reais.