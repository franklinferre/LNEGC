Contribuindo
===========

Obrigado pelo interesse em contribuir com o LNEGC! Este documento fornece diretrizes e instruções para contribuir com o projeto.

Código de Conduta
--------------

Ao participar deste projeto, você concorda em seguir nosso `Código de Conduta`_.

.. _Código de Conduta: https://github.com/seu-usuario/lnegc/blob/main/CODE_OF_CONDUCT.md

Como Contribuir
-------------

1. **Fork do Repositório**

   Faça um fork do repositório para sua conta no GitHub.

2. **Clone Local**

   .. code-block:: bash

       git clone https://github.com/seu-usuario/lnegc.git
       cd lnegc

3. **Criar Branch**

   .. code-block:: bash

       git checkout -b feature/nome-da-feature
       # ou
       git checkout -b fix/nome-do-fix

4. **Desenvolvimento**

   * Siga as convenções de código
   * Escreva testes para novas funcionalidades
   * Mantenha a documentação atualizada
   * Use commits semânticos

5. **Testes**

   Execute os testes antes de enviar:

   .. code-block:: bash

       python -m pytest
       python -m mypy .
       python -m flake8
       python -m black .
       python -m isort .

6. **Pull Request**

   * Crie um PR para a branch main
   * Descreva as mudanças
   * Referencie issues relacionadas
   * Aguarde review

Convenções de Código
-----------------

1. **Estrutura de Arquivos**

   * Use a estrutura padrão do projeto
   * Mantenha arquivos relacionados juntos
   * Siga as convenções de nomenclatura

2. **Estilo de Código**

   * Siga PEP 8
   * Use type hints
   * Documente funções e classes
   * Mantenha linhas com no máximo 100 caracteres

3. **Testes**

   * Escreva testes para novas funcionalidades
   * Mantenha cobertura acima de 80%
   * Use fixtures quando apropriado
   * Siga o padrão AAA (Arrange, Act, Assert)

4. **Documentação**

   * Mantenha a documentação atualizada
   * Use docstrings em português
   * Documente exemplos de uso
   * Atualize o changelog

Commits
------

Use commits semânticos:

* feat: Nova funcionalidade
* fix: Correção de bug
* docs: Documentação
* style: Formatação
* refactor: Refatoração
* test: Testes
* chore: Manutenção

Exemplo:

.. code-block:: bash

    git commit -m "feat(validador): adiciona validação de CPF"
    git commit -m "fix(api): corrige erro de autenticação"
    git commit -m "docs(readme): atualiza instruções de instalação"

Issues
-----

* Use templates fornecidos
* Seja específico e claro
* Inclua exemplos quando possível
* Referencie PRs relacionados

Pull Requests
-----------

1. **Template**

   * Descrição das mudanças
   * Motivo das mudanças
   * Impacto das mudanças
   * Testes realizados

2. **Review**

   * Aguarde review de pelo menos um mantenedor
   * Responda feedback prontamente
   * Faça ajustes quando necessário
   * Mantenha discussões focadas

3. **Merge**

   * Todos os testes devem passar
   * Documentação deve estar atualizada
   * Código deve estar formatado
   * Commits devem ser semânticos

Desenvolvimento Local
------------------

1. **Ambiente**

   .. code-block:: bash

       python -m venv venv
       source venv/bin/activate  # Linux/macOS
       venv\\Scripts\\activate   # Windows
       pip install -r requirements.txt
       pip install -e .

2. **Testes**

   .. code-block:: bash

       python -m pytest
       python -m pytest --cov=lnegc
       python -m pytest --cov-report=html

3. **Linting**

   .. code-block:: bash

       python -m flake8
       python -m mypy .
       python -m black .
       python -m isort .

4. **Documentação**

   .. code-block:: bash

       cd docs
       make html
       make serve

Releases
-------

1. **Versionamento**

   * Siga Semantic Versioning
   * Atualize CHANGELOG.md
   * Crie tag no GitHub
   * Atualize documentação

2. **Checklist**

   * Todos os testes passam
   * Documentação atualizada
   * Changelog atualizado
   * Tag criada
   * Release publicado

Contato
------

* GitHub Issues: https://github.com/seu-usuario/lnegc/issues
* Email: seu-email@exemplo.com
* Discord: https://discord.gg/seu-servidor

Agradecimentos
------------

* Lista de contribuidores
* Projetos inspiradores
* Comunidade open source 