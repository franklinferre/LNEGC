#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testes para o módulo Parser do LNEGC.
"""

import tempfile
from pathlib import Path
from unittest import TestCase, main

from lnegc.parser import LNEGCParser


class TestParser(TestCase):
    """Testes para o Parser do LNEGC."""

    def setUp(self):
        """Prepara ambiente para os testes."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = Path(self.temp_dir) / "test.lnegc"

    def tearDown(self):
        """Limpa ambiente após os testes."""
        import shutil

        shutil.rmtree(self.temp_dir)

    def test_parse_basic_file(self):
        """Testa parsing de arquivo básico."""
        content = """# Componente de Teste
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2023-10-15
Domínio: Testes
Tags: teste, componente

## Descrição
Este é um componente de teste.

## Interface
- Entrada: String
- Saída: String

## Algoritmo
1. Receber entrada
2. Processar
3. Retornar resultado
"""
        self.test_file.write_text(content)

        parser = LNEGCParser(str(self.test_file))
        result = parser.parse()

        self.assertEqual(result["metadata"]["nome"], "Componente de Teste")
        self.assertEqual(result["metadata"]["versao"], "1.0.0")
        self.assertEqual(result["metadata"]["autor"], "Equipe LNEGC")
        self.assertEqual(result["metadata"]["data"], "2023-10-15")
        self.assertEqual(result["metadata"]["dominio"], "Testes")
        self.assertEqual(result["metadata"]["tags"], ["teste", "componente"])

        self.assertIn("Descrição", result["sections"])
        self.assertIn("Interface", result["sections"])
        self.assertIn("Algoritmo", result["sections"])

    def test_parse_missing_metadata(self):
        """Testa parsing com metadados faltando."""
        content = """# Componente de Teste

## Descrição
Este é um componente de teste.
"""
        self.test_file.write_text(content)

        parser = LNEGCParser(str(self.test_file))
        result = parser.parse()

        self.assertEqual(result["metadata"], {})
        self.assertIn("Descrição", result["sections"])

    def test_parse_empty_sections(self):
        """Testa parsing com seções vazias."""
        content = """# Componente de Teste
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2023-10-15
Domínio: Testes
Tags: teste

## Descrição

## Interface

## Algoritmo
"""
        self.test_file.write_text(content)

        parser = LNEGCParser(str(self.test_file))
        result = parser.parse()

        self.assertEqual(result["sections"]["Descrição"], "")
        self.assertEqual(result["sections"]["Interface"], "")
        self.assertEqual(result["sections"]["Algoritmo"], "")

    def test_parse_complex_content(self):
        """Testa parsing com conteúdo complexo."""
        content = """# Validador de CPF
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2023-10-15
Domínio: Validação
Tags: cpf, validação, documento

## Interface
- Entrada: String (CPF)
- Saída: Boolean
- Exceções: FormatoInvalidoException

## Algoritmo
1. Limpar entrada
   - Remover pontuação
   - Remover espaços
2. Validar formato
   - Verificar se tem 11 dígitos
   - Verificar se são todos números
3. Verificar dígitos repetidos
   - CPF não pode ter todos os dígitos iguais
4. Calcular primeiro dígito verificador
   - Multiplicar primeiros 9 dígitos por peso (10 a 2)
   - Somar resultados
   - Calcular resto da divisão por 11
   - Se resto < 2, dígito = 0; senão, dígito = 11 - resto
5. Calcular segundo dígito verificador
   - Multiplicar primeiros 10 dígitos por peso (11 a 2)
   - Somar resultados
   - Calcular resto da divisão por 11
   - Se resto < 2, dígito = 0; senão, dígito = 11 - resto
6. Comparar dígitos calculados com originais

## Exemplos
1. CPF Válido: 529.982.247-25
2. CPF Inválido: 111.111.111-11
3. Formato Inválido: ABC.DEF.GHI-JK
"""
        self.test_file.write_text(content)

        parser = LNEGCParser(str(self.test_file))
        result = parser.parse()

        self.assertEqual(result["metadata"]["nome"], "Validador de CPF")
        self.assertEqual(len(result["metadata"]["tags"]), 3)
        self.assertIn("Interface", result["sections"])
        self.assertIn("Algoritmo", result["sections"])
        self.assertIn("Exemplos", result["sections"])

    def test_parse_file_not_found(self):
        """Testa parsing com arquivo inexistente."""
        parser = LNEGCParser("arquivo_inexistente.lnegc")
        with self.assertRaises(FileNotFoundError):
            parser.parse()

    def test_parse_invalid_encoding(self):
        """Testa parsing com encoding inválido."""
        # Criar arquivo com bytes inválidos
        with open(self.test_file, "wb") as f:
            f.write(b"\xFF\xFE Invalid UTF-8 bytes")

        parser = LNEGCParser(str(self.test_file))
        with self.assertRaises(UnicodeDecodeError):
            parser.parse()

    def test_parse_metadata_with_explicit_metadata(self):
        """Testa extração de metadados com formato explícito."""
        content = """# Componente Teste
Versão: 1.0.0
Autor: Teste
Data: 2023-01-01
Tags: teste, metadata

## Descrição
Teste de metadados explícitos.
"""
        file_path = Path(self.temp_dir) / "test_explicit.lnegc"
        file_path.write_text(content)

        parser = LNEGCParser(file_path)
        result = parser.parse()

        self.assertEqual(result["metadata"]["nome"], "Componente Teste")
        self.assertEqual(result["metadata"]["versao"], "1.0.0")
        self.assertEqual(result["metadata"]["autor"], "Teste")
        self.assertEqual(result["metadata"]["data"], "2023-01-01")
        self.assertEqual(result["metadata"]["tags"], ["teste", "metadata"])

    def test_parse_sections_with_empty_content(self):
        """Testa extração de seções com conteúdo vazio."""
        content = """# Componente Teste
Versão: 1.0.0

[Seção 1]

[Seção 2]
Conteúdo da seção 2

[Seção 3]
"""
        file_path = Path(self.temp_dir) / "test_sections.lnegc"
        file_path.write_text(content)

        parser = LNEGCParser(file_path)
        result = parser.parse()

        self.assertEqual(result["sections"]["Seção 1"], "")
        self.assertEqual(result["sections"]["Seção 2"], "Conteúdo da seção 2")
        self.assertEqual(result["sections"]["Seção 3"], "")

    def test_parse_empty_file(self):
        """Testa processamento de arquivo vazio."""
        # Cria arquivo vazio
        file_path = Path(self.temp_dir) / "empty.lnegc"
        file_path.write_text("")

        parser = LNEGCParser(file_path)
        result = parser.parse()

        self.assertEqual(result["metadata"], {})
        self.assertEqual(result["sections"], {})


if __name__ == "__main__":
    main() 