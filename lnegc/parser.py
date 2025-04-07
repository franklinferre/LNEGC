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

    def __init__(self, file_path: Union[str, Path]):
        """
        Inicializa o parser LNEGC.

        Args:
            file_path: Caminho para o arquivo .lnegc a ser processado
        """
        self.file_path = Path(file_path)
        self._content: Optional[str] = None
        self._lines: Optional[List[str]] = None

    def _read_file(self) -> None:
        """
        Lê o conteúdo do arquivo.

        Raises:
            FileNotFoundError: Se o arquivo não existir
            UnicodeDecodeError: Se o arquivo não estiver em UTF-8
        """
        if not self.file_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {self.file_path}")

        self._content = self.file_path.read_text(encoding="utf-8")
        self._lines = self._content.splitlines()

    def _parse_metadata(self) -> Dict[str, Union[str, List[str]]]:
        """
        Extrai os metadados do arquivo LNEGC.

        Returns:
            Dict contendo os metadados do arquivo
        """
        metadata = {}
        if not self._lines:
            return metadata

        # Verifica se há metadados explícitos (linhas com formato chave: valor)
        has_metadata = False
        for line in self._lines[1:]:
            if line.startswith("[") or line.startswith("## "):
                break
            if ":" in line and not line.startswith("#"):
                has_metadata = True
                break

        # Extrai o nome do componente/entidade/interface/teste da primeira linha
        # apenas se houver metadados explícitos
        if has_metadata and self._lines[0].startswith("# "):
            metadata["nome"] = self._lines[0][2:].strip()

        # Processa os metadados linha por linha até encontrar uma seção
        for line in self._lines[1:]:
            if line.startswith("[") or line.startswith("## "):
                break
            
            # Procura por pares chave: valor
            match = re.match(r"^([^:]+):\s*(.+)$", line)
            if match:
                key, value = match.groups()
                key = key.strip().lower()
                value = value.strip()

                # Converte chaves para o formato esperado
                key_map = {
                    "versão": "versao",
                    "domínio": "dominio",
                    "autor": "autor",
                    "data": "data",
                    "tags": "tags",
                    "linguagem_padrão": "linguagem",
                }
                key = key_map.get(key, key)

                # Processa tags como lista
                if key == "tags":
                    metadata[key] = [tag.strip() for tag in value.split(",")]
                else:
                    metadata[key] = value

        return metadata

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

        if not self._lines:
            return sections

        for line in self._lines:
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

    def parse(self) -> Dict[str, Dict]:
        """
        Processa o arquivo LNEGC e retorna sua estrutura.

        Returns:
            Dict contendo a estrutura do arquivo LNEGC com metadados e seções

        Raises:
            FileNotFoundError: Se o arquivo não existir
            UnicodeDecodeError: Se o arquivo não estiver em UTF-8
        """
        self._read_file()

        return {
            "metadata": self._parse_metadata(),
            "sections": self._parse_sections()
        } 