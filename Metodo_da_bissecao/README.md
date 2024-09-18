# Resolvedor de Método da Bisseção

Este projeto implementa um método de bisseção em Python para encontrar raízes de funções contínuas. Além disso, inclui uma visualização da função em forma de gráfico ASCII diretamente no terminal.

## Funcionalidades

- **find_interval**: Encontra um intervalo `[a, b]` onde a função muda de sinal, indicando a presença de uma raiz. Por padrão a busca é realizada dentro do intervalo `[-100,100]`
- **bisection_method**: Executa o método da bisseção para aproximar a raiz de uma função dentro de um intervalo encontrado pela função ```find_interval()```, com uma precisão e número máximo de iterações especificados.
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
Digite a função f(x) em termos de 'x': x**2 - 3

Deseja utilizar uma tolerância diferente de 1e-5? (s/n): n

Deseja utilizar um número máximo de iterações diferente de 100? (s/n): n
```

### Exemplo de Saída
```plaintext
Gráfico ASCII de f(x) no intervalo [-30, 30]:

*                                                          *
 *                                                        * 
  **                                                    **  
    **                                                **    
      **                                            **      
        **                                        **        
          ***                                  ***          
             ***                            ***             
                ****                    ****                
                    ********************                                     

Intervalo inicial encontrado: [a, b] = [-2, -1]

Tabela de Passos da Bisseção:
+------------+----------+----------+----------+-----------+----------+
|   Iteração |        a |        b |      Xns |    f(Xns) |     Erro |
+============+==========+==========+==========+===========+==========+
|          1 | -2       | -1       | -1.5     | -0.75     | 0.5      |
+------------+----------+----------+----------+-----------+----------+
|          2 | -2       | -1.5     | -1.75    |  0.0625   | 0.25     |
+------------+----------+----------+----------+-----------+----------+
|          3 | -1.75    | -1.5     | -1.625   | -0.359375 | 0.125    |
+------------+----------+----------+----------+-----------+----------+
|          4 | -1.75    | -1.625   | -1.6875  | -0.152344 | 0.0625   |
|   ...      | ...      | ...      | ...      | ...       | ...      |
+------------+----------+----------+----------+-----------+----------+

A solução aproximada é: -1.732048
```

## Dependências

O projeto depende das seguintes bibliotecas Python:

- `numpy`
- `tabulate`

Você pode instalar as dependências usando:

```bash
pip install -r requirements.txt
```
