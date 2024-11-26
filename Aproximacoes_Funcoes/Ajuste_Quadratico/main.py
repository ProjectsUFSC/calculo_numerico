import numpy as np
from tabulate import tabulate

def quadratic_least_squares_fit(x_data, y_data):
    """
    Calcula os coeficientes a, b e c do ajuste quadrático
    y = ax² + bx + c usando mínimos quadrados.
    """
    n = len(x_data)
    if n != len(y_data):
        raise ValueError("Os vetores x e y devem ter o mesmo tamanho.")
    
    # Monta a matriz do sistema normal
    X = np.vstack([x_data**2, x_data, np.ones_like(x_data)]).T
    Y = y_data.reshape(-1, 1)
    
    # Resolve o sistema usando o método dos mínimos quadrados
    coef, _, _, _ = np.linalg.lstsq(X, Y, rcond=None)
    a, b, c = coef.flatten()
    
    return a, b, c

def calculate_residuals(x_data, y_data, a, b, c):
    """
    Calcula os resíduos entre os dados observados e o ajuste quadrático.
    """
    y_pred = a * x_data**2 + b * x_data + c
    residuals = y_data - y_pred
    return residuals

def print_table(x_data, y_data, residuals, a, b, c):
    """
    Exibe uma tabela com os dados, os valores ajustados e os resíduos.
    """
    y_adjusted = a * x_data**2 + b * x_data + c
    headers = ["x", "y", "y ajustado", "Resíduo"]
    table = [[x, y, y_adj, res] for x, y, y_adj, res in zip(x_data, y_data, y_adjusted, residuals)]
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
    
    # Cálculo do ajuste quadrático
    a, b, c = quadratic_least_squares_fit(x_data, y_data)
    residuals = calculate_residuals(x_data, y_data, a, b, c)
    
    # Exibição dos resultados
    print_table(x_data, y_data, residuals, a, b, c)
    
    print("\nEquação do ajuste quadrático:")
    print(f"y = {a:.6f}x² + {b:.6f}x + {c:.6f}")
    
    print("\nSoma dos quadrados dos resíduos (SSR):")
    print(f"SSR = {np.sum(residuals ** 2):.6f}")
    
except Exception as e:
    print(f"Erro: {e}")
