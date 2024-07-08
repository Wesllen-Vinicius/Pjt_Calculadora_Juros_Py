import tkinter as tk
from controller.controller import CalculadoraJurosController

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraJurosController(root)
    root.mainloop()
