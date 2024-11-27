import numpy as np
from tabulate import tabulate

def simpson_method(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("O número de subdivisões (n) deve ser par para a Regra de Simpson.")
    
    h = (b - a) / n  # Largura de cada subintervalo
    steps = []
    integral = 0

    for i in range(n + 1):
        x = a + i * h
        weight = 2 if i % 2 == 0 else 4
        if i == 0 or i == n:
            weight = 1
        term = weight * f(x)
        integral += term
        steps.append((i, x, f(x), weight, term, integral))
    
    integral = integral * (h / 3)
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
    # Chamada do método de Simpson
    steps, integral = simpson_method(f, a, b, n)
    
    # Monta a tabela de resultados
    headers = ["Iteração", "x", "f(x)", "c", "c*f(x)", "Integral"]
    table = [
        [
            step[0],
            f"{step[1]:.{decimal_places}f}",
            f"{step[2]:.{decimal_places}f}",
            step[3],
            f"{step[4]:.{decimal_places}f}",
            f"{step[5]:.{decimal_places}f}"
        ] 
        for step in steps
    ]
    
    print("\nTabela de Cálculo (Regra de Simpson):")
    print(tabulate(table, headers, tablefmt="grid"))
    
    # Exibe o resultado final
    print(f"\nValor aproximado da integral: {integral:.{decimal_places}f}\n")

except Exception as e:
    print(f"Erro: {e}")
