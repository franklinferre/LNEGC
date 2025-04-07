API
===

Esta seção documenta a API do processador LNEGC.

Classes Principais
---------------

LNEGCParser
^^^^^^^^^^

.. py:class:: LNEGCParser(file_path: str)

   Parser para arquivos LNEGC.

   :param file_path: Caminho do arquivo LNEGC a ser processado.
   :type file_path: str

   .. py:method:: parse() -> Dict[str, Any]

      Analisa o arquivo LNEGC e extrai metadados e seções.

      :return: Dicionário contendo metadados e seções do arquivo.
      :rtype: Dict[str, Any]

      Exemplo de retorno:

      .. code-block:: python

          {
              'metadata': {
                  'nome': 'Nome do Componente',
                  'versao': '1.0.0',
                  'autor': 'Nome do Autor',
                  'data': '2023-10-15',
                  'dominio': 'Domínio do Componente',
                  'tags': ['tag1', 'tag2']
              },
              'sections': {
                  'Descrição': 'Texto da descrição...',
                  'Interface': 'Definição da interface...',
                  'Algoritmo': 'Passos do algoritmo...'
              },
              'file_path': '/caminho/do/arquivo.lnegc'
          }

LNEGCProcessor
^^^^^^^^^^^^

.. py:class:: LNEGCProcessor(base_dir: str)

   Processador para arquivos LNEGC.

   :param base_dir: Diretório base contendo os arquivos LNEGC.
   :type base_dir: str

   .. py:method:: process_all() -> Dict[str, Any]

      Processa todos os arquivos LNEGC no diretório base.

      :return: Dicionário contendo todos os componentes processados.
      :rtype: Dict[str, Any]

      Exemplo de retorno:

      .. code-block:: python

          {
              'config': {...},
              'components': [...],
              'entities': [...],
              'interfaces': [...],
              'tests': [...]
          }

   .. py:method:: generate_prompt(target_language: str = 'python') -> str

      Gera um prompt estruturado para alimentar sistemas de IA.

      :param target_language: Linguagem alvo para geração de código.
      :type target_language: str
      :return: Prompt formatado para o sistema de IA.
      :rtype: str

Uso via Linha de Comando
---------------------

O processador LNEGC pode ser usado via linha de comando:

.. code-block:: bash

    python lnegc_processor.py [opções]

Opções:
^^^^^^^

--dir DIR           Diretório base com arquivos LNEGC (padrão: 'lnegc')
--output OUTPUT     Arquivo de saída para o prompt (padrão: 'prompt.txt')
--language LANG     Linguagem alvo para geração de código (padrão: 'python')

Exemplos de Uso
------------

1. **Processamento Básico**:

   .. code-block:: python

       from lnegc import LNEGCProcessor

       # Criar processador
       processor = LNEGCProcessor('lnegc')

       # Processar arquivos
       result = processor.process_all()

       # Gerar prompt
       prompt = processor.generate_prompt('python')

2. **Processamento de Arquivo Único**:

   .. code-block:: python

       from lnegc import LNEGCParser

       # Criar parser
       parser = LNEGCParser('lnegc/componentes/validador_cpf.lnegc')

       # Processar arquivo
       result = parser.parse()

3. **Uso via CLI**:

   .. code-block:: bash

       # Processar diretório padrão
       python lnegc_processor.py

       # Especificar diretório e linguagem
       python lnegc_processor.py --dir meu_projeto --language java

       # Especificar arquivo de saída
       python lnegc_processor.py --output meu_prompt.txt

Formatos de Arquivo
----------------

1. **Arquivo de Componente**:

   .. code-block:: text

       # Nome do Componente
       Versão: 1.0.0
       Autor: Nome do Autor
       Data: YYYY-MM-DD
       Domínio: Domínio
       Tags: tag1, tag2

       ## Descrição
       Descrição do componente.

       ## Interface
       Definição da interface.

       ## Algoritmo
       Passos do algoritmo.

2. **Arquivo de Entidade**:

   .. code-block:: text

       # Nome da Entidade
       Versão: 1.0.0
       Autor: Nome do Autor
       Data: YYYY-MM-DD
       Domínio: Domínio
       Tags: tag1, tag2

       ## Atributos
       Lista de atributos.

       ## Relacionamentos
       Lista de relacionamentos.

3. **Arquivo de Teste**:

   .. code-block:: text

       # Nome do Teste
       Versão: 1.0.0
       Autor: Nome do Autor
       Data: YYYY-MM-DD
       Domínio: Domínio
       Tags: tag1, tag2

       ## Cenários de Teste
       Lista de cenários.

Integração com IA
--------------

O prompt gerado segue um formato específico:

.. code-block:: text

    # Geração de Código a partir de Especificação LNEGC

    ## Linguagem Alvo: [linguagem]

    ## Configuração do Projeto
    [detalhes da configuração]

    ## Entidades
    [definições de entidades]

    ## Interfaces
    [definições de interfaces]

    ## Componentes
    [definições de componentes]

    ## Testes
    [definições de testes]

    ## Instruções
    [instruções para geração] 