# Resolvedor de Sistema Linear com Método de Jacobi

Este projeto implementa o método iterativo de Jacobi para resolver sistemas de equações lineares. Ele exibe as soluções intermediárias e os erros em cada iteração, permitindo acompanhar o processo de convergência.

## Funcionalidades

- **`jacobi_method`**: Implementa o método de Jacobi para resolver um sistema de equações lineares do tipo `Ax = b`.
- **`print_steps`**: Exibe os valores das variáveis e os erros a cada iteração em uma tabela formatada no terminal.

## Como Usar

1. **Entrada da Matriz e Vetor**:
   - O programa solicita que o usuário insira os coeficientes da matriz `A` e do vetor `b` do sistema de equações lineares `Ax = b`.

2. **Configuração de Tolerância e Máximo de Iterações**:
   - O usuário pode definir uma tolerância diferente da padrão (1e-5) e um número máximo de iterações (padrão: 100).

3. **Execução do Método de Jacobi**:
   - O programa resolve o sistema iterativamente, exibindo os valores das variáveis e os erros em cada iteração até que o critério de convergência seja atendido.

4. **Exibição dos Resultados**:
   - Após a convergência, o programa exibe a solução final do sistema, o vetor original `b` e o vetor `b'` calculado com base na solução aproximada.

## Exemplo de Uso

```bash
python main.py
```

### Exemplo de Entrada
```plaintext
Digite o número de equações: 3

Digite os coeficientes da matriz A:
Equação 1 (separar coeficientes por espaço): 4 1 2
Equação 2 (separar coeficientes por espaço): 3 5 1
Equação 3 (separar coeficientes por espaço): 1 1 3

Digite os coeficientes do vetor b:
b (separar coeficientes por espaço): 4 7 3
```

### Exemplo de Saída
```plaintext
Matriz inicial aumentada [A|b]:
+-----+-----+-----+-----+
| 4   | 1   | 2   | 4   |
+-----+-----+-----+-----+
| 3   | 5   | 1   | 7   |
+-----+-----+-----+-----+
| 1   | 1   | 3   | 3   |
+-----+-----+-----+-----+

Tabela de Soluções e Erros por Iteração:
+----------+----------+----------+----------+----------+----------+
|    x1    |    x2    |    x3    |  err_x1  |  err_x2  |  err_x3  |
+----------+----------+----------+----------+----------+----------+
|   1.0000 |   1.4000 |   0.5333 |   1.0000 |   1.4000 |   0.5333 |
|   0.4167 |   1.2333 |   0.5333 |   0.5833 |   0.1667 |   0.0000 |
|   0.4250 |   1.4100 |   0.3667 |   0.0083 |   0.1767 |   0.1667 |
|   0.4533 |   1.4167 |   0.3667 |   0.0283 |   0.0067 |   0.0000 |
|   0.4500 |   1.4230 |   0.3611 |   0.0033 |   0.0063 |   0.0056 |
+----------+----------+----------+----------+----------+----------+

Solução aproximada final:
x1 = 0.450000
x2 = 1.423000
x3 = 0.361100

Vetor b (coeficientes):
+------+-------+-------+
|  b1  |   b2  |   b3  |
+------+-------+-------+
|  4.0 |  7.0  |  3.0  |
+------+-------+-------+

Vetor b' (calculado com base nos valores de x):
+-------+--------+--------+
|  b'1  |   b'2  |   b'3  |
+-------+--------+--------+
|  4.0  |   7.0  |   3.0  |
+-------+--------+--------+
```

## Dependências

O projeto depende das seguintes bibliotecas Python:

- **numpy**: Biblioteca para cálculos matemáticos e manipulação de arrays.
- **tabulate**: Utilizada para exibir os resultados em forma de tabela.

### Instalação das dependências

Você pode instalar as dependências utilizando o comando:

```bash
pip install -r requirements.txt
```
