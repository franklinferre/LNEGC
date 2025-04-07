# Guia de Uso Avançado

## Templates Personalizados

### 1. Criar Template
```bash
mkdir -p .lnegc/templates
touch .lnegc/templates/componente.lnegc
```

### 2. Definir Template
Edite o arquivo `componente.lnegc`:

```lnegc
# Template de Componente
Versão: 1.0.0
Autor: Seu Nome
Data: 2024-04-07
Domínio: Templates
Tags: template, componente

## Estrutura
- Nome do Componente
- Versão
- Autor
- Data
- Domínio
- Tags

## Seções
- Interface
- Algoritmo
- Exemplos
- Exceções
```

### 3. Usar Template
```bash
lnegc generate --template componente src/components/novo.lnegc
```

## Plugins

### 1. Criar Plugin
```bash
mkdir -p .lnegc/plugins
touch .lnegc/plugins/meu-plugin.js
```

### 2. Implementar Plugin
```javascript
module.exports = {
  name: 'meu-plugin',
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

### 3. Ativar Plugin
Edite o arquivo `.lnegc/config.lnegc`:

```lnegc
## PLUGINS
- meu-plugin
```

## Hooks

### 1. Definir Hooks
Edite o arquivo `.lnegc/config.lnegc`:

```lnegc
## HOOKS
- beforeGenerate: scripts/before-generate.js
- afterGenerate: scripts/after-generate.js
- beforeValidate: scripts/before-validate.js
- afterValidate: scripts/after-validate.js
```

### 2. Implementar Scripts
```bash
mkdir -p scripts
touch scripts/before-generate.js
```

```javascript
module.exports = async (context) => {
  // Lógica antes da geração
};
```

## Validação Avançada

### 1. Regras Personalizadas
Edite o arquivo `.lnegc/config.lnegc`:

```lnegc
## VALIDAÇÕES
- regra1: scripts/validacoes/regra1.js
- regra2: scripts/validacoes/regra2.js
```

### 2. Implementar Regras
```javascript
module.exports = {
  validate: (context) => {
    // Lógica de validação
  },
  message: 'Mensagem de erro'
};
```

## Análise Avançada

### 1. Métricas Personalizadas
Edite o arquivo `.lnegc/config.lnegc`:

```lnegc
## MÉTRICAS
- metrica1: scripts/metricas/metrica1.js
- metrica2: scripts/metricas/metrica2.js
```

### 2. Implementar Métricas
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

## Integração com IDEs

### Visual Studio Code
1. Configurar tasks
2. Definir snippets
3. Configurar debug
4. Personalizar extensão

### IntelliJ IDEA
1. Configurar run configurations
2. Definir live templates
3. Configurar debug
4. Personalizar plugin

### Eclipse
1. Configurar launch configurations
2. Definir code templates
3. Configurar debug
4. Personalizar plugin

## Integração com CI/CD

### GitHub Actions
```yaml
name: LNEGC
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
      - run: npm install -g lnegc
      - run: lnegc validate
```

### GitLab CI
```yaml
validate:
  image: node:18
  script:
    - npm install -g lnegc
    - lnegc validate
```

### Jenkins
```groovy
pipeline {
  agent any
  stages {
    stage('Validate') {
      steps {
        sh 'npm install -g lnegc'
        sh 'lnegc validate'
      }
    }
  }
}
```

## Troubleshooting

### Logs
```bash
# Ver logs
lnegc logs

# Limpar logs
lnegc logs clear

# Exportar logs
lnegc logs export
```

### Debug
```bash
# Modo debug
lnegc --debug generate

# Log detalhado
lnegc --verbose generate
```

### Cache
```bash
# Limpar cache
lnegc cache clear

# Reconstruir cache
lnegc cache rebuild
```

## Próximos Passos

1. [Exemplos](exemplos/README.md)
2. [Boas Práticas](boas-praticas/README.md)
3. [Documentação da API](referencias/api.md)
4. [Contribuindo](referencias/contribuindo.md) 