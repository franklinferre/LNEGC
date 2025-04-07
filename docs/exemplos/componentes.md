# Exemplos de Componentes

## Calculadora

```lnegc
# Calculadora
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2024-04-07
Domínio: Matemática
Tags: matemática, cálculo

## Interface
- Entrada: Dois números (a, b)
- Saída: Resultado da operação
- Exceções: DivisaoPorZeroException

## Algoritmo
1. Receber dois números
2. Realizar a operação
3. Retornar o resultado

## Exemplos
1. Soma: 2 + 3 = 5
2. Subtração: 5 - 3 = 2
3. Multiplicação: 4 * 3 = 12
4. Divisão: 10 / 2 = 5

## Exceções
- DivisaoPorZeroException: Quando o divisor é zero
```

## Validador de Email

```lnegc
# Validador de Email
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2024-04-07
Domínio: Validação
Tags: email, validação

## Interface
- Entrada: String (email)
- Saída: Boolean (válido/inválido)
- Exceções: EmailInvalidoException

## Algoritmo
1. Verificar formato básico (usuario@dominio)
2. Validar caracteres permitidos
3. Verificar domínio válido
4. Retornar resultado

## Exemplos
1. válido: "usuario@dominio.com" -> true
2. inválido: "usuario@" -> false
3. inválido: "@dominio.com" -> false
4. inválido: "usuario@dominio" -> false

## Exceções
- EmailInvalidoException: Quando o formato é inválido
``` 