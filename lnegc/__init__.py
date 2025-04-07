"""
LNEGC - Linguagem Natural Estruturada para Geração de Código.

Este pacote fornece ferramentas para processar arquivos LNEGC e gerar código através de sistemas de IA.
A LNEGC é uma linguagem de marcação que permite descrever componentes, entidades, interfaces e testes
de forma estruturada, usando linguagem natural em português.

Principais módulos:
- parser: Extrai informações dos arquivos .lnegc
- processor: Gera prompts para sistemas de IA
- cli: Interface de linha de comando

Exemplo de uso:
    from lnegc.processor import LNEGCProcessor

    # Cria um processador para o diretório do projeto
    processor = LNEGCProcessor("./meu-projeto")

    # Processa os arquivos e gera os prompts
    prompts = processor.process()

    # Itera sobre os prompts gerados
    for tipo, lista_prompts in prompts.items():
        print(f"Prompts para {tipo}:")
        for prompt in lista_prompts:
            print(prompt)
            print("-" * 80)
"""

from .src.core.parser import LNEGCParser
from .src.core.processor import LNEGCProcessor

__version__ = "0.1.0"
__author__ = "Equipe LNEGC"
__email__ = "contato@lnegc.com.br"

__all__ = ["LNEGCParser", "LNEGCProcessor"] 