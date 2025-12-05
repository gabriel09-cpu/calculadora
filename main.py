from ui import CalculatorUI
from controller import Controller

def main():
    ui = CalculatorUI(None)
    controller = Controller(ui)
    ui.controller = controller
    ui.run()

if __name__ == "__main__":
    main()
