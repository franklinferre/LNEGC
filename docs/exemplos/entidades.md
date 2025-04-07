# Exemplos de Entidades

## Usuário

```lnegc
# Usuário
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2024-04-07
Domínio: Usuários
Tags: usuário, autenticação

## Descrição
Entidade que representa um usuário do sistema.

## Atributos
- id: UUID (obrigatório)
- nome: String (obrigatório)
- email: String (obrigatório)
- senha: String (obrigatório)
- ativo: Boolean (obrigatório)
- dataCriacao: DateTime (obrigatório)
- dataAtualizacao: DateTime (opcional)

## Relacionamentos
- Perfil: OneToOne
- Permissões: ManyToMany

## Validações
- Email deve ser único
- Senha deve ter mínimo 8 caracteres
- Nome não pode ser vazio
```

## Produto

```lnegc
# Produto
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2024-04-07
Domínio: Produtos
Tags: produto, estoque

## Descrição
Entidade que representa um produto no sistema.

## Atributos
- id: UUID (obrigatório)
- codigo: String (obrigatório)
- nome: String (obrigatório)
- descricao: String (opcional)
- preco: Decimal (obrigatório)
- quantidade: Integer (obrigatório)
- categoria: String (obrigatório)
- dataCriacao: DateTime (obrigatório)
- dataAtualizacao: DateTime (opcional)

## Relacionamentos
- Categoria: ManyToOne
- Vendas: OneToMany

## Validações
- Código deve ser único
- Preço deve ser maior que zero
- Quantidade não pode ser negativa
``` 