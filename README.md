# LNEGC - Linguagem Natural Estruturada para Geração de Código

LNEGC é uma linguagem e ferramenta que permite gerar código a partir de descrições em linguagem natural estruturada.

## Visão Geral

O LNEGC permite que você:

- Descreva componentes, entidades e interfaces em linguagem natural
- Gere código automaticamente a partir dessas descrições
- Mantenha documentação sempre atualizada
- Siga padrões e boas práticas consistentemente

## Instalação

```bash
npm install -g lnegc
# ou
yarn global add lnegc
```

## Uso Básico

1. Criar um arquivo `.lnegc`:

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
├── docs/                    # Documentação
│   ├── README.md           # Documentação principal
│   ├── INDEX.md            # Índice da documentação
│   ├── ESTRUTURA.md        # Estrutura do projeto
│   ├── GUIAS.md            # Guias de uso
│   ├── EXEMPLOS.md         # Exemplos
│   ├── BOAS_PRATICAS.md    # Boas práticas
│   ├── TEMPLATES.md        # Templates
│   ├── ESPECIFICACAO.md    # Especificação
│   ├── GRAMATICA.md        # Gramática formal
│   ├── PROCESSADOR.md      # Especificação do processador
│   ├── PROMPTS.md          # Especificação dos prompts
│   └── VANTAGENS.md        # Vantagens
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

## Documentação

- [Índice](docs/INDEX.md)
- [Estrutura](docs/ESTRUTURA.md)
- [Guias](docs/GUIAS.md)
- [Exemplos](docs/EXEMPLOS.md)
- [Boas Práticas](docs/BOAS_PRATICAS.md)
- [Templates](docs/TEMPLATES.md)
- [Especificação](docs/ESPECIFICACAO.md)
- [Gramática](docs/GRAMATICA.md)
- [Processador](docs/PROCESSADOR.md)
- [Prompts](docs/PROMPTS.md)
- [Vantagens](docs/VANTAGENS.md)

## Contribuição

1. Fork o projeto
2. Crie sua branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Feat: adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes. 