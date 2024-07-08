import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.modelo import CalculadoraJuros

# Inicializa a calculadora fora das funções de teste para reutilização
calculadora = CalculadoraJuros()

def test_calculo_juros_anual():
    # Valor inicial: R$ 1000, Taxa de juros anual: 5%, Valor mensal: R$ 100, Período: 2 anos
    resultado = calculadora.calcular_juros(1000, 5, 'Anual', 100, 2, 'Anos')
    assert resultado == pytest.approx(1221.55, rel=1e-2)  # Verifica se o resultado é aproximadamente 1221.55

def test_calculo_juros_mensal():
    # Valor inicial: R$ 1500, Taxa de juros mensal: 1%, Valor mensal: R$ 50, Período: 6 meses
    resultado = calculadora.calcular_juros(1500, 1, 'Mensal', 50, 6, 'Meses')
    assert resultado == pytest.approx(1863.62, rel=1e-2)  # Verifica se o resultado é aproximadamente 1863.62

def test_calculo_juros_invalido():
    # Testa um cenário inválido: tipo de juros não reconhecido
    resultado = calculadora.calcular_juros(1000, 5, 'Trimestral', 100, 2, 'Anos')
    assert resultado is None  # Verifica se o resultado é None, indicando um tipo de juros inválido
