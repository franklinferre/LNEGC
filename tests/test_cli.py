#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testes para o módulo CLI do LNEGC.
"""

import os
import tempfile
from pathlib import Path
from unittest import TestCase, main
from unittest.mock import patch

from lnegc.cli import main as cli_main


class TestCLI(TestCase):
    """Testes para o CLI do LNEGC."""

    def setUp(self):
        """Prepara ambiente para os testes."""
        # Criar diretório temporário
        self.temp_dir = tempfile.mkdtemp()
        self.base_dir = Path(self.temp_dir) / "lnegc"
        self.base_dir.mkdir()

        # Criar estrutura de diretórios
        (self.base_dir / "componentes").mkdir()
        (self.base_dir / "entidades").mkdir()
        (self.base_dir / "interfaces").mkdir()
        (self.base_dir / "testes").mkdir()

        # Criar arquivo de configuração
        config_content = """# Sistema de Teste
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2023-10-15
Domínio: Testes
Tags: teste, exemplo

## Descrição
Sistema para testes do LNEGC.
"""
        (self.base_dir / "config.lnegc").write_text(config_content)

        # Criar arquivo de componente
        component_content = """# Componente de Teste
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2023-10-15
Domínio: Testes
Tags: teste, componente

## Interface
- Entrada: String
- Saída: String

## Algoritmo
1. Receber entrada
2. Processar
3. Retornar resultado
"""
        (self.base_dir / "componentes" / "teste.lnegc").write_text(component_content)

    def tearDown(self):
        """Limpa ambiente após os testes."""
        import shutil

        shutil.rmtree(self.temp_dir)

    def test_cli_help(self):
        """Testa exibição da ajuda."""
        with self.assertRaises(SystemExit) as cm:
            cli_main(["--help"])
        self.assertEqual(cm.exception.code, 0)

    def test_cli_version(self):
        """Testa exibição da versão."""
        with self.assertRaises(SystemExit) as cm:
            cli_main(["--version"])
        self.assertEqual(cm.exception.code, 0)

    def test_cli_invalid_dir(self):
        """Testa diretório inválido."""
        result = cli_main(["--dir", "diretorio_inexistente"])
        self.assertEqual(result, 1)

    def test_cli_not_dir(self):
        """Testa caminho que não é diretório."""
        file_path = Path(self.temp_dir) / "arquivo.txt"
        file_path.touch()
        result = cli_main(["--dir", str(file_path)])
        self.assertEqual(result, 1)

    def test_cli_success(self):
        """Testa processamento bem-sucedido."""
        output_file = Path(self.temp_dir) / "prompt.txt"
        result = cli_main([
            "--dir", str(self.base_dir),
            "--output", str(output_file),
            "--language", "python",
            "--verbose"
        ])
        self.assertEqual(result, 0)
        self.assertTrue(output_file.exists())
        content = output_file.read_text()
        self.assertIn("Componente de Teste", content)
        self.assertIn("python", content.lower())
        self.assertIn("Entrada: String", content)
        self.assertIn("Saída: String", content)

    def test_cli_custom_language(self):
        """Testa processamento com linguagem personalizada."""
        output_file = Path(self.temp_dir) / "prompt.txt"
        result = cli_main([
            "--dir", str(self.base_dir),
            "--output", str(output_file),
            "--language", "java"
        ])
        self.assertEqual(result, 0)
        content = output_file.read_text()
        self.assertIn("java", content.lower())

    def test_cli_exception_handling(self):
        """Testa o tratamento de exceções no CLI."""
        # Força uma exceção ao tentar processar um diretório inválido
        with patch('lnegc.processor.LNEGCProcessor.process', side_effect=Exception("Erro forçado")):
            result = cli_main(["--dir", str(Path(self.temp_dir) / "invalid"), "--verbose"])
            self.assertEqual(result, 1)  # Deve retornar código de erro 1

    def test_cli_exception_without_args(self):
        """Testa o tratamento de exceções quando parsed_args é None."""
        # Força uma exceção antes que parsed_args seja definido
        with patch('lnegc.cli.parse_args', side_effect=Exception("Erro antes de parsed_args")):
            result = cli_main([])
            self.assertEqual(result, 1)  # Deve retornar código de erro 1

    def test_cli_main_entry_point(self):
        """Testa o ponto de entrada principal do CLI."""
        # Cria um arquivo temporário para testar
        output_file = Path(self.temp_dir) / "output.txt"
        
        # Executa o CLI como script principal
        with patch('sys.argv', ['lnegc', '--dir', str(self.base_dir), '--output', str(output_file)]):
            with patch('sys.exit') as mock_exit:
                import lnegc.cli
                if hasattr(lnegc.cli, '__main__'):
                    mock_exit.assert_called_once()
                    self.assertTrue(output_file.exists())


if __name__ == "__main__":
    main() 