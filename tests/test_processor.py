#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testes para o módulo Processor do LNEGC.
"""

import os
import tempfile
from pathlib import Path
from unittest import TestCase, main

from lnegc.processor import LNEGCProcessor


class TestProcessor(TestCase):
    """Testes para o Processor do LNEGC."""

    def setUp(self):
        """Prepara ambiente para os testes."""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.test_dir = self.temp_dir / "lnegc"
        
        # Cria estrutura de diretórios
        os.makedirs(self.test_dir / "componentes")
        os.makedirs(self.test_dir / "entidades")
        os.makedirs(self.test_dir / "interfaces")
        os.makedirs(self.test_dir / "testes")

        # Cria arquivo de configuração
        config_content = """# Projeto LNEGC
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2023-10-15
Domínio: Testes
Tags: teste, configuração

## Descrição
Projeto de teste para o processador LNEGC.

## Configurações
- Nome: Projeto Teste
- Versão: 1.0.0
- Linguagem: Python
- Framework: FastAPI
- Banco de Dados: PostgreSQL

## Dependências
- OpenAI API
- Python 3.8+
- Markdown
"""
        (self.test_dir / "config.lnegc").write_text(config_content)

        # Cria arquivo de componente
        component_content = """# Validador de CPF
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
2. Validar formato
3. Calcular dígitos verificadores
4. Comparar dígitos

## Exemplos
1. CPF Válido: 529.982.247-25
2. CPF Inválido: 111.111.111-11
"""
        (self.test_dir / "componentes" / "validador_cpf.lnegc").write_text(component_content)

        # Cria arquivo de entidade
        entity_content = """# Cliente
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2023-10-15
Domínio: Negócio
Tags: cliente, pessoa

## Descrição
Entidade que representa um cliente no sistema.

## Atributos
- id: UUID (obrigatório)
- nome: String (obrigatório)
- cpf: String (obrigatório)
- email: String (obrigatório)
- telefone: String (opcional)

## Relacionamentos
- Pedidos: OneToMany
- Categorias: ManyToMany

## Validações
- CPF deve ser válido
- Email deve ser único
- Nome deve ter entre 3 e 100 caracteres
"""
        (self.test_dir / "entidades" / "cliente.lnegc").write_text(entity_content)

        # Cria arquivo de interface
        interface_content = """# Repositório
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2023-10-15
Domínio: Persistência
Tags: repositório, crud

## Descrição
Interface base para repositórios de dados.

## Métodos
- salvar(entidade: T): T
- buscarPorId(id: UUID): Optional[T]
- listarTodos(): List[T]
- atualizar(entidade: T): T
- excluir(id: UUID): void

## Propriedades
- tipo: Type[T]
- conexao: Connection
"""
        (self.test_dir / "interfaces" / "repositorio.lnegc").write_text(interface_content)

        # Cria arquivo de teste
        test_content = """# Teste Validador CPF
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2023-10-15
Domínio: Testes
Tags: teste, cpf, validação

## Descrição
Testes unitários para o validador de CPF.

## Cenários
1. CPF válido deve retornar true
2. CPF inválido deve retornar false
3. CPF com formato inválido deve lançar exceção
4. CPF com dígitos repetidos deve retornar false

## Mocks
Não são necessários mocks para este teste.
"""
        (self.test_dir / "testes" / "teste_validador_cpf.lnegc").write_text(test_content)

    def tearDown(self):
        """Limpa ambiente após os testes."""
        import shutil
        shutil.rmtree(self.temp_dir)

    def test_processor_init(self):
        """Testa inicialização do processador."""
        processor = LNEGCProcessor(self.test_dir)
        self.assertEqual(processor.directory, self.test_dir)
        self.assertEqual(processor.target_language, "python")

        processor = LNEGCProcessor(self.test_dir, "typescript")
        self.assertEqual(processor.target_language, "typescript")

    def test_processor_load_config(self):
        """Testa carregamento do arquivo de configuração."""
        processor = LNEGCProcessor(self.test_dir)
        processor._load_config()

        self.assertIsNotNone(processor._config)
        self.assertEqual(processor._config["metadata"]["nome"], "Projeto LNEGC")
        self.assertEqual(processor._config["metadata"]["versao"], "1.0.0")
        self.assertEqual(len(processor._config["metadata"]["tags"]), 2)

    def test_processor_load_files(self):
        """Testa carregamento dos arquivos do projeto."""
        processor = LNEGCProcessor(self.test_dir)
        processor._load_files()

        self.assertEqual(len(processor._components), 1)
        self.assertEqual(len(processor._entities), 1)
        self.assertEqual(len(processor._interfaces), 1)
        self.assertEqual(len(processor._tests), 1)

    def test_processor_generate_component_prompt(self):
        """Testa geração de prompt para componente."""
        processor = LNEGCProcessor(self.test_dir)
        processor._load_files()

        prompt = processor._generate_component_prompt(processor._components[0])
        self.assertIn("Validador de CPF", prompt)
        self.assertIn("Entrada: String (CPF)", prompt)
        self.assertIn("CPF Válido: 529.982.247-25", prompt)

    def test_processor_generate_entity_prompt(self):
        """Testa geração de prompt para entidade."""
        processor = LNEGCProcessor(self.test_dir)
        processor._load_files()

        prompt = processor._generate_entity_prompt(processor._entities[0])
        self.assertIn("Cliente", prompt)
        self.assertIn("id: UUID (obrigatório)", prompt)
        self.assertIn("Pedidos: OneToMany", prompt)

    def test_processor_generate_interface_prompt(self):
        """Testa geração de prompt para interface."""
        processor = LNEGCProcessor(self.test_dir)
        processor._load_files()

        prompt = processor._generate_interface_prompt(processor._interfaces[0])
        self.assertIn("Repositório", prompt)
        self.assertIn("salvar(entidade: T): T", prompt)
        self.assertIn("tipo: Type[T]", prompt)

    def test_processor_generate_test_prompt(self):
        """Testa geração de prompt para teste."""
        processor = LNEGCProcessor(self.test_dir)
        processor._load_files()

        prompt = processor._generate_test_prompt(processor._tests[0])
        self.assertIn("Teste Validador CPF", prompt)
        self.assertIn("CPF válido deve retornar true", prompt)
        self.assertIn("Não são necessários mocks", prompt)

    def test_processor_process(self):
        """Testa processamento completo do projeto."""
        processor = LNEGCProcessor(self.test_dir)
        prompts = processor.process()

        self.assertIn("componentes", prompts)
        self.assertIn("entidades", prompts)
        self.assertIn("interfaces", prompts)
        self.assertIn("testes", prompts)

        self.assertEqual(len(prompts["componentes"]), 1)
        self.assertEqual(len(prompts["entidades"]), 1)
        self.assertEqual(len(prompts["interfaces"]), 1)
        self.assertEqual(len(prompts["testes"]), 1)

    def test_processor_invalid_directory(self):
        """Testa processamento com diretório inválido."""
        processor = LNEGCProcessor(self.temp_dir / "invalid")
        with self.assertRaises(FileNotFoundError):
            processor.process()

    def test_processor_missing_config(self):
        """Testa processamento sem arquivo de configuração."""
        os.remove(self.test_dir / "config.lnegc")
        processor = LNEGCProcessor(self.test_dir)
        with self.assertRaises(FileNotFoundError):
            processor.process()


if __name__ == "__main__":
    main() 