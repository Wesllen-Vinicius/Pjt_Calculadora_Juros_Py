class CalculadoraJuros:
    def calcular_juros(self, valor_inicial, taxa_juros, tipo_juros, valor_mensal, periodo, tipo_periodo):
        if tipo_juros == 'Anual':
            taxa_juros /= 100.0  # Convertendo para decimal
            taxa_juros_mensal = (1 + taxa_juros) ** (1 / 12.0) - 1
        elif tipo_juros == 'Mensal':
            taxa_juros_mensal = taxa_juros / 100.0
        else:
            return None

        if tipo_periodo == 'Anos':
            periodo *= 12

        valor_final = valor_inicial
        for _ in range(int(periodo)):
            valor_final *= (1 + taxa_juros_mensal)
            valor_final += valor_mensal

        return valor_final
