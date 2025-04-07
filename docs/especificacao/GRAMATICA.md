# Gramática Formal LNEGC

Este documento define a gramática formal da Linguagem Natural Estruturada para Geração de Código (LNEGC) usando a notação BNF (Backus-Naur Form).

## 1. Estrutura Básica

```
arquivo ::= cabecalho secoes

cabecalho ::= "#" nome "\n"
             "Versão:" versao "\n"
             "Autor:" autor "\n"
             "Data:" data "\n"
             "Domínio:" dominio "\n"
             "Tags:" tags "\n"

nome ::= texto
versao ::= numero "." numero "." numero
autor ::= texto
data ::= ano "-" mes "-" dia
dominio ::= texto
tags ::= tag ("," tag)*
tag ::= texto

secoes ::= secao*
secao ::= "##" nome_secao "\n" conteudo
nome_secao ::= texto
conteudo ::= (linha | subsecao)*
subsecao ::= "###" nome_subsecao "\n" conteudo
nome_subsecao ::= texto
```

## 2. Tipos de Dados

```
tipo ::= tipo_basico | tipo_composto

tipo_basico ::= "string" | "number" | "boolean" | "date" | "datetime" | "array" | "object"

tipo_composto ::= enum | interface | type | class

enum ::= "enum" "{" valores "}"
valores ::= valor ("," valor)*
valor ::= texto

interface ::= "interface" "{" membros "}"
membros ::= membro*
membro ::= propriedade | metodo

type ::= "type" nome "=" tipo

class ::= "class" nome "{" implementacao "}"
implementacao ::= (propriedade | metodo)*
```

## 3. Declarações

```
declaracao ::= definicao | acao | condicao | iteracao

definicao ::= "Definir" sujeito "como" tipo
sujeito ::= texto

acao ::= verbo objeto
verbo ::= texto
objeto ::= texto

condicao ::= "Se" expressao "então" acoes
             ("Senão se" expressao "então" acoes)*
             ("Senão" acoes)?
expressao ::= texto
acoes ::= acao+

iteracao ::= "Para cada" item "em" colecao "," acoes
item ::= texto
colecao ::= texto
```

## 4. Propriedades

```
propriedade ::= entidade "tem" nome "como" tipo
                (restricoes)?
entidade ::= texto
nome ::= texto
restricoes ::= "com" restricao ("," restricao)*
restricao ::= texto
```

## 5. Relacionamentos

```
relacionamento ::= entidade_a "se relaciona com" entidade_b "como" tipo
entidade_a ::= texto
entidade_b ::= texto
tipo ::= "um-para-um" | "um-para-muitos" | "muitos-para-muitos"
```

## 6. Validações

```
validacao ::= atributo "deve" regra
atributo ::= texto
regra ::= regra_simples | regra_composta

regra_simples ::= texto

regra_composta ::= regra_simples operador regra_simples
operador ::= "e" | "ou" | "não"
```

## 7. Exceções

```
excecao ::= nome_excecao ":" "quando" condicao
nome_excecao ::= texto
condicao ::= texto

tratamento ::= "Se" condicao "então lançar" excecao
```

## 8. Exemplos

```
exemplo ::= numero "." "Exemplo:" descricao "\n"
           entrada "\n"
           saida "\n"
           descricao_exemplo

numero ::= digito+
descricao ::= texto
entrada ::= "Entrada:" valores
valores ::= valor ("," valor)*
valor ::= nome "=" valor_literal
valor_literal ::= texto | numero | booleano | objeto | array
saida ::= "Saída:" valores
descricao_exemplo ::= "Descrição:" texto
```

## 9. APIs

```
api ::= endpoint*

endpoint ::= "###" nome "\n"
            metodo "\n"
            path "\n"
            parametros "\n"
            respostas "\n"
            exemplo?

metodo ::= "Método:" ("GET" | "POST" | "PUT" | "DELETE" | "PATCH")
path ::= "Path:" texto
parametros ::= "Parâmetros:" parametro*
parametro ::= "-" nome ":" tipo "(" origem ")"
origem ::= "body" | "query" | "path" | "header"
respostas ::= "Respostas:" resposta*
resposta ::= "-" codigo ":" descricao
codigo ::= numero
exemplo ::= "Exemplo:" "\n" "```" texto "```"
```

## 10. Fluxos

```
fluxo ::= entrada "\n"
         saida "\n"
         passos "\n"
         excecoes "\n"
         exemplos

entrada ::= "## Entrada" "\n" definicoes
definicoes ::= definicao*

saida ::= "## Saída" "\n" definicoes

passos ::= "## Passos" "\n" passo*
passo ::= numero "." nome "\n" acoes

excecoes ::= "## Exceções" "\n" excecao*

exemplos ::= "## Exemplos" "\n" exemplo*
```

## 11. Testes

```
teste ::= cenarios "\n"
         mocks "\n"
         stubs

cenarios ::= "## Cenários" "\n" cenario*
cenario ::= "###" nome "\n" pre_condicoes "\n" passos "\n" resultado

pre_condicoes ::= "1. Pré-condições:" "\n" condicao*
condicao ::= "-" texto

passos ::= "2. Passos:" "\n" passo*
passo ::= "-" texto

resultado ::= "3. Resultado Esperado:" "\n" expectativa*
expectativa ::= "-" texto

mocks ::= "## Mocks" "\n" mock*
mock ::= "-" nome ":" "\n" comportamento*
comportamento ::= "  -" texto

stubs ::= "## Stubs" "\n" stub*
stub ::= "-" nome ":" "\n" comportamento*
``` 