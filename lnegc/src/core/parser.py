#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parser para arquivos LNEGC.

Este módulo implementa o parser para a Linguagem Natural Estruturada para Geração de Código (LNEGC).
O parser é responsável por ler arquivos .lnegc e extrair suas informações em um formato estruturado
que pode ser usado para gerar código através de sistemas de IA.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Union


class LNEGCParser:
    """Parser para arquivos LNEGC."""

    def __init__(self, file_path: Path):
        """
        Inicializa o parser LNEGC.

        Args:
            file_path: Caminho para o arquivo .lnegc a ser processado
        """
        self.file_path = file_path
        self.content = self._read_file()

    def _read_file(self) -> str:
        """Lê o conteúdo do arquivo."""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def parse(self) -> dict:
        """Parse o arquivo .lnegc e retorna um dicionário com as informações."""
        sections = self._parse_sections()
        metadata = self._parse_metadata(sections.get('Metadados', ''))
        
        return {
            'metadata': metadata,
            'attributes': self._parse_list_items(sections.get('Atributos', '')),
            'validations': self._parse_list_items(sections.get('Validações', '')),
            'relationships': self._parse_list_items(sections.get('Relacionamentos', '')),
            'methods': self._parse_list_items(sections.get('Métodos', '')),
            'indexes': self._parse_list_items(sections.get('Índices', '')),
            'permissions': self._parse_list_items(sections.get('Permissões', '')),
            'auditoria': self._parse_list_items(sections.get('Auditoria', ''))
        }

    def _parse_sections(self) -> dict:
        """Parse as seções do arquivo."""
        sections = {}
        current_section = None
        current_content = []

        for line in self.content.split('\n'):
            if line.startswith('## '):
                if current_section:
                    sections[current_section] = '\n'.join(current_content)
                current_section = line[3:].strip()
                current_content = []
            elif current_section:
                current_content.append(line)

        if current_section:
            sections[current_section] = '\n'.join(current_content)

        return sections

    def _parse_metadata(self, content: str = None) -> dict:
        """
        Parse os metadados da entidade.
        
        Args:
            content: Conteúdo da seção de metadados. Se None, usa o conteúdo do arquivo.
        """
        metadata = {}
        text = content if content is not None else self.content
        
        for line in text.split('\n'):
            if line.startswith('- **'):
                key, value = line[4:].split('**:', 1)
                metadata[key.strip()] = value.strip()
        return metadata

    def _parse_list_items(self, content: str) -> List[str]:
        """Parse itens de lista do conteúdo."""
        items = []
        for line in content.split('\n'):
            if line.startswith('- '):
                items.append(line[2:].strip())
        return items

    def _parse_sections(self) -> Dict[str, str]:
        """
        Extrai as seções do arquivo LNEGC.

        Returns:
            Dict contendo as seções do arquivo
        """
        sections = {}
        current_section = None
        current_content = []
        in_section = False

        if not self.content:
            return sections

        for line in self.content.split('\n'):
            if line.startswith("["):
                # Se já estávamos em uma seção, salvamos seu conteúdo
                if current_section:
                    sections[current_section] = "\n".join(current_content).strip()
                    current_content = []
                
                # Inicia nova seção
                current_section = line[1:].strip().rstrip("]")
                in_section = True
            elif line.startswith("## "):
                # Se já estávamos em uma seção, salvamos seu conteúdo
                if current_section:
                    sections[current_section] = "\n".join(current_content).strip()
                    current_content = []
                
                # Inicia nova seção
                current_section = line[3:].strip()
                in_section = True
            elif in_section and not line.startswith("# "):
                # Adiciona linha ao conteúdo da seção atual
                current_content.append(line)

        # Salva a última seção
        if current_section:
            sections[current_section] = "\n".join(current_content).strip()

        return sections 