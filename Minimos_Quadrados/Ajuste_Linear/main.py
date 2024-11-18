import numpy as np
from tabulate import tabulate

def least_squares_fit(x_data, y_data):
    """Calcula os coeficientes a e b do ajuste linear y = ax + b usando mínimos quadrados."""
    n = len(x_data)
    if n != len(y_data):
        raise ValueError("Os vetores x e y devem ter o mesmo tamanho.")
    
    # Cálculos intermediários
    x_mean = np.mean(x_data)
    y_mean = np.mean(y_data)
    xy_mean = np.mean(x_data * y_data)
    x2_mean = np.mean(x_data ** 2)
    
    # Coeficientes da reta
    a = (xy_mean - x_mean * y_mean) / (x2_mean - x_mean ** 2)
    b = y_mean - a * x_mean
    
    return a, b

def calculate_residuals(x_data, y_data, a, b):
    """Calcula os resíduos entre os dados observados e o ajuste linear."""
    y_pred = a * x_data + b
    residuals = y_data - y_pred
    return residuals

def print_table(x_data, y_data, residuals):
    """Exibe uma tabela com os dados, os valores ajustados e os resíduos."""
    headers = ["x", "y", "y ajustado", "Resíduo"]
    table = [[x, y, a * x + b, r] for x, y, r in zip(x_data, y_data, residuals)]
    print("\nTabela de Dados e Resíduos:")
    print(tabulate(table, headers=headers, tablefmt="grid", floatfmt=".6f"))

# Entrada de dados
try:
    n = int(input("Digite o número de pontos experimentais: "))
    
    print("\nDigite os valores de x separados por espaço:")
    x_data = np.array(list(map(float, input().split())))
    
    print("\nDigite os valores de y separados por espaço:")
    y_data = np.array(list(map(float, input().split())))
    
    if len(x_data) != n or len(y_data) != n:
        raise ValueError("O número de pontos fornecidos não corresponde ao número de entradas especificado.")
    
    # Cálculo do ajuste linear
    a, b = least_squares_fit(x_data, y_data)
    residuals = calculate_residuals(x_data, y_data, a, b)
    
    # Exibição dos resultados
    print_table(x_data, y_data, residuals)
    
    print("\nEquação da reta ajustada:")
    print(f"y = {a:.6f}x + {b:.6f}")
    
    print("\nSoma dos quadrados dos resíduos (SSR):")
    print(f"SSR = {np.sum(residuals ** 2):.6f}")
    
except Exception as e:
    print(f"Erro: {e}")
