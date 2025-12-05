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

---

# 🎨 UI - Interface Gráfica (Visão Geral)

O arquivo ``ui.py`` contém a classe ``CalculatorUI``, responsável por criar e gerenciar a interface gráfica da calculadora usando ``tkinter``.

## 🧱 Construção da Interface

```python
def __init__(self, controller):
    self.controller = controller
    
    self.window = tk.Tk()
    self.window.title("Calculadora POO")
    self.window.geometry("300x380")
```

✅ ``self.controller = controller``

Armazena referência ao Controller para poder chamar ``process_operation()`` quando necessário.

✅ ``self.window = tk.Tk()``

Cria a janela principal da aplicação.

✅ ``self.window.title()`` e ``self.window.geometry()``

Define o título e o tamanho da janela (300x380 pixels).

---

## 📺 Display da Calculadora

```python
self.display = tk.Entry(self.window, font=("Arial", 20), justify="right")
self.display.pack(fill="both", padx=10, pady=10)
```

✅ ``tk.Entry`` 

Cria um campo de texto onde o usuário vê os números e operações digitadas.

✅ ``justify="right"`` 

Alinha o conteúdo à direita, como em calculadoras reais.

✅ ``pack(fill="both", padx=10, pady=10)`` 

Posiciona o display com espaçamento de 10 pixels.

---

## 🔘 Criação dos Botões

```python
def create_buttons(self):
    buttons = [
        ["7", "8", "9", "÷"],
        ["4", "5", "6", "×"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
    ]
```

✅ A matriz ``buttons`` define a **posição e símbolo de cada botão**.

✅ Cada linha é um ``tk.Frame`` (linha da calculadora).

✅ Cada botão é um ``tk.Button`` com:
- ``text``: o símbolo exibido
- ``width=5, height=2``: tamanho do botão
- ``font=("Arial", 16)``: fonte e tamanho
- ``command=lambda t=text: self.on_button_click(t)``: função chamada ao clicar

---

## ⌨️ Tratamento de Cliques nos Botões

```python
def on_button_click(self, value):
    if value == "=":
        self.calculate()
    else:
        self.display.insert(tk.END, value)
```

✅ Se o botão clicado é ``"="``:

Chama o método ``calculate()`` para processar a expressão.

✅ Caso contrário:

Insere o símbolo no display (números e operadores).

**Exemplo de fluxo:**

1. Usuário clica ``"3"`` → insere ``"3"`` no display
2. Usuário clica ``"×"`` → insere ``"×"`` no display (agora mostra ``"3×"``)
3. Usuário clica ``"4"`` → insere ``"4"`` no display (agora mostra ``"3×4"``)
4. Usuário clica ``"="`` → chama ``calculate()``

---

## 🧮 Método de Cálculo

```python
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
```

✅ ``self.display.get()``

Obtém o texto digitado no display.

✅ ``expression.replace('×', '*').replace('÷', '/')``

Converte os símbolos visuais para operadores Python reconhecidos.

✅ ``eval(expression)``

Avalia a expressão matemática (ex: ``"3*4"`` → ``12``).

✅ Atualiza o display com o resultado.

✅ Se ocorrer erro → mostra ``"Erro"``.

---

## ▶️ Executar a Interface

```python
def run(self):
    self.window.mainloop()
```

✅ ``mainloop()`` 

Inicia o loop da interface gráfica, deixando a janela aberta e respondendo aos cliques do usuário.

---

## 🎯 RESUMÃO DA UI

>A classe ``CalculatorUI`` cria a janela gráfica com um display e botões.
>Cada botão inserido no display mostra o símbolo clicado.
>Quando ``"="`` é clicado, a expressão é convertida e avaliada.
>O resultado é mostrado no display ou um erro é exibido.

---

# 🚀 Main - Iniciador do Projeto

O arquivo ``main.py`` é o **ponto de entrada** do programa. É aqui que tudo começa.

```python
from ui import CalculatorUI
from controller import Controller

def main():
    ui = CalculatorUI(None)
    controller = Controller(ui)
    ui.controller = controller
    ui.run()

if __name__ == "__main__":
    main()
```

---

## 🧱 Entendendo a Inicialização

### 1️⃣ Criar a Interface

```python
ui = CalculatorUI(None)
```

Cria a janela da calculadora. Passamos ``None`` porque ainda não temos o Controller.

### 2️⃣ Criar o Controller

```python
controller = Controller(ui)
```

Cria o Controller, passando a interface como referência.

### 3️⃣ Conectar o Controller à Interface

```python
ui.controller = controller
```

Agora a interface tem acesso ao Controller para processar operações.

### 4️⃣ Iniciar a Interface

```python
ui.run()
```

Chama ``mainloop()`` e mantém a janela aberta.

---

## 🔄 Fluxo Completo do Programa

```
main()
  ↓
Cria CalculatorUI (janela aparece)
  ↓
Cria Controller (calculadora "real" é instanciada)
  ↓
Conecta os dois objetos
  ↓
ui.run() inicia o mainloop
  ↓
Usuário clica em "3"
  ↓
on_button_click("3") → insere "3" no display
  ↓
Usuário clica em "×"
  ↓
on_button_click("×") → insere "×" no display
  ↓
Usuário clica em "4"
  ↓
on_button_click("4") → insere "4" no display
  ↓
Usuário clica em "="
  ↓
calculate() → normaliza "3×4" para "3*4"
  ↓
eval("3*4") = 12
  ↓
Display mostra "12"
```

---

## 🎯 RESUMÃO DO MAIN

>``main.py`` é o arquivo que você executa para iniciar o programa.
>Ele cria a interface, o controller e conecta tudo.
>Depois chama ``ui.run()`` para manter a janela aberta.
>É o **maestro** que orquestra todo o projeto.

---

# 🏗️ Arquitetura Completa do Projeto

```
main.py (Iniciador)
   ↓
   ├─→ CalculatorUI (ui.py) - Interface Gráfica
   │        ↓
   │    Botões → Exibe números/operadores no display
   │        ↓
   │    Clica "=" → Chama calculate()
   │
   └─→ Controller (controller.py) - Intermediário
            ↓
        process_operation(op, x, y)
            ↓
        Calculator (calculator.py) - Operações Reais
            ↓
        Retorna resultado → UI mostra no display
```

---

## 🎓 Padrão de Design Utilizado

Este projeto segue o padrão **MVC (Model-View-Controller)**:

- **Model** (``calculator.py``): Lógica pura de cálculo
- **View** (``ui.py``): Interface gráfica (o que o usuário vê)
- **Controller** (``controller.py``): Intermediário que conecta View e Model

Isso torna o código:
- ✅ **Modular**: cada parte tem responsabilidade própria
- ✅ **Reutilizável**: Calculator pode ser usada em outra interface
- ✅ **Testável**: cada componente pode ser testado isoladamente
- ✅ **Mantível**: fácil de entender e modificar

---

# ✅ Projeto Concluído!

Agora você tem uma calculadora funcional que:
- ✅ Realiza operações básicas (``+``, ``-``, ``×``, ``÷``)
- ✅ Calcula raiz quadrada (``√``) e potência (``^``)
- ✅ Trata erros (divisão por zero, entradas inválidas)
- ✅ Tem interface gráfica amigável
- ✅ Segue princípios de POO e padrões de design

**Para executar:**
```bash
python main.py
```

Aproveite sua calculadora! 🎉