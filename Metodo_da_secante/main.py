import numpy as np
from tabulate import tabulate

def secant_method(f, x0, x1, tol, max_iter):
    steps = []
    
    for iter_count in range(1, max_iter + 1):
        f_x0 = f(x0)
        f_x1 = f(x1)

        xn = x1 - f_x1 * (x0 - x1) / (f_x0 - f_x1)

        err = abs(xn - x1)
        
        steps.append((iter_count, x0, x1, xn, err))
        
        if err <= tol:
            break
        
        x0 = x1
        x1 = xn
    
    return steps

def plot_ascii(f, start=-30, end=30, width=60, height=10):
    x_values = np.linspace(start, end, width)
    y_values = np.array([f(x) for x in x_values])
    
    min_y, max_y = y_values.min(), y_values.max()
    y_range = max_y - min_y
    
    y_scaled = np.floor((y_values - min_y) / y_range * (height - 1)).astype(int)
    
    canvas = np.full((height, width), ' ', dtype=str)
    
    for i in range(width):
        y_pos = height - 1 - y_scaled[i]
        if 0 <= y_pos < height:
            canvas[y_pos, i] = '*'
    
    canvas_str = '\n'.join([''.join(row) for row in canvas])
    
    print(f"\nGráfico ASCII de f(x) no intervalo [{start}, {end}]:\n")
    print(canvas_str)

# Entrada da função e da derivada
expression = input("\nDigite a função f(x) em termos de 'x': ")

f = lambda x: eval(expression)

plot_ascii(f)

x0 = float(input("\nDigite o valor inicial x0: "))
x1 = float(input("\nDigite o valor inicial x1: "))

tol = input("\nDeseja utilizar uma tolerância diferente de 1e-5? (s/n): ")
tol = float(input("\nDigite a tolerância desejada: ")) if tol == 's' else 1e-5

max_iter = input("\nDeseja utilizar um número máximo de iterações diferente de 100? (s/n): ")
max_iter = int(input("\nDigite o número máximo de iterações desejado: ")) if max_iter == 's' else 100


try:

    
    steps = secant_method(f, x0, x1, tol, max_iter)
    
    headers = ["Iteração", "X(n-1)", "Xn", "X(n+1)", "Erro"]
    table = [[step[0], f"{step[1]:.6f}", f"{step[2]:.6f}", f"{step[3]:.6f}", f"{step[4]:.6f}"] for step in steps]

    print("\nTabela de Passos do Método da Secante:")
    print(tabulate(table, headers, tablefmt="grid"))

    print(f"\nA solução aproximada é: {steps[-1][3]:.6f}\n")

except ValueError as e:
    print(f"Erro: {e}")
