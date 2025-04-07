# Guia de Contribuição

## Como Contribuir

### 1. Fork do Projeto
1. Acesse o repositório do LNEGC
2. Clique em "Fork"
3. Clone seu fork localmente

### 2. Configurar Ambiente
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/lnegc.git
cd lnegc

# Instale as dependências
npm install

# Execute os testes
npm test
```

### 3. Criar Branch
```bash
# Crie uma branch para sua feature
git checkout -b feature/nome-da-feature

# Ou para correção
git checkout -b fix/nome-do-fix
```

### 4. Desenvolvimento
1. Siga as [boas práticas](boas-praticas/README.md)
2. Escreva testes para novas funcionalidades
3. Mantenha a documentação atualizada
4. Siga o [guia de estilo](boas-praticas/convencoes.md)

### 5. Commits
```bash
# Commits devem seguir o padrão
git commit -m "feat: adiciona nova funcionalidade"
git commit -m "fix: corrige bug na validação"
git commit -m "docs: atualiza documentação"
```

### 6. Pull Request
1. Push para seu fork
2. Crie um Pull Request
3. Descreva as mudanças
4. Aguarde review

## Guia de Estilo

### Código
- Use TypeScript
- Siga o ESLint
- Siga o Prettier
- Documente funções e classes

### Testes
- Testes unitários
- Testes de integração
- Cobertura mínima de 80%
- Testes significativos

### Documentação
- Documentação em português
- Exemplos práticos
- Documentação da API
- Guias de uso

## Estrutura do Projeto

```
lnegc/
├── src/                # Código fonte
│   ├── core/          # Núcleo do sistema
│   ├── parser/        # Parser LNEGC
│   ├── validator/     # Validações
│   ├── generator/     # Geração de código
│   └── cli/           # Interface de linha de comando
├── tests/             # Testes
│   ├── unit/          # Testes unitários
│   ├── integration/   # Testes de integração
│   └── e2e/           # Testes end-to-end
├── docs/              # Documentação
│   ├── api/           # Documentação da API
│   ├── guides/        # Guias de uso
│   └── examples/      # Exemplos
└── examples/          # Exemplos de uso
```

## Processo de Desenvolvimento

### 1. Planejamento
1. Identifique a necessidade
2. Descreva a solução
3. Defina os requisitos
4. Planeje os testes

### 2. Implementação
1. Siga o TDD
2. Implemente a funcionalidade
3. Escreva os testes
4. Documente o código

### 3. Review
1. Auto-review do código
2. Review por pares
3. Ajustes necessários
4. Aprovação final

### 4. Integração
1. Merge para develop
2. Testes de integração
3. Deploy para staging
4. Testes em produção

## Reportando Problemas

### Issues
1. Use o template de issue
2. Descreva o problema
3. Forneça exemplos
4. Adicione logs

### Bug Reports
```markdown
## Descrição
Descrição clara do bug

## Passos para Reproduzir
1. Passo 1
2. Passo 2
3. Passo 3

## Comportamento Esperado
O que deveria acontecer

## Comportamento Atual
O que está acontecendo

## Ambiente
- Sistema Operacional:
- Node.js:
- npm:
- LNEGC:

## Logs
Logs relevantes
```

### Feature Requests
```markdown
## Descrição
Descrição clara da feature

## Justificativa
Por que esta feature é necessária

## Exemplos de Uso
Como a feature seria usada

## Alternativas Consideradas
Outras abordagens consideradas
```

## Comunidade

### Canais
- GitHub Issues
- GitHub Discussions
- Discord
- Email

### Eventos
- Meetups
- Workshops
- Conferências
- Hackathons

### Recursos
- Blog
- Newsletter
- Documentação
- Tutoriais

## Licença

### Código
- MIT License
- Atribuição necessária
- Sem garantias
- Sem responsabilidades

### Documentação
- CC BY 4.0
- Atribuição necessária
- Compartilhamento permitido
- Modificação permitida

## Próximos Passos

1. [Guia de Instalação](guias/instalacao.md)
2. [Guia de Uso Básico](guias/uso-basico.md)
3. [Guia de Uso Avançado](guias/uso-avancado.md)
4. [Documentação da API](api.md) 