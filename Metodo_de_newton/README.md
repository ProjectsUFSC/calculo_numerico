# Resolvedor de Método de Newton

Este projeto implementa o método de cálculo numérico de Newton ou e Newton-Raphson para encontrar raízes de funções contínuas. Além disso, inclui uma visualização da função em forma de gráfico ASCII diretamente no terminal.

## Funcionalidades

- **find_interval**: Encontra um intervalo `[a, b]` onde a função muda de sinal, indicando a presença de uma raiz. Por padrão a busca é realizada dentro do intervalo `[-100,100]`
- **find_initial_value**: Encontra o melhor valor inicial levando em consideração os valores `[a, b]` achados em ```find_intervals()``` usando a regra f(x) * f''(x) > 0.
- **newton_method**: Executa o método de newton para aproximar a raiz de uma função a partir do ponto incial encontrado pela função ```find_initial_value()```, com uma precisão e número máximo de iterações especificados.
- **plot_ascii**: Gera um gráfico ASCII da função no terminal para uma visualização rápida do comportamento da função.

## Como Usar

1. **Entrada da Função**: 
   - O programa solicita ao usuário que insira a função `f(x)` em termos de `x`.
   - A função deve ser digitada como uma expressão Python válida.

2. **Entrada da Derivada da Função**:
   - O programa solicita ao usuário que insira a derivada da função `f'(x)` em termos de `x`. 
   - A função deve ser digitada como uma expressão Python válida.

3. **Visualização da Função**:
   - O programa gera e exibe um gráfico ASCII da função no intervalo `[-30, 30]`.

4. **Parâmetros de Tolerância e Iteração**:
   - O usuário pode optar por usar uma tolerância padrão de `1e-5` ou especificar uma diferente.
   - O usuário também pode definir um número máximo de iterações `(padrão: 100)`.

5. **Execução do Método de Newton**:
   - O programa encontra um valor inicial `x'` onde a `f(x)*f''(x)>0`.
   - Em seguida, executa o método de newton para encontrar uma aproximação da raiz e exibe os resultados em uma tabela formatada.

6. **Exibição dos Resultados**:
   - O programa exibe uma tabela mostrando cada iteração do método, com os valores de `xn`, `f(xn)`, `df(xn)`, `x(n+1)`, `Erro`, e o erro relativo.
   - A solução aproximada é exibida ao final.

## Exemplo de Uso

```bash
python main.py
```


### Exemplo de Entrada
```python
Digite a função f(x) em termos de 'x': 2*x - np.sin(x) -4

Digite a derivada df(x) em termos de 'x': 2 - np.cos(x)

Digite a segunda derivada d²f(x) em termos de 'x': np.sin(x)

Deseja utilizar uma tolerância diferente de 1e-5? (s/n): s

Digite a tolerância desejada: 0.001

Deseja utilizar um número máximo de iterações diferente de 100? (s/n): n
```

### Exemplo de Saída
```plaintext
Gráfico ASCII de f(x) no intervalo [-30, 30]:

                                                           *
                                                     ****** 
                                              *******       
                                        ******              
                                 *******                    
                           ******                           
                    *******                                 
              ******                                        
       *******                                              
*******                                                     

Valor inicial encontrado automaticamente: x0 = 3.00

Tabela de Passos do Método de Newton:
+------------+---------+----------+----------+---------+----------+
|   Iteração |      x0 |    f(x0) |   df(x0) |      x1 |     Erro |
+============+=========+==========+==========+=========+==========+
|          1 | 3       | 1.85888  |  2.98999 | 2.3783  | 0.621701 |
+------------+---------+----------+----------+---------+----------+
|          2 | 2.3783  | 0.065294 |  2.72256 | 2.35432 | 0.023983 |
+------------+---------+----------+----------+---------+----------+
|          3 | 2.35432 | 0.0002   |  2.70578 | 2.35424 | 7.4e-05  |
+------------+---------+----------+----------+---------+----------+

A solução aproximada é: 2.354243
```

## Dependências

O projeto depende das seguintes bibliotecas Python:

- `numpy`
- `tabulate`

Você pode instalar as dependências usando:

```bash
pip install -r requirements.txt
```
