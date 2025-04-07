# Documentação da API

## Comandos

### generate
Gera código a partir de arquivos `.lnegc`.

```bash
lnegc generate [opções] <arquivo|diretorio>
```

#### Opções
- `--template <nome>`: Usa um template específico
- `--output <diretorio>`: Define o diretório de saída
- `--language <linguagem>`: Define a linguagem alvo
- `--framework <framework>`: Define o framework alvo
- `--verbose`: Exibe informações detalhadas
- `--debug`: Modo debug

#### Exemplos
```bash
# Gerar a partir de um arquivo
lnegc generate src/components/calculadora.lnegc

# Gerar a partir de um diretório
lnegc generate src/components/

# Usar template específico
lnegc generate --template componente src/components/novo.lnegc

# Definir linguagem e framework
lnegc generate --language typescript --framework react src/components/novo.lnegc
```

### validate
Valida arquivos `.lnegc`.

```bash
lnegc validate [opções] <arquivo|diretorio>
```

#### Opções
- `--rules <arquivo>`: Define arquivo de regras
- `--verbose`: Exibe informações detalhadas
- `--debug`: Modo debug

#### Exemplos
```bash
# Validar um arquivo
lnegc validate src/components/calculadora.lnegc

# Validar um diretório
lnegc validate src/components/

# Usar regras personalizadas
lnegc validate --rules .lnegc/rules.js src/components/
```

### analyze
Analisa arquivos `.lnegc`.

```bash
lnegc analyze [opções] <arquivo|diretorio>
```

#### Opções
- `--metrics <arquivo>`: Define arquivo de métricas
- `--output <arquivo>`: Define arquivo de saída
- `--format <formato>`: Define formato de saída
- `--verbose`: Exibe informações detalhadas
- `--debug`: Modo debug

#### Exemplos
```bash
# Analisar um arquivo
lnegc analyze src/components/calculadora.lnegc

# Analisar um diretório
lnegc analyze src/components/

# Usar métricas personalizadas
lnegc analyze --metrics .lnegc/metrics.js src/components/

# Exportar relatório
lnegc analyze --output relatorio.json --format json src/components/
```

### docs
Gerencia documentação.

```bash
lnegc docs <comando> [opções]
```

#### Comandos
- `generate`: Gera documentação
- `serve`: Inicia servidor de documentação
- `export`: Exporta documentação

#### Opções
- `--output <diretorio>`: Define diretório de saída
- `--format <formato>`: Define formato de saída
- `--port <porta>`: Define porta do servidor
- `--verbose`: Exibe informações detalhadas
- `--debug`: Modo debug

#### Exemplos
```bash
# Gerar documentação
lnegc docs generate

# Iniciar servidor
lnegc docs serve --port 3000

# Exportar documentação
lnegc docs export --format html
```

### logs
Gerencia logs.

```bash
lnegc logs <comando> [opções]
```

#### Comandos
- `show`: Exibe logs
- `clear`: Limpa logs
- `export`: Exporta logs

#### Opções
- `--output <arquivo>`: Define arquivo de saída
- `--format <formato>`: Define formato de saída
- `--level <nivel>`: Define nível de log
- `--verbose`: Exibe informações detalhadas
- `--debug`: Modo debug

#### Exemplos
```bash
# Exibir logs
lnegc logs show

# Limpar logs
lnegc logs clear

# Exportar logs
lnegc logs export --format json
```

### cache
Gerencia cache.

```bash
lnegc cache <comando> [opções]
```

#### Comandos
- `clear`: Limpa cache
- `rebuild`: Reconstrói cache
- `status`: Exibe status do cache

#### Opções
- `--verbose`: Exibe informações detalhadas
- `--debug`: Modo debug

#### Exemplos
```bash
# Limpar cache
lnegc cache clear

# Reconstruir cache
lnegc cache rebuild

# Ver status
lnegc cache status
```

## Configuração

### Arquivo de Configuração
O arquivo `.lnegc/config.lnegc` define as configurações do projeto:

```lnegc
# Nome do Projeto
Versão: 1.0.0
Autor: Seu Nome
Data: 2024-04-07
Domínio: Seu Domínio
Tags: tag1, tag2

## CONFIGURAÇÕES
- Nome: Nome do Projeto
- Linguagem: python  # ou typescript, java, etc.
- Framework: FastAPI  # opcional
- Banco de Dados: PostgreSQL  # opcional

## PLUGINS
- plugin1
- plugin2

## HOOKS
- beforeGenerate: scripts/before-generate.js
- afterGenerate: scripts/after-generate.js
- beforeValidate: scripts/before-validate.js
- afterValidate: scripts/after-validate.js

## VALIDAÇÕES
- regra1: scripts/validacoes/regra1.js
- regra2: scripts/validacoes/regra2.js

## MÉTRICAS
- metrica1: scripts/metricas/metrica1.js
- metrica2: scripts/metricas/metrica2.js

## Descrição
Descrição geral do projeto.
```

## Plugins

### Estrutura
```javascript
module.exports = {
  name: 'nome-do-plugin',
  version: '1.0.0',
  hooks: {
    beforeGenerate: async (context) => {
      // Lógica antes da geração
    },
    afterGenerate: async (context) => {
      // Lógica depois da geração
    }
  }
};
```

### Contexto
O objeto `context` contém:
- `file`: Informações do arquivo
- `config`: Configurações do projeto
- `logger`: Logger do sistema
- `cache`: Cache do sistema

## Hooks

### Estrutura
```javascript
module.exports = async (context) => {
  // Lógica do hook
};
```

### Tipos
- `beforeGenerate`: Executado antes da geração
- `afterGenerate`: Executado depois da geração
- `beforeValidate`: Executado antes da validação
- `afterValidate`: Executado depois da validação

## Validações

### Estrutura
```javascript
module.exports = {
  validate: (context) => {
    // Lógica de validação
  },
  message: 'Mensagem de erro'
};
```

### Retorno
- `true`: Validação passou
- `false`: Validação falhou
- `string`: Mensagem de erro

## Métricas

### Estrutura
```javascript
module.exports = {
  analyze: (context) => {
    // Lógica de análise
  },
  report: (results) => {
    // Geração de relatório
  }
};
```

### Retorno
- `object`: Resultados da análise
- `string`: Relatório formatado 