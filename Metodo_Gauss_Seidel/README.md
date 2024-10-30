# Resolvedor de Sistema Linear com Método de Gauss-Seidel

Este projeto implementa o método iterativo de Gauss-Seidel para resolver sistemas de equações lineares. Ele exibe as soluções intermediárias e os erros em cada iteração, permitindo acompanhar o processo de convergência até a solução final do sistema.

## Funcionalidades

- **`gauss_seidel_method`**: Implementa o método de Gauss-Seidel para resolver um sistema de equações lineares do tipo `Ax = b`.
- **`print_steps`**: Exibe os valores das variáveis e os erros a cada iteração em uma tabela formatada no terminal.

## Como Usar

1. **Entrada da Matriz e Vetor**:
   - O programa solicita que o usuário insira os coeficientes da matriz `A` e do vetor `b` do sistema de equações lineares `Ax = b`.

2. **Configuração de Tolerância e Máximo de Iterações**:
   - O usuário pode definir uma tolerância diferente da padrão (1e-5) e um número máximo de iterações (padrão: 100).

3. **Execução do Método de Gauss-Seidel**:
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
Equação 1 (separar coeficientes por espaço): 6 -1 1
Equação 2 (separar coeficientes por espaço): 1 8 -1
Equação 3 (separar coeficientes por espaço): 1 1 5

Digite os coeficientes do vetor b:
b (separar coeficientes por espaço): 7 16 18

Deseja utilizar uma tolerância diferente de 1e-5? (s/n): s

Digite a tolerância desejada: 0.01

Deseja utilizar um número máximo de iterações diferente de 100? (s/n): n
```

### Exemplo de Saída
```plaintext
Matriz inicial aumentada [A|b]:
+---+----+----+----+
| 6 | -1 |  1 |  7 |
+---+----+----+----+
| 1 |  8 | -1 | 16 |
+---+----+----+----+
| 1 |  1 |  5 | 18 |
+---+----+----+----+

Tabela de Soluções e Erros por Iteração:
+----------+---------+---------+----------+----------+----------+
|       x1 |      x2 |      x3 |   err_x1 |   err_x2 |   err_x3 |
+==========+=========+=========+==========+==========+==========+
| 1.16667  | 1.85417 | 2.99583 | 1.16667  | 1.85417  | 2.99583  |
+----------+---------+---------+----------+----------+----------+
| 0.976389 | 2.25243 | 2.95424 | 0.190278 | 0.398264 | 0.041597 |
+----------+---------+---------+----------+----------+----------+
| 1.0497   | 2.23807 | 2.94245 | 0.07331  | 0.014363 | 0.011789 |
+----------+---------+---------+----------+----------+----------+
| 1.04927  | 2.23665 | 2.94282 | 0.000429 | 0.00142  | 0.00037  |
+----------+---------+---------+----------+----------+----------+

Solução aproximada final:
x1 = 1.049699
x2 = 2.238067
x3 = 2.942447

Vetor b (coeficientes):
+------+------+------+
|   b1 |   b2 |   b3 |
+======+======+======+
|    7 |   16 |   18 |
+------+------+------+

Vetor b' (calculado com base nos valores de x):
+---------+---------+-------+
|     b'1 |     b'2 |   b'3 |
+=========+=========+=======+
| 7.00257 | 16.0118 |    18 |
+---------+---------+-------+
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

