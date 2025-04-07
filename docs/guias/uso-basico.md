# Guia de Uso Básico

Este guia apresenta os conceitos básicos e primeiros passos para começar a usar o LNEGC.

## Estrutura do Projeto

```
projeto/
├── .lnegc/                  # Configurações do LNEGC
│   ├── config.lnegc         # Configuração global
│   ├── rules.lnegc          # Regras do projeto
│   └── templates/           # Templates personalizados
│
├── src/                     # Código fonte
│   ├── components/          # Componentes
│   │   └── *.lnegc         # Arquivos de componentes
│   ├── entities/           # Entidades
│   │   └── *.lnegc         # Arquivos de entidades
│   ├── interfaces/         # Interfaces
│   │   └── *.lnegc         # Arquivos de interfaces
│   └── tests/              # Testes
│       └── *.lnegc         # Arquivos de teste
│
├── generated/              # Código gerado
│   ├── components/         # Componentes gerados
│   ├── entities/          # Entidades geradas
│   ├── interfaces/        # Interfaces geradas
│   └── tests/             # Testes gerados
│
├── .gitignore             # Arquivos ignorados pelo Git
├── package.json           # Dependências e scripts
└── README.md              # Documentação do projeto
```

## Configuração Inicial

1. Criar diretório do projeto:
```bash
mkdir meu-projeto
cd meu-projeto
```

2. Inicializar projeto:
```bash
lnegc init
```

3. Configurar arquivo `.lnegc/config.lnegc`:
```lnegc
# Configuração do Projeto

## Metadados
- **Nome**: Meu Projeto
- **Versão**: 1.0.0
- **Autor**: João Silva
- **Domínio**: exemplo.com
- **Tags**: web, api, backend

## Configurações
- **Linguagem**: TypeScript
- **Framework**: Node.js
- **Banco de Dados**: PostgreSQL
- **Testes**: Jest
```

## Exemplo de Uso

1. Criar componente:
```lnegc
# Calculadora

Este componente implementa operações matemáticas básicas.

## Interface
```typescript
interface Calculadora {
    soma(a: number, b: number): number;
    subtracao(a: number, b: number): number;
    multiplicacao(a: number, b: number): number;
    divisao(a: number, b: number): number;
}
```

## Algoritmo
1. Receber operação e operandos
2. Validar operandos
3. Executar operação
4. Retornar resultado

## Exemplos
```typescript
const calc = new Calculadora();
const resultado = calc.soma(5, 3);
console.log(resultado); // 8
```
```

2. Gerar código:
```bash
lnegc generate src/components/calculadora.lnegc
```

3. Validar código:
```bash
lnegc validate src/components/calculadora.lnegc
```

4. Analisar código:
```bash
lnegc analyze src/components/calculadora.lnegc
```

## Vantagens

- **Produtividade**: Gere código rapidamente a partir de descrições
- **Qualidade**: Siga padrões e boas práticas consistentemente
- **Manutenibilidade**: Documentação sempre atualizada
- **Colaboração**: Linguagem comum para toda a equipe
- **Escalabilidade**: Estrutura organizada e extensível

## Próximos Passos

- [Uso Avançado](uso-avancado.md)
- [API](../referencias/api.md)
- [Exemplos](../exemplos/)
- [Boas Práticas](../boas-praticas/)

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