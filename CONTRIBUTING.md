# Guia de Contribuição

Obrigado por investir seu tempo em contribuir para o projeto! Qualquer contribuição que você fizer será refletida no [LNEGC](https://github.com/franklinferre/LNEGC) 🎉

## Começando

### Issues

#### Criar uma Nova Issue

Se você encontrar um problema ou tiver uma sugestão para o LNEGC, verifique se já existe uma issue sobre isso. Se não existir, você pode abrir uma nova issue usando um dos templates fornecidos:

* [🐛 Reportar Bug](.github/ISSUE_TEMPLATE/bug_report.md)
* [🚀 Sugestão de Feature](.github/ISSUE_TEMPLATE/feature_request.md)

### Fazer Mudanças Localmente

1. Fork o repositório.

2. Instale as dependências de desenvolvimento:
   ```bash
   pip install -e ".[dev]"
   ```

3. Crie um branch de trabalho:
   ```bash
   git checkout -b nome-da-feature
   ```

### Fazer Mudanças

1. Faça suas mudanças:
   * Mantenha suas mudanças focadas em um único aspecto
   * Desenvolva features em branches separados
   * Adicione testes quando relevante
   * Atualize a documentação conforme necessário

2. Execute os testes:
   ```bash
   pytest
   ```

3. Execute o linting:
   ```bash
   flake8
   black .
   isort .
   ```

### Commit suas Atualizações

Commit Message Format:
\`\`\`
<tipo>(<escopo>): <descrição>

[corpo]

[rodapé]
\`\`\`

Tipos:
* feat: Nova feature
* fix: Correção de bug
* docs: Mudanças na documentação
* style: Formatação, ponto e vírgula faltando, etc
* refactor: Refatoração de código
* test: Adicionando testes
* chore: Atualização de tarefas de build, configurações, etc

Exemplo:
\`\`\`
feat(parser): adiciona suporte para arrays

Adiciona capacidade de parsear arrays na linguagem LNEGC.
Arrays podem ser definidos usando a sintaxe [item1, item2].

Closes #123
\`\`\`

### Pull Request

Quando você terminar suas mudanças:

1. Execute todos os testes e linting
2. Atualize a documentação se necessário
3. Crie um pull request usando o template fornecido
4. Não se esqueça de linkar o PR à issue se você estiver resolvendo uma
5. Habilite a opção "Allow maintainer edits" 
6. Aguarde a review

## Guia de Estilo

### Convenções de Código

* Use Python 3.10+
* Siga PEP 8
* Use type hints
* Documente usando docstrings no formato Google
* Mantenha funções pequenas e focadas
* Escreva testes para novas features

### Git Commit Messages

* Use o tempo presente ("Adiciona feature" não "Adicionou feature")
* Use o modo imperativo ("Mova o cursor para..." não "Moveu o cursor para...")
* Limite a primeira linha a 72 caracteres
* Referencie issues e pull requests livremente após a primeira linha

## Recursos Adicionais

* [Documentação do Projeto](docs/README.md)
* [Código de Conduta](CODE_OF_CONDUCT.md)
* [Guia de Segurança](SECURITY.md) 