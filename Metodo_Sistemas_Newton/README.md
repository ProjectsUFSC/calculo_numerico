# Resolvedor de Sistema Não Linear com Método de Newton

Este projeto implementa o método de Newton para resolver sistemas de equações não lineares. Ele exibe as soluções intermediárias e os erros em cada iteração, permitindo acompanhar o processo de convergência.

## Funcionalidades

- **`newton_method`**: Implementa o método de Newton para resolver um sistema de equações não lineares do tipo `F(x) = 0`, onde `F` é um vetor de funções e `J` é a matriz Jacobiana.
- **`print_steps`**: Exibe os valores das variáveis e os erros a cada iteração em uma tabela formatada no terminal.

## Como Usar

1. **Definir o Sistema de Equações e a Jacobiana**:
   - O programa solicita que o usuário insira o número de variáveis, as funções do sistema não linear `F(x)` e a matriz Jacobiana `J(x)`.

2. **Aproximação Inicial**:
   - O usuário insere uma aproximação inicial para os valores de `x`.

3. **Configuração de Tolerância e Máximo de Iterações**:
   - O usuário pode definir uma tolerância diferente da padrão (1e-5) e um número máximo de iterações (padrão: 100).

4. **Execução do Método de Newton**:
   - O programa resolve o sistema iterativamente, exibindo os valores das variáveis e os erros em cada iteração até que o critério de convergência seja atendido.

5. **Exibição dos Resultados**:
   - Após a convergência, o programa exibe a solução final do sistema.

## Exemplo de Uso

```bash
python main.py
```

### Exemplo de Entrada
Considere o sistema:
\[
f_1(x) = x_1 + x_2 - 3
\]
\[
f_2(x) = x_1^2 + x_2^2 - 9
\]

Aproximação inicial: \( x_0 = (1, 5) \)

```plaintext
Digite o número de variáveis do sistema: 2

Digite a expressão para f1(x1, ..., x2): x1 + x2 - 3
Digite a expressão para f2(x1, ..., x2): x1**2 + x2**2 - 9

Digite a derivada ∂f1/∂x1: 1
Digite a derivada ∂f1/∂x2: 1
Digite a derivada ∂f2/∂x1: 2*x1
Digite a derivada ∂f2/∂x2: 2*x2

Digite a aproximação inicial para x (x1, x2): 1 5

Deseja utilizar uma tolerância diferente de 1e-5? (s/n): n
Deseja utilizar um número máximo de iterações diferente de 100? (s/n): n
```

### Exemplo de Saída
```plaintext
Tabela de Soluções e Erros por Iteração:
+-----------+---------+----------+
|        x1 |      x2 |       Er |
+===========+=========+==========+
| -0.625    | 3.625   | 1.625    |
+-----------+---------+----------+
| -0.091912 | 3.09191 | 0.533088 |
+-----------+---------+----------+
| -0.002653 | 3.00265 | 0.089258 |
+-----------+---------+----------+
| -2e-06    | 3       | 0.002651 |
+-----------+---------+----------+
| -0        | 3       | 2e-06    |
+-----------+---------+----------+

Solução aproximada final:
x1 = -0.000000
x2 = 3.000000
```

## Dependências

O projeto depende das seguintes bibliotecas Python:

- **numpy**: Para cálculos matemáticos e manipulação de arrays.
- **tabulate**: Para exibir os resultados em forma de tabela.
- **sympy**: Para interpretar as entradas do usuário.

### Instalação das Dependências

Você pode instalar as dependências utilizando o comando:

```bash
pip install -r requirements.txt
```

## Observações

O método de Newton requer que o sistema seja derivável e que a matriz Jacobiana seja invertível em cada iteração. É recomendado usar uma boa aproximação inicial para aumentar a chance de convergência.