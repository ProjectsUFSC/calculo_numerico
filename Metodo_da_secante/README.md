# Resolvedor de Método da Secante

Este projeto implementa o método de cálculo numérico da Secante para encontrar raízes de funções contínuas. Além disso, inclui uma visualização da função em forma de gráfico ASCII diretamente no terminal.

## Funcionalidades

- **secant_method**: Executa o método da secante para aproximar a raiz de uma função a partir dos pontos inciais `x0` e `x1` com uma precisão e número máximo de iterações especificados pelo usuário.
- **plot_ascii**: Gera um gráfico ASCII da função no terminal para uma visualização rápida do comportamento da função.

## Como Usar

1. **Entrada da Função**: 
   - O programa solicita ao usuário que insira a função `f(x)` em termos de `x`.
   - A função deve ser digitada como uma expressão Python válida.

2. **Visualização da Função**:
   - O programa gera e exibe um gráfico ASCII da função no intervalo `[-30, 30]`.

3. **Entradas iniciais**:
    - O programa solicita ao usuário os dois valores iniciais `x0` e `x1`.

4. **Parâmetros de Tolerância e Iteração**:
   - O usuário pode optar por usar uma tolerância padrão de `1e-5` ou especificar uma diferente.
   - O usuário também pode definir um número máximo de iterações `(padrão: 100)`.

5. **Execução do Método da Secante**:
   - O programa executa o método da secante para encontrar uma aproximação da raiz e exibe os resultados em uma tabela formatada.

6. **Exibição dos Resultados**:
   - O programa exibe uma tabela mostrando cada iteração do método, com os valores de `x(n-1)`, `xn`, `x(n+1)`, `Erro`, e o erro relativo.
   - A solução aproximada é exibida ao final.

## Exemplo de Uso

```bash
python main.py
```


### Exemplo de Entrada
```python
Digite a função f(x) em termos de 'x': x**2 +x -6

Digite o valor inicial x0: 1.5

Digite o valor inicial x1: 1.7

Deseja utilizar uma tolerância diferente de 1e-5? (s/n): s

Digite a tolerância desejada: 0.01

Deseja utilizar um número máximo de iterações diferente de 100? (s/n): n
```

### Exemplo de Saída
```plaintext
Gráfico ASCII de f(x) no intervalo [-30, 30]:

                                                           *
*                                                         * 
 **                                                     **  
   **                                                 **    
     **                                             **      
       ***                                        **        
          **                                   ***          
            ***                             ***             
               *****                    ****                
                    ********************                                                     

Tabela de Passos do Método da Secante:
+------------+----------+---------+----------+----------+
|   Iteração |   X(n-1) |      Xn |   X(n+1) |     Erro |
+============+==========+=========+==========+==========+
|          1 |  1.5     | 1.7     |  2.03571 | 0.335714 |
+------------+----------+---------+----------+----------+
|          2 |  1.7     | 2.03571 |  1.99774 | 0.037977 |
+------------+----------+---------+----------+----------+
|          3 |  2.03571 | 1.99774 |  1.99998 | 0.002246 |
+------------+----------+---------+----------+----------+

A solução aproximada é: 1.999984
```

## Dependências

O projeto depende das seguintes bibliotecas Python:

- `numpy`
- `tabulate`

Você pode instalar as dependências usando:

```bash
pip install -r requirements.txt
```
