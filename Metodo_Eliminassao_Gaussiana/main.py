import numpy as np
from tabulate import tabulate

def gauss_elimination(A, b):
    n = len(b)
    steps = []
    
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    for i in range(n):

        for j in range(i + 1, n):
            if Ab[i,i] == 0:
                for k in range(i + 1, n):
                    if Ab[k, i] != 0:
                        Ab[[i, k]] = Ab[[k, i]]
                        break
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
        
        steps.append(np.copy(Ab))
    
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.sum(Ab[i, i+1:-1] * x[i+1:])) / Ab[i, i]

    return x, steps

def print_steps(steps):
    headers = [f"Passo {i+1}" for i in range(len(steps))]
    tables = [np.round(step, 4) for step in steps]
    
    for i, table in enumerate(tables):
        print(f"\nMatriz no Passo {i+1}:")
        print(tabulate(table, tablefmt="grid"))

n = int(input("Digite o número de equações: "))
A = np.zeros((n, n))
b = np.zeros(n)


print("\nDigite os coeficientes da matriz A:")
for i in range(n):
    A[i] = list(map(float, input(f"Equação {i+1} (separar coeficientes por espaço): ").split()))

print("\nDigite os coeficientes do vetor b:")
b = np.array(list(map(float, input("b (separar coeficientes por espaço): ").split())))

Ab = np.hstack([A, b.reshape(-1, 1)])
print("\nMatriz inicial aumentada [A|b]:")
print(tabulate(np.round(Ab, 4), tablefmt="grid"))

try:

    x, steps = gauss_elimination(A, b)
    
    print_steps(steps)
    
    print("\nSolução aproximada:")
    for i, xi in enumerate(x):
        print(f"x{i+1} = {xi:.6f}")

except Exception as e:
    print(f"Erro: {e}")
