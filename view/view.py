import tkinter
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CalculadoraJurosView:
    def __init__(self, root, calcular_callback):
        self.root = root
        self.calcular_callback = calcular_callback

        self.setup_ui()

    def setup_ui(self):
        self.root.title("Calculadora de Juros")

        input_frame = ttk.Frame(self.root, padding="20")
        input_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(input_frame, text="Valor Inicial (R$):").grid(row=0, column=0, sticky="w")
        self.valor_inicial_entry = ttk.Entry(input_frame)
        self.valor_inicial_entry.grid(row=0, column=1)

        ttk.Label(input_frame, text="Taxa de Juros (%):").grid(row=1, column=0, sticky="w")
        self.taxa_juros_entry = ttk.Entry(input_frame)
        self.taxa_juros_entry.grid(row=1, column=1)

        ttk.Label(input_frame, text="Tipo de Juros:").grid(row=2, column=0, sticky="w")
        self.tipo_juros_combobox = ttk.Combobox(input_frame, values=['Anual', 'Mensal'])
        self.tipo_juros_combobox.grid(row=2, column=1)
        self.tipo_juros_combobox.current(0)

        ttk.Label(input_frame, text="Valor Mensal (R$):").grid(row=3, column=0, sticky="w")
        self.valor_mensal_entry = ttk.Entry(input_frame)
        self.valor_mensal_entry.grid(row=3, column=1)

        ttk.Label(input_frame, text="Período:").grid(row=4, column=0, sticky="w")
        self.periodo_entry = ttk.Entry(input_frame)
        self.periodo_entry.grid(row=4, column=1)

        ttk.Label(input_frame, text="Tipo de Período:").grid(row=5, column=0, sticky="w")
        self.tipo_periodo_combobox = ttk.Combobox(input_frame, values=['Anos', 'Meses'])
        self.tipo_periodo_combobox.grid(row=5, column=1)
        self.tipo_periodo_combobox.current(0)

        calcular_button = ttk.Button(input_frame, text="Calcular", command=self.calcular)
        calcular_button.grid(row=6, columnspan=2, pady=10)

        resultado_frame = ttk.Frame(self.root, padding="20")
        resultado_frame.grid(row=1, column=0, sticky="nsew")

        ttk.Label(resultado_frame, text="Resultados:", font=("Arial", 14, "bold")).grid(row=0, column=0, pady=10, sticky="w")

        ttk.Label(resultado_frame, text="Valor Total Final:").grid(row=1, column=0, sticky="w")
        self.valor_final_label = ttk.Label(resultado_frame, text="")
        self.valor_final_label.grid(row=1, column=1, sticky="w")

        ttk.Label(resultado_frame, text="Valor Total Investido:").grid(row=2, column=0, sticky="w")
        self.valor_investido_label = ttk.Label(resultado_frame, text="")
        self.valor_investido_label.grid(row=2, column=1, sticky="w")

        ttk.Label(resultado_frame, text="Total em Juros:").grid(row=3, column=0, sticky="w")
        self.total_juros_label = ttk.Label(resultado_frame, text="")
        self.total_juros_label.grid(row=3, column=1, sticky="w")

        # Frame para o gráfico
        grafico_frame = ttk.Frame(self.root, padding="20")
        grafico_frame.grid(row=2, column=0, sticky="nsew")

        self.fig, self.ax = plt.subplots(figsize=(8, 4))
        self.ax.set_xlabel('Período')
        self.ax.set_ylabel('Valor acumulado')

        self.canvas = FigureCanvasTkAgg(self.fig, master=grafico_frame)
        self.canvas.get_tk_widget().pack()

    def calcular(self):
        valor_inicial = float(self.valor_inicial_entry.get())
        taxa_juros = float(self.taxa_juros_entry.get())
        tipo_juros = self.tipo_juros_combobox.get()
        valor_mensal = float(self.valor_mensal_entry.get())
        periodo = float(self.periodo_entry.get())
        tipo_periodo = self.tipo_periodo_combobox.get()

        resultado = self.calcular_callback(valor_inicial, taxa_juros, tipo_juros, valor_mensal, periodo, tipo_periodo)

        if resultado is not None:
            valor_total_final = resultado
            valor_total_investido = valor_inicial + valor_mensal * periodo
            total_juros = valor_total_final - valor_total_investido

            self.valor_final_label.config(text=f"R$ {valor_total_final:.2f}")
            self.valor_investido_label.config(text=f"R$ {valor_total_investido:.2f}")
            self.total_juros_label.config(text=f"R$ {total_juros:.2f}")

            # Gerar dados para o gráfico
            valores_acumulados = []
            valor_acumulado = valor_inicial
            valores_acumulados.append(valor_acumulado)

            if tipo_juros == 'Anual':
                taxa_juros /= 100
                taxa_juros_mensal = (1 + taxa_juros) ** (1 / 12) - 1
            elif tipo_juros == 'Mensal':
                taxa_juros /= 100
                taxa_juros_mensal = taxa_juros

            if tipo_periodo == 'Anos':
                periodo *= 12

            for _ in range(int(periodo)):
                valor_acumulado *= (1 + taxa_juros_mensal)
                valor_acumulado += valor_mensal
                valores_acumulados.append(valor_acumulado)

            # Atualizar gráfico
            self.ax.clear()
            self.ax.plot(range(len(valores_acumulados)), valores_acumulados, marker='o', linestyle='-')
            self.ax.set_xlabel('Período')
            self.ax.set_ylabel('Valor acumulado')
            self.canvas.draw()

        else:
            self.valor_final_label.config(text="")
            self.valor_investido_label.config(text="")
            self.total_juros_label.config(text="Opção inválida para o tipo de juros. Use 'Anual' ou 'Mensal'.")
