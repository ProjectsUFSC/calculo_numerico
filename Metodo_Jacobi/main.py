import numpy as np
from tabulate import tabulate

def jacobi_method(A, b, tol=1e-5, max_iterations=100):
    n = len(b)
    x = np.zeros_like(b)  # vetor inicial de zeros
    steps = []  # armazena as iterações
    
    for i in range(n):
        if abs(A[i, i]) <= np.sum(np.abs(A[i, :])) - np.abs(A[i, i]):
            raise ValueError(f"O critério de dominância diagonal não é satisfeito na linha {i+1}")

    for k in range(max_iterations):
        x_new = np.zeros_like(x)

        for i in range(n):
            s = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s) / A[i, i]
        
        # Calcular erros para x_1, x_2, x_3
        err_x1 = abs(x_new[0] - x[0])
        err_x2 = abs(x_new[1] - x[1]) if n > 1 else 0
        err_x3 = abs(x_new[2] - x[2]) if n > 2 else 0
        
        steps.append(np.hstack([np.copy(x_new), [err_x1, err_x2, err_x3]]))
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:  # Critério de convergência
            break
        
        x = x_new

    return x, steps

def print_steps(steps):
    headers = [f"x{i+1}" for i in range(len(steps[0]) // 2)] + ["err_x1", "err_x2", "err_x3"]
    
    # Criar a tabela combinando os valores de x e seus respectivos erros
    table = [np.round(step, 6) for step in steps]
    
    print("\nTabela de Soluções e Erros por Iteração:")
    print(tabulate(table, headers=headers, tablefmt="grid"))

# Leitura da matriz A e vetor b
n = int(input("Digite o número de equações: "))
A = np.zeros((n, n))
b = np.zeros(n)

print("\nDigite os coeficientes da matriz A:")
for i in range(n):
    A[i] = list(map(float, input(f"Equação {i+1} (separar coeficientes por espaço): ").split()))

print("\nDigite os coeficientes do vetor b:")
b = np.array(list(map(float, input("b (separar coeficientes por espaço): ").split())))

# Perguntar tolerância e número máximo de iterações ao usuário
tol = input("\nDeseja utilizar uma tolerância diferente de 1e-5? (s/n): ")
tol = float(input("\nDigite a tolerância desejada: ")) if tol.lower() == 's' else 1e-5

max_iter = input("\nDeseja utilizar um número máximo de iterações diferente de 100? (s/n): ")
max_iter = int(input("\nDigite o número máximo de iterações desejado: ")) if max_iter.lower() == 's' else 100

# Imprimir a matriz aumentada
Ab = np.hstack([A, b.reshape(-1, 1)])
print("\nMatriz inicial aumentada [A|b]:")
print(tabulate(np.round(Ab, 4), tablefmt="grid"))

try:
    # Chamar o método de Jacobi
    x, steps = jacobi_method(A, b, tol, max_iter)
    
    # Imprimir as iterações e os erros
    print_steps(steps)
    
    # Imprimir a solução final
    print("\nSolução aproximada final:")
    for i, xi in enumerate(x):
        print(f"x{i+1} = {xi:.6f}")
    
    # Mostrar o vetor b
    print("\nVetor b (coeficientes):")
    print(tabulate([b], headers=[f"b{i+1}" for i in range(len(b))], tablefmt="grid"))
    
    # Calcular b' com base nos valores de x encontrados
    b_prime = np.dot(A, x)
    print("\nVetor b' (calculado com base nos valores de x):")
    print(tabulate([b_prime], headers=[f"b'{i+1}" for i in range(len(b_prime))], tablefmt="grid"))

except Exception as e:
    print(f"Erro: {e}")
