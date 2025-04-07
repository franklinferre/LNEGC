#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Processador para arquivos LNEGC.

Este módulo implementa o processador para a Linguagem Natural Estruturada para Geração de Código (LNEGC).
O processador é responsável por transformar a estrutura extraída pelo parser em prompts que podem ser
enviados para sistemas de IA para geração de código.
"""

import os
from pathlib import Path
from typing import Dict, List, Optional, Union

from .parser import LNEGCParser


class LNEGCProcessor:
    """Processador para arquivos LNEGC."""

    def __init__(self, directory: Union[str, Path], target_language: str = None):
        """
        Inicializa o processador LNEGC.

        Args:
            directory: Diretório contendo os arquivos .lnegc
            target_language: Linguagem alvo para geração de código.
                           Se None, usa a linguagem definida no arquivo de configuração.
        """
        self.directory = Path(directory)
        self._config: Optional[Dict] = None
        self._components: List[Dict] = []
        self._entities: List[Dict] = []
        self._interfaces: List[Dict] = []
        self._tests: List[Dict] = []
        self.target_language = target_language if target_language is not None else "python"

    def _load_config(self) -> None:
        """
        Carrega o arquivo de configuração do projeto.

        Raises:
            FileNotFoundError: Se o arquivo config.lnegc não existir
        """
        config_file = self.directory / "config.lnegc"
        if not config_file.exists():
            raise FileNotFoundError(f"Arquivo de configuração não encontrado: {config_file}")

        parser = LNEGCParser(config_file)
        self._config = parser.parse()
        
        # Define a linguagem alvo com base na configuração
        if self.target_language is None:
            # Procura a linguagem nas configurações
            config_sections = self._config.get('sections', {})
            if 'CONFIGURAÇÕES' in config_sections:
                for line in config_sections['CONFIGURAÇÕES'].split('\n'):
                    if line.startswith('Linguagem_Padrão:'):
                        self.target_language = line.split(':')[1].strip()
                        break
            
            # Se não encontrou, procura nos metadados
            if not self.target_language:
                self.target_language = self._config.get('metadata', {}).get('linguagem')
            
            # Se ainda não encontrou, usa o padrão
            if not self.target_language:
                self.target_language = 'python'

    def _load_files(self) -> None:
        """Carrega todos os arquivos .lnegc do projeto."""
        # Carrega componentes
        components_dir = self.directory / "componentes"
        if components_dir.exists():
            for file in components_dir.glob("*.lnegc"):
                parser = LNEGCParser(file)
                self._components.append(parser.parse())

        # Carrega entidades
        entities_dir = self.directory / "entidades"
        if entities_dir.exists():
            for file in entities_dir.glob("*.lnegc"):
                parser = LNEGCParser(file)
                self._entities.append(parser.parse())

        # Carrega interfaces
        interfaces_dir = self.directory / "interfaces"
        if interfaces_dir.exists():
            for file in interfaces_dir.glob("*.lnegc"):
                parser = LNEGCParser(file)
                self._interfaces.append(parser.parse())

        # Carrega testes
        tests_dir = self.directory / "testes"
        if tests_dir.exists():
            for file in tests_dir.glob("*.lnegc"):
                parser = LNEGCParser(file)
                self._tests.append(parser.parse())

    def _generate_component_prompt(self, component: Dict) -> str:
        """
        Gera o prompt para um componente.

        Args:
            component: Dicionário com os dados do componente

        Returns:
            String contendo o prompt para o componente
        """
        prompt = f"""Por favor, gere um componente em {self.target_language} com as seguintes especificações:

Nome: {component['metadata'].get('nome', 'Componente')}
Versão: {component['metadata'].get('versao', '1.0.0')}
Autor: {component['metadata'].get('autor', 'Equipe LNEGC')}
Tipo: {component['metadata'].get('tipo', 'Utilitário')}

Descrição:
{component['sections'].get('Descrição', component['sections'].get('DESCRIÇÃO', 'Sem descrição disponível.'))}

Algoritmo:
{component['sections'].get('Algoritmo', component['sections'].get('ALGORITMO', 'Sem algoritmo definido.'))}

Regras:
{component['sections'].get('Regras', component['sections'].get('REGRAS', 'Sem regras definidas.'))}

Interface:
{component['sections'].get('Interface', component['sections'].get('INTERFACE', 'Sem interface definida.'))}

Observações:
- Toda a documentação deve estar em português do Brasil
- Comentários devem estar em português do Brasil
- Nomes de variáveis e funções devem seguir o padrão camelCase em português
"""
        if "Exemplos" in component["sections"] or "EXEMPLOS" in component["sections"]:
            prompt += f"\nExemplos:\n{component['sections'].get('Exemplos', component['sections'].get('EXEMPLOS', ''))}"

        if "Implementação" in component["sections"] or "IMPLEMENTAÇÃO" in component["sections"]:
            prompt += f"\nImplementação de Referência:\n{component['sections'].get('Implementação', component['sections'].get('IMPLEMENTAÇÃO', ''))}"

        return prompt

    def _generate_entity_prompt(self, entity: Dict) -> str:
        """
        Gera o prompt para uma entidade.

        Args:
            entity: Dicionário com os dados da entidade

        Returns:
            String contendo o prompt para a entidade
        """
        prompt = f"""Por favor, gere uma entidade em {self.target_language} com as seguintes especificações:

