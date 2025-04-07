Instalação
==========

Requisitos do Sistema
------------------

Antes de instalar o LNEGC, certifique-se de que seu sistema atende aos seguintes requisitos:

* Python 3.8 ou superior
* pip (gerenciador de pacotes Python)
* Git (para controle de versão)
* Ambiente virtual Python (recomendado)

Instalação via pip
----------------

A forma mais simples de instalar o LNEGC é através do pip:

.. code-block:: bash

    pip install lnegc

Instalação a partir do Código Fonte
--------------------------------

Para instalar a versão mais recente do código fonte:

1. Clone o repositório:

   .. code-block:: bash

       git clone https://github.com/seu-usuario/lnegc.git
       cd lnegc

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

   .. code-block:: bash

       python -m venv venv
       source venv/bin/activate  # Linux/macOS
       venv\\Scripts\\activate   # Windows

3. Instale as dependências:

   .. code-block:: bash

       pip install -r requirements.txt

4. Instale o pacote em modo de desenvolvimento:

   .. code-block:: bash

       pip install -e .

Verificando a Instalação
---------------------

Para verificar se a instalação foi bem-sucedida:

.. code-block:: bash

    python -c "import lnegc; print(lnegc.__version__)"

Configuração do Ambiente
---------------------

1. **Configuração do Editor**

   Recomendamos usar um editor de texto ou IDE com suporte a:
   
   * Realce de sintaxe Python
   * Integração com linters (flake8, mypy)
   * Formatação automática (black, isort)

2. **Configuração do Git**

   Configure seu Git com suas credenciais:

   .. code-block:: bash

       git config --global user.name "Seu Nome"
       git config --global user.email "seu.email@exemplo.com"

3. **Variáveis de Ambiente**

   Se necessário, configure as seguintes variáveis de ambiente:

   .. code-block:: bash

       export LNEGC_HOME=/caminho/para/lnegc
       export PYTHONPATH=$PYTHONPATH:$LNEGC_HOME

Estrutura de Diretórios
---------------------

Após a instalação, você terá a seguinte estrutura de diretórios:

.. code-block:: text

    lnegc/
    ├── componentes/     # Componentes reutilizáveis
    ├── entidades/       # Definições de entidades
    ├── interfaces/      # Definições de interfaces
    ├── testes/         # Especificações de testes
    ├── config.lnegc    # Configuração global do projeto
    ├── docs/           # Documentação
    ├── tests/          # Testes unitários e de integração
    └── requirements.txt # Dependências do projeto

Próximos Passos
-------------

Após a instalação, recomendamos:

1. Ler a documentação de uso
2. Explorar os exemplos fornecidos
3. Configurar seu ambiente de desenvolvimento
4. Começar a criar seus próprios arquivos LNEGC

Solução de Problemas
------------------

Se encontrar problemas durante a instalação:

1. Verifique se todos os requisitos do sistema foram atendidos
2. Certifique-se de que seu ambiente virtual está ativo
3. Verifique se todas as dependências foram instaladas corretamente
4. Consulte os logs de erro para mais detalhes

Para mais ajuda, consulte:

* A seção de issues no GitHub
* A documentação online
* O fórum da comunidade 