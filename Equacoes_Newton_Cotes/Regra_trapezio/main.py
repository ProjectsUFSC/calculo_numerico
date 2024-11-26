import numpy as np
from tabulate import tabulate

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n  # Largura de cada intervalo
    steps = []
    integral = 0
    
    for i in range(n):
        A = a + h * i     
        B = a + h * (i + 1)  
        area = (h / 2) * (f(A) + f(B)) 
        integral += area
        steps.append((i + 1, h, A, B, f(A), f(B), area, integral))
    
    return steps, integral

# Entrada da função
expression = input("\nDigite a função f(x) em termos de 'x': ")
f = lambda x: eval(expression)

# Entrada do intervalo e número de subdivisões
a = float(input("\nDigite o limite inferior do intervalo (a): "))
b = float(input("Digite o limite superior do intervalo (b): "))
n = int(input("Digite o número de subdivisões (n): "))

# Entrada do número de casas decimais
decimal_places = int(input("\nDigite o número de casas decimais para o arredondamento: "))

try:
    # Chamada da Regra do Trapézio
    steps, integral = trapezoidal_rule(f, a, b, n)
    
    # Monta a tabela de resultados
    headers = ["Iteração", "h", "a'", "b'", "f(a')", "f(b')", "Área do Trapézio", "Área Acumulada"]
    table = [
        [
            step[0],
            f"{step[1]:.{decimal_places}f}",
            f"{step[2]:.{decimal_places}f}",
            f"{step[3]:.{decimal_places}f}",
            f"{step[4]:.{decimal_places}f}",
            f"{step[5]:.{decimal_places}f}",
            f"{step[6]:.{decimal_places}f}",
            f"{step[7]:.{decimal_places}f}"
        ]
        for step in steps
    ]
    
    print("\nTabela de Cálculo (Regra do Trapézio):")
    print(tabulate(table, headers, tablefmt="grid"))
    
    # Exibe o resultado final
    print(f"\nValor aproximado da integral: {integral:.{decimal_places}f}\n")

except Exception as e:
    print(f"Erro: {e}")