Nome: {entity['metadata'].get('nome', 'Entidade')}
Versão: {entity['metadata'].get('versao', '1.0.0')}
Autor: {entity['metadata'].get('autor', 'Equipe LNEGC')}
Tipo: {entity['metadata'].get('tipo', 'Domínio')}

Descrição:
{entity['sections'].get('Descrição', entity['sections'].get('DESCRIÇÃO', 'Sem descrição disponível.'))}

Atributos:
{entity['sections'].get('Atributos', entity['sections'].get('ATRIBUTOS', 'Sem atributos definidos.'))}

Regras:
{entity['sections'].get('Regras', entity['sections'].get('REGRAS', 'Sem regras definidas.'))}

Relacionamentos:
{entity['sections'].get('Relacionamentos', entity['sections'].get('RELACIONAMENTOS', 'Sem relacionamentos definidos.'))}

"""
        if "Implementação" in entity["sections"] or "IMPLEMENTAÇÃO" in entity["sections"]:
            prompt += f"\nImplementação de Referência:\n{entity['sections'].get('Implementação', entity['sections'].get('IMPLEMENTAÇÃO', ''))}"

        return prompt

    def _generate_interface_prompt(self, interface: Dict) -> str:
        """
        Gera o prompt para uma interface.

        Args:
            interface: Dicionário com os dados da interface

        Returns:
            String contendo o prompt para a interface
        """
        prompt = f"""Por favor, gere uma interface em {self.target_language} com as seguintes especificações:

Nome: {interface['metadata'].get('nome', 'Interface')}
Versão: {interface['metadata'].get('versao', '1.0.0')}
Autor: {interface['metadata'].get('autor', 'Equipe LNEGC')}
Tipo: {interface['metadata'].get('tipo', 'Interface')}

Descrição:
{interface['sections'].get('Descrição', interface['sections'].get('DESCRIÇÃO', 'Sem descrição disponível.'))}

Métodos:
{interface['sections'].get('Métodos', interface['sections'].get('MÉTODOS', 'Sem métodos definidos.'))}

Propriedades:
{interface['sections'].get('Propriedades', interface['sections'].get('PROPRIEDADES', 'Sem propriedades definidas.'))}

Regras:
{interface['sections'].get('Regras', interface['sections'].get('REGRAS', 'Sem regras definidas.'))}

"""
        if "Implementação" in interface["sections"] or "IMPLEMENTAÇÃO" in interface["sections"]:
            prompt += f"\nImplementação de Referência:\n{interface['sections'].get('Implementação', interface['sections'].get('IMPLEMENTAÇÃO', ''))}"

        return prompt

    def _generate_test_prompt(self, test: Dict) -> str:
        """
        Gera o prompt para um teste.

        Args:
            test: Dicionário com os dados do teste

        Returns:
            String contendo o prompt para o teste
        """
        prompt = f"""Por favor, gere testes em {self.target_language} com as seguintes especificações:

Nome: {test['metadata'].get('nome', 'Teste')}
Versão: {test['metadata'].get('versao', '1.0.0')}
Autor: {test['metadata'].get('autor', 'Equipe LNEGC')}
Tipo: {test['metadata'].get('tipo', 'Teste Unitário')}

Descrição:
{test['sections'].get('Descrição', test['sections'].get('DESCRIÇÃO', 'Sem descrição disponível.'))}

Cenários:
{test['sections'].get('Cenários', test['sections'].get('CENÁRIOS', 'Sem cenários definidos.'))}

Mocks:
{test['sections'].get('Mocks', test['sections'].get('MOCKS', 'Sem mocks definidos.'))}

Fixtures:
{test['sections'].get('Fixtures', test['sections'].get('FIXTURES', 'Sem fixtures definidas.'))}

"""
        if "Implementação" in test["sections"] or "IMPLEMENTAÇÃO" in test["sections"]:
            prompt += f"\nImplementação de Referência:\n{test['sections'].get('Implementação', test['sections'].get('IMPLEMENTAÇÃO', ''))}"

        return prompt

    def process(self) -> Dict[str, List[str]]:
        """
        Processa todos os arquivos LNEGC e gera os prompts.

        Returns:
            Dicionário com os prompts gerados por tipo
        """
        self._load_config()
        self._load_files()

        # Remove duplicatas usando um set para cada tipo
        unique_components = {str(c): c for c in self._components}
        unique_entities = {str(e): e for e in self._entities}
        unique_interfaces = {str(i): i for i in self._interfaces}
        unique_tests = {str(t): t for t in self._tests}

        prompts = {
            "componentes": [self._generate_component_prompt(c) for c in unique_components.values()],
            "entidades": [self._generate_entity_prompt(e) for e in unique_entities.values()],
            "interfaces": [self._generate_interface_prompt(i) for i in unique_interfaces.values()],
            "testes": [self._generate_test_prompt(t) for t in unique_tests.values()]
        }

        return prompts

    def process_all(self) -> List[str]:
        """
        Processa todos os arquivos LNEGC e retorna uma lista com todos os prompts.

        Returns:
            Lista com todos os prompts gerados
        """
        result = self.process()
        all_prompts = []
        for prompts in result.values():
            all_prompts.extend(prompts)
        return all_prompts 