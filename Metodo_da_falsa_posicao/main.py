import numpy as np
from tabulate import tabulate

def find_interval(f, start=-100, end=100, step=1):
    x1 = start
    x2 = start + step
    f_x1 = f(x1)
    
    while x2 <= end:
        f_x2 = f(x2)
        if f_x1 * f_x2 < 0:
            return x1, x2
        x1, f_x1 = x2, f_x2
        x2 += step
    
    raise ValueError("\nNão foi encontrado um intervalo com mudança de sinal dentro do intervalo {-100, 100}")

def false_position_method(f, a, b, tol, max_iter):
    steps = []
    f_a = f(a)
    f_b = f(b)
    
    
    for iter_count in range(1, max_iter + 1):
        Xns = (a * f_b - b * f_a) / (f_b - f_a)
        f_Xns = f(Xns)
        err = abs(f(Xns))
        steps.append((iter_count, a, b, Xns, f_Xns, err))
        
        if err <= tol:
            break
        
        if f_Xns * f_a < 0:
            b = Xns
        else:
            a = Xns
            f_a = f_Xns 
    
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

expression = input("\nDigite a função f(x) em termos de 'x': ")
f = lambda x: eval(expression)

plot_ascii(f)

tol = input("\nDeseja utilizar uma tolerância diferente de 1e-5? (s/n): ")
tol = float(input("\nDigite a tolerância desejada: ")) if tol == 's' else 1e-5

max_iter = input("\nDeseja utilizar um número máximo de iterações diferente de 100? (s/n): ")
max_iter = int(input("\nDigite o número máximo de iterações desejado: ")) if max_iter == 's' else 100

try:
    a, b = find_interval(f)
    print(f"\nIntervalo inicial encontrado: [a, b] = [{a}, {b}]")
    
    steps = false_position_method(f, a, b, tol, max_iter)
    
    headers = ["Iteração", "a", "b", "Xns", "f(Xns)", "Erro"]
    table = [[step[0], f"{step[1]:.6f}", f"{step[2]:.6f}", f"{step[3]:.6f}", f"{step[4]:.6f}", f"{step[5]:.6f}"] for step in steps]

    print("\nTabela de Passos da Falsa Posição:")
    print(tabulate(table, headers, tablefmt="grid"))

    print(f"\nA solução aproximada é: {steps[-1][3]:.6f}\n\n")
    print(f"f(x) = {f(steps[-1][3]):.6f}\n\n")

except ValueError as e:
    print(f"Erro: {e}")
