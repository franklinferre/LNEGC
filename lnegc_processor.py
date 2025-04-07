#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Processador LNEGC - Linguagem Natural Estruturada para Geração de Código
Este script processa arquivos .lnegc e prepara para geração de código por IA.
"""

import os
import re
import json
import argparse
from typing import Dict, List, Any, Optional

class LNEGCParser:
    """Parser para arquivos LNEGC."""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.content = self._read_file()
        self.metadata = {}
        self.sections = {}
    
    def _read_file(self) -> str:
        """Lê o conteúdo do arquivo."""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def parse(self) -> Dict[str, Any]:
        """Analisa o arquivo LNEGC e extrai metadados e seções."""
        # Extrair cabeçalho e metadados
        header_match = re.match(r'#\s*(.*?)\nVersão:\s*(.*?)\nAutor:\s*(.*?)\nData:\s*(.*?)\nDomínio:\s*(.*?)\nTags:\s*(.*?)\n', 
                               self.content, re.DOTALL)
        if header_match:
            self.metadata = {
                'nome': header_match.group(1).strip(),
                'versao': header_match.group(2).strip(),
                'autor': header_match.group(3).strip(),
                'data': header_match.group(4).strip(),
                'dominio': header_match.group(5).strip(),
                'tags': [tag.strip() for tag in header_match.group(6).split(',')]
            }
        
        # Extrair seções
        sections = re.findall(r'##\s*(.*?)\n(.*?)(?=##|\Z)', self.content, re.DOTALL)
        for section_name, section_content in sections:
            section_name = section_name.strip()
            self.sections[section_name] = section_content.strip()
        
        return {
            'metadata': self.metadata,
            'sections': self.sections,
            'file_path': self.file_path
        }

class LNEGCProcessor:
    """Processador para arquivos LNEGC."""
    
    def __init__(self, base_dir: str):
        self.base_dir = base_dir
        self.components = []
        self.entities = []
        self.interfaces = []
        self.tests = []
        self.config = None
    
    def process_all(self) -> Dict[str, Any]:
        """Processa todos os arquivos LNEGC no diretório base."""
        # Processar arquivo de configuração
        config_path = os.path.join(self.base_dir, 'config.lnegc')
        if os.path.exists(config_path):
            parser = LNEGCParser(config_path)
            self.config = parser.parse()
        
        # Processar componentes
        components_dir = os.path.join(self.base_dir, 'componentes')
        if os.path.exists(components_dir):
            for file_name in os.listdir(components_dir):
                if file_name.endswith('.lnegc'):
                    file_path = os.path.join(components_dir, file_name)
                    parser = LNEGCParser(file_path)
                    self.components.append(parser.parse())
        
        # Processar entidades
        entities_dir = os.path.join(self.base_dir, 'entidades')
        if os.path.exists(entities_dir):
            for file_name in os.listdir(entities_dir):
                if file_name.endswith('.lnegc'):
                    file_path = os.path.join(entities_dir, file_name)
                    parser = LNEGCParser(file_path)
                    self.entities.append(parser.parse())
        
        # Processar interfaces
        interfaces_dir = os.path.join(self.base_dir, 'interfaces')
        if os.path.exists(interfaces_dir):
            for file_name in os.listdir(interfaces_dir):
                if file_name.endswith('.lnegc'):
                    file_path = os.path.join(interfaces_dir, file_name)
                    parser = LNEGCParser(file_path)
                    self.interfaces.append(parser.parse())
        
        # Processar testes
        tests_dir = os.path.join(self.base_dir, 'testes')
        if os.path.exists(tests_dir):
            for file_name in os.listdir(tests_dir):
                if file_name.endswith('.lnegc'):
                    file_path = os.path.join(tests_dir, file_name)
                    parser = LNEGCParser(file_path)
                    self.tests.append(parser.parse())
        
        return {
            'config': self.config,
            'components': self.components,
            'entities': self.entities,
            'interfaces': self.interfaces,
            'tests': self.tests
        }
    
    def generate_prompt(self, target_language: str = 'python') -> str:
        """Gera um prompt para alimentar uma IA com os dados processados."""
        prompt = f"# Geração de Código a partir de Especificação LNEGC\n\n"
        prompt += f"## Linguagem Alvo: {target_language}\n\n"
        
        if self.config:
            prompt += f"## Configuração do Projeto\n"
            prompt += f"Nome: {self.config['metadata'].get('nome', 'Projeto LNEGC')}\n"
            prompt += f"Versão: {self.config['metadata'].get('versao', '1.0.0')}\n"
            prompt += f"Domínio: {self.config['metadata'].get('dominio', 'Geração de Código')}\n\n"
        
        # Adicionar entidades
        if self.entities:
            prompt += f"## Entidades\n\n"
            for entity in self.entities:
                prompt += f"### {entity['metadata']['nome']}\n"
                if 'Atributos' in entity['sections']:
                    prompt += f"Atributos:\n{entity['sections']['Atributos']}\n\n"
                if 'Relacionamentos' in entity['sections']:
                    prompt += f"Relacionamentos:\n{entity['sections']['Relacionamentos']}\n\n"
        
        # Adicionar interfaces
        if self.interfaces:
            prompt += f"## Interfaces\n\n"
            for interface in self.interfaces:
                prompt += f"### {interface['metadata']['nome']}\n"
                if 'Métodos Requeridos' in interface['sections']:
                    prompt += f"Métodos:\n{interface['sections']['Métodos Requeridos']}\n\n"
        
        # Adicionar componentes
        if self.components:
            prompt += f"## Componentes\n\n"
            for component in self.components:
                prompt += f"### {component['metadata']['nome']}\n"
                if 'Interface' in component['sections']:
                    prompt += f"Interface:\n{component['sections']['Interface']}\n\n"
                if 'Algoritmo' in component['sections']:
                    prompt += f"Algoritmo:\n{component['sections']['Algoritmo']}\n\n"
        
        # Adicionar testes
        if self.tests:
            prompt += f"## Testes\n\n"
            for test in self.tests:
                prompt += f"### {test['metadata']['nome']}\n"
                if 'Cenários de Teste' in test['sections']:
                    prompt += f"Cenários:\n{test['sections']['Cenários de Teste']}\n\n"
        
        prompt += f"## Instruções\n\n"
        prompt += f"Com base na especificação LNEGC acima, gere o código completo em {target_language}.\n"
        prompt += f"Inclua todas as classes, interfaces, métodos e testes necessários.\n"
        prompt += f"Siga as melhores práticas de programação e padrões de projeto apropriados.\n"
        
        return prompt

def main():
    parser = argparse.ArgumentParser(description='Processador LNEGC')
    parser.add_argument('--dir', type=str, default='lnegc', help='Diretório base com arquivos LNEGC')
    parser.add_argument('--output', type=str, default='prompt.txt', help='Arquivo de saída para o prompt')
    parser.add_argument('--language', type=str, default='python', help='Linguagem alvo para geração de código')
    args = parser.parse_args()
    
    processor = LNEGCProcessor(args.dir)
    result = processor.process_all()
    
    # Gerar prompt para IA
    prompt = processor.generate_prompt(args.language)
    
    # Salvar prompt em arquivo
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(prompt)
    
    print(f"Processamento concluído. Prompt salvo em {args.output}")
    print(f"Componentes processados: {len(result['components'])}")
    print(f"Entidades processadas: {len(result['entities'])}")
    print(f"Interfaces processadas: {len(result['interfaces'])}")
    print(f"Testes processados: {len(result['tests'])}")

if __name__ == "__main__":
    main() 