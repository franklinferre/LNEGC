# Guia de Uso Básico

## Criando um Componente

### 1. Criar Arquivo
Crie um arquivo `.lnegc` para seu componente:

```bash
mkdir -p src/components
touch src/components/calculadora.lnegc
```

### 2. Descrever Componente
Edite o arquivo `calculadora.lnegc`:

```lnegc
# Calculadora
Versão: 1.0.0
Autor: Seu Nome
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
```

### 3. Gerar Código
```bash
lnegc generate src/components/calculadora.lnegc
```

## Criando uma Entidade

### 1. Criar Arquivo
```bash
mkdir -p src/entities
touch src/entities/usuario.lnegc
```

### 2. Descrever Entidade
Edite o arquivo `usuario.lnegc`:

```lnegc
# Usuário
Versão: 1.0.0
Autor: Seu Nome
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

### 3. Gerar Código
```bash
lnegc generate src/entities/usuario.lnegc
```

## Criando uma Interface

### 1. Criar Arquivo
```bash
mkdir -p src/interfaces
touch src/interfaces/repositorio.lnegc
```

### 2. Descrever Interface
Edite o arquivo `repositorio.lnegc`:

```lnegc
# Repositório
Versão: 1.0.0
Autor: Seu Nome
Data: 2024-04-07
Domínio: Persistência
Tags: repositório, persistência

## Descrição
Interface para operações de persistência.

## Métodos
- criar(entidade: Entidade): Entidade
- ler(id: UUID): Entidade
- atualizar(entidade: Entidade): Entidade
- deletar(id: UUID): void
- listar(filtros: Filtros): Entidade[]

## Propriedades
- conexao: Conexao
- logger: Logger
```

### 3. Gerar Código
```bash
lnegc generate src/interfaces/repositorio.lnegc
```

## Validação

### 1. Validar Arquivo
```bash
lnegc validate src/components/calculadora.lnegc
```

### 2. Validar Diretório
```bash
lnegc validate src/components/
```

### 3. Validar Projeto
```bash
lnegc validate
```

## Análise

### 1. Analisar Arquivo
```bash
lnegc analyze src/components/calculadora.lnegc
```

### 2. Analisar Diretório
```bash
lnegc analyze src/components/
```

### 3. Analisar Projeto
```bash
lnegc analyze
```

## Documentação

### 1. Gerar Documentação
```bash
lnegc docs generate
```

### 2. Visualizar Documentação
```bash
lnegc docs serve
```

## Próximos Passos

1. [Guia de Uso Avançado](uso-avancado.md)
2. [Exemplos](exemplos/README.md)
3. [Boas Práticas](boas-praticas/README.md)
4. [Documentação da API](referencias/api.md) 