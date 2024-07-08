import tkinter as tk
from tkinter import ttk
from model.modelo import CalculadoraJuros
from view.view import CalculadoraJurosView

class CalculadoraJurosController:
    def __init__(self, root):
        self.root = root
        self.model = CalculadoraJuros()
        self.view = CalculadoraJurosView(self.root, self.calcular_juros)

    def calcular_juros(self, valor_inicial, taxa_juros, tipo_juros, valor_mensal, periodo, tipo_periodo):
        return self.model.calcular_juros(valor_inicial, taxa_juros, tipo_juros, valor_mensal, periodo, tipo_periodo)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraJurosController(root)
    root.mainloop()
