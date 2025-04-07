# Exemplos de Fluxos

## Processamento de Pedido

```lnegc
# Processamento de Pedido
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2024-04-07
Domínio: Vendas
Tags: pedido, processamento

## Descrição
Fluxo de processamento de um pedido de venda.

## Passos
1. Validar dados do pedido
2. Verificar estoque
3. Processar pagamento
4. Atualizar estoque
5. Enviar confirmação

## Validações
- Dados do pedido devem ser válidos
- Produtos devem estar em estoque
- Pagamento deve ser aprovado

## Exceções
- EstoqueInsuficienteException
- PagamentoRecusadoException
- DadosInvalidosException

## Exemplos
1. Pedido válido com estoque e pagamento aprovado
2. Pedido com estoque insuficiente
3. Pedido com pagamento recusado
```

## Cadastro de Usuário

```lnegc
# Cadastro de Usuário
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2024-04-07
Domínio: Usuários
Tags: cadastro, usuário

## Descrição
Fluxo de cadastro de um novo usuário.

## Passos
1. Validar dados do usuário
2. Verificar email único
3. Criptografar senha
4. Criar perfil
5. Enviar email de confirmação

## Validações
- Email deve ser único
- Senha deve atender requisitos
- Dados obrigatórios preenchidos

## Exceções
- EmailJaCadastradoException
- SenhaInvalidaException
- DadosIncompletosException

## Exemplos
1. Cadastro com dados válidos
2. Cadastro com email já existente
3. Cadastro com senha inválida
``` 