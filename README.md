# Função Multiplicação de Argumentos

Este repositório contém um exercício de programação em Python que implementa uma função para multiplicar todos os argumentos não nomeados recebidos e retornar o total.

## Objetivo

O objetivo deste exercício é criar uma função que receba múltiplos argumentos e os multiplique. O resultado da multiplicação é então retornado e exibido. O programa permite que o usuário forneça quantos números quiser para a multiplicação.

## Como Funciona

1. A função **`multiplicacao()`** usa o operador `*args` para receber uma quantidade variável de argumentos numéricos.
2. A função percorre todos os argumentos passados e os multiplica.
3. O resultado da multiplicação é armazenado na variável `total` e retornado.
4. O programa exibe o resultado final da multiplicação no console.

## Estrutura do Código

- **Função `multiplicacao()`**: A função recebe múltiplos argumentos (não nomeados) e multiplica todos os números passados.
  - **`total = 1`**: Inicializa a variável `total` com 1 (porque qualquer número multiplicado por 1 não altera seu valor).
  - **`for num in args:`**: Itera sobre todos os números passados para a função.
  - **`total *= num`**: Multiplica o número atual de `args` pelo valor de `total`.
  - **`return total`**: Retorna o resultado final da multiplicação.
  
- **Entrada do usuário**: O programa chama a função **`multiplicacao()`** passando vários números como argumentos.
- **Exibição do resultado**: O resultado da multiplicação é impresso no console.

## Exemplo de Execução

### Entrada:
```python
resultado = multiplicacao(1, 2, 3, 4, 5, 6)
print(f'O resultado da multiplicação é: {resultado}')
```

### Saída:
```
O resultado da multiplicação é: 720
```

## Como Usar

1. Clone ou baixe este repositório.
2. Abra o arquivo Python no seu editor de código favorito.
3. Execute o programa.
4. A função **`multiplicacao()`** receberá os argumentos que você passar para ela, e o programa exibirá o resultado da multiplicação desses números.

## Requisitos

- Python 3.x

## Contribuindo

Se você deseja contribuir para este exercício, pode adicionar mais funcionalidades, como dividir os números ou realizar outras operações matemáticas. Para contribuir:
1. Fork o repositório.
2. Crie uma nova branch.
3. Faça suas modificações.
4. Abra um **pull request** com suas alterações.

## Licença

Este projeto é de código aberto e pode ser modificado ou compartilhado conforme necessário.

---

Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato! 😄
