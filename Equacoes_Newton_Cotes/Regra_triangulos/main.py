import numpy as np
from tabulate import tabulate

def rectangle_method(f, a, b, n):
    
    h = (b - a) / n  # Largura de cada retângulo
    steps = []
    integral = 0
    
    for i in range(n):
        A = (a + h*i)
        B = (a + h*(i+1))
        X = (A +  B)/2
        area = f(X)
        integral += area
        steps.append((i + 1, h , A , B , X, f(X), integral))
    
    return steps, h*integral

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
    # Chamada do método dos retângulos
    steps, integral = rectangle_method(f, a, b, n)
    
    # Monta a tabela de resultados
    headers = ["Iteração", "h", "a'", "b'", "x'", "f(x')", "área"]
    table = [
        [
            step[0], 
            f"{step[1]:.{decimal_places}f}", 
            f"{step[2]:.{decimal_places}f}", 
            f"{step[3]:.{decimal_places}f}",
            f"{step[4]:.{decimal_places}f}",
            f"{step[5]:.{decimal_places}f}",
            f"{step[6]:.{decimal_places}f}"
        ] 
        for step in steps
    ]
    
    print("\nTabela de Cálculo (Método dos Retângulos):")
    print(tabulate(table, headers, tablefmt="grid"))
    
    # Exibe o resultado final
    print(f"\nValor aproximado da integral: {integral:.{decimal_places}f}\n")

except Exception as e:
    print(f"Erro: {e}")
