# Resolvedor de Método da Falsa Posição

Este projeto implementa o método de cálculo numérico da falsa posição em Python para encontrar raízes de funções contínuas. Além disso, inclui uma visualização da função em forma de gráfico ASCII diretamente no terminal.

## Funcionalidades

- **find_interval**: Encontra um intervalo `[a, b]` onde a função muda de sinal, indicando a presença de uma raiz. Por padrão a busca é realizada dentro do intervalo `[-100,100]`
- **false_position_method**: Executa o método da falsa posição para aproximar a raiz de uma função dentro de um intervalo encontrado pela função ```find_interval()```, com uma precisão e número máximo de iterações especificados.
- **plot_ascii**: Gera um gráfico ASCII da função no terminal para uma visualização rápida do comportamento da função.

## Como Usar

1. **Entrada da Função**: 
   - O programa solicita ao usuário que insira a função `f(x)` em termos de `x`.
   - A função deve ser digitada como uma expressão Python válida.

2. **Visualização da Função**:
   - O programa gera e exibe um gráfico ASCII da função no intervalo `[-30, 30]`.

3. **Parâmetros de Tolerância e Iteração**:
   - O usuário pode optar por usar uma tolerância padrão de `1e-5` ou especificar uma diferente.
   - O usuário também pode definir um número máximo de iterações `(padrão: 100)`.

4. **Execução do Método da Bisseção**:
   - O programa encontra um intervalo `[a, b]` onde a função muda de sinal.
   - Em seguida, executa o método da bisseção para encontrar uma aproximação da raiz dentro do intervalo e exibe os resultados em uma tabela formatada.

5. **Exibição dos Resultados**:
   - O programa exibe uma tabela mostrando cada iteração do método, com os valores de `a`, `b`, `Xns`, `f(Xns)`, e o erro relativo.
   - A solução aproximada é exibida ao final.

## Exemplo de Uso

```bash
python main.py
```


### Exemplo de Entrada
```python
Digite a função f(x) em termos de 'x': x**3 - 9*x + 3

Deseja utilizar uma tolerância diferente de 1e-5? (s/n): s

Digite a tolerância desejada: 0.001

Deseja utilizar um número máximo de iterações diferente de 100? (s/n): n
```

### Exemplo de Saída
```plaintext
Gráfico ASCII de f(x) no intervalo [-30, 30]:

                                                           *
                                                         ** 
                                                      ***   
                                                   ***      
                                            *******         
                ****************************                
         *******                                            
      ***                                                   
   ***                                                      
***                            

Intervalo inicial encontrado: [a, b] = [-4, -3]

Tabela de Passos da Falsa Posição:
+------------+----------+----------+----------+-----------+----------+
|   Iteração |        a |        b |      Xns |    f(Xns) |     Erro |
+============+==========+==========+==========+===========+==========+
|          1 | -4       | -3       | -3.10714 |  0.966882 | 0.966882 |
+------------+----------+----------+----------+-----------+----------+
|          2 | -4       | -3.10714 | -3.20281 | -1.02903  | 1.02903  |
+------------+----------+----------+----------+-----------+----------+
|          3 | -3.20281 | -3.10714 | -3.17837 | -0.502751 | 0.502751 |
+------------+----------+----------+----------+-----------+----------+
|          4 | -3.17837 | -3.10714 | -3.16815 | -0.285918 | 0.285918 |
+------------+----------+----------+----------+-----------+----------+
|          5 | -3.16815 | -3.10714 | -3.16284 | -0.174117 | 0.174117 |
+------------+----------+----------+----------+-----------+----------+
|          6 | -3.16284 | -3.10714 | -3.15979 | -0.110011 | 0.110011 |
+------------+----------+----------+----------+-----------+----------+
|          7 | -3.15979 | -3.10714 | -3.15792 | -0.071026 | 0.071026 |
+------------+----------+----------+----------+-----------+----------+
|          8 | -3.15792 | -3.10714 | -3.15675 | -0.046473 | 0.046473 |
+------------+----------+----------+----------+-----------+----------+
|          9 | -3.15675 | -3.10714 | -3.15599 | -0.030666 | 0.030666 |
+------------+----------+----------+----------+-----------+----------+
|         10 | -3.15599 | -3.10714 | -3.1555  | -0.020347 | 0.020347 |
+------------+----------+----------+----------+-----------+----------+
|         11 | -3.1555  | -3.10714 | -3.15517 | -0.013549 | 0.013549 |
+------------+----------+----------+----------+-----------+----------+
|         12 | -3.15517 | -3.10714 | -3.15496 | -0.009044 | 0.009044 |
+------------+----------+----------+----------+-----------+----------+
|         13 | -3.15496 | -3.10714 | -3.15481 | -0.006046 | 0.006046 |
+------------+----------+----------+----------+-----------+----------+
|         14 | -3.15481 | -3.10714 | -3.15472 | -0.004046 | 0.004046 |
+------------+----------+----------+----------+-----------+----------+
|         15 | -3.15472 | -3.10714 | -3.15465 | -0.00271  | 0.00271  |
+------------+----------+----------+----------+-----------+----------+
|         16 | -3.15465 | -3.10714 | -3.15461 | -0.001816 | 0.001816 |
+------------+----------+----------+----------+-----------+----------+
|         17 | -3.15461 | -3.10714 | -3.15458 | -0.001217 | 0.001217 |
+------------+----------+----------+----------+-----------+----------+
|         18 | -3.15458 | -3.10714 | -3.15456 | -0.000816 | 0.000816 |
+------------+----------+----------+----------+-----------+----------+

A solução aproximada é: -3.154562
f(x) = -0.000816
```

## Dependências

O projeto depende das seguintes bibliotecas Python:

- `numpy`
- `tabulate`

Você pode instalar as dependências usando:

```bash
pip install -r requirements.txt
```
