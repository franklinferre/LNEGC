# Guia de Instalação

## Requisitos

### Sistema
- Node.js 18+
- npm 9+ ou yarn 1.22+
- Git 2.30+

### IDE (Recomendado)
- Visual Studio Code
- IntelliJ IDEA
- Eclipse

## Instalação Global

### Usando npm
```bash
npm install -g lnegc
```

### Usando yarn
```bash
yarn global add lnegc
```

## Instalação Local

### Usando npm
```bash
npm install lnegc --save-dev
```

### Usando yarn
```bash
yarn add lnegc --dev
```

## Verificação

### Versão
```bash
lnegc --version
```

### Ajuda
```bash
lnegc --help
```

## Configuração Inicial

### 1. Criar Diretório do Projeto
```bash
mkdir meu-projeto
cd meu-projeto
```

### 2. Inicializar Projeto
```bash
lnegc init
```

### 3. Configurar Projeto
Edite o arquivo `.lnegc/config.lnegc`:
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

## Descrição
Descrição geral do projeto.
```

## Extensões de IDE

### Visual Studio Code
1. Abra o VS Code
2. Vá para a aba de extensões
3. Pesquise por "LNEGC"
4. Instale a extensão oficial

### IntelliJ IDEA
1. Abra o IntelliJ IDEA
2. Vá para Settings > Plugins
3. Pesquise por "LNEGC"
4. Instale o plugin oficial

### Eclipse
1. Abra o Eclipse
2. Vá para Help > Eclipse Marketplace
3. Pesquise por "LNEGC"
4. Instale o plugin oficial

## Configuração do Git

### 1. Inicializar Repositório
```bash
git init
```

### 2. Criar .gitignore
```bash
cat > .gitignore << 'EOF'
node_modules/
.env
*.log
generated/
EOF
```

### 3. Primeiro Commit
```bash
git add .
git commit -m "feat: initial commit"
```

## Próximos Passos

1. [Guia de Uso Básico](uso-basico.md)
2. [Exemplos](exemplos/README.md)
3. [Boas Práticas](boas-praticas/README.md)
4. [Documentação da API](referencias/api.md) 