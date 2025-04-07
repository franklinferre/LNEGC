#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Interface de linha de comando para o processador LNEGC.
"""

import argparse
import sys
from pathlib import Path
from typing import List, Optional

from .processor import LNEGCProcessor


def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """Processa argumentos da linha de comando.

    Args:
        args: Lista de argumentos da linha de comando.
            Se None, usa sys.argv[1:].

    Returns:
        Namespace com os argumentos processados.
    """
    parser = argparse.ArgumentParser(
        description="Processador LNEGC - Linguagem Natural Estruturada para Geração de Código",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--dir",
        type=str,
        default="lnegc",
        help="Diretório base com arquivos LNEGC (padrão: 'lnegc')",
    )

    parser.add_argument(
        "--output",
        type=str,
        default="prompt.txt",
        help="Arquivo de saída para o prompt (padrão: 'prompt.txt')",
    )

    parser.add_argument(
        "--language",
        type=str,
        default=None,
        help="Linguagem alvo para geração de código (se não especificado, usa a linguagem do arquivo de configuração)",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Exibe informações detalhadas durante o processamento",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__import__('lnegc').__version__}",
    )

    return parser.parse_args(args)


def main(args: Optional[List[str]] = None) -> int:
    """Função principal do CLI.

    Args:
        args: Lista de argumentos da linha de comando.
            Se None, usa sys.argv[1:].

    Returns:
        0 em caso de sucesso, outro valor em caso de erro.
    """
    try:
        # Processar argumentos
        parsed_args = parse_args(args)

        # Verificar diretório
        base_dir = Path(parsed_args.dir)
        if not base_dir.exists():
            print(f"Erro: Diretório '{base_dir}' não encontrado.", file=sys.stderr)
            return 1

        if not base_dir.is_dir():
            print(f"Erro: '{base_dir}' não é um diretório.", file=sys.stderr)
            return 1

        # Criar processador com a linguagem especificada
        processor = LNEGCProcessor(str(base_dir), parsed_args.language)

        # Processar arquivos
        if parsed_args.verbose:
            print("Processando arquivos LNEGC...")

        result = processor.process()
        prompts = processor.process_all()

        # Salvar prompts
        output_path = Path(parsed_args.output)
        output_path.write_text("\n\n".join(prompts), encoding="utf-8")

        if parsed_args.verbose:
            print(f"\nProcessamento concluído. Prompts salvos em {output_path}")
            print(f"Componentes processados: {len(result['componentes'])}")
            print(f"Entidades processadas: {len(result['entidades'])}")
            print(f"Interfaces processadas: {len(result['interfaces'])}")
            print(f"Testes processados: {len(result['testes'])}")

        return 0

    except Exception as e:
        print(f"Erro: {e}", file=sys.stderr)
        if parsed_args and parsed_args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main()) 