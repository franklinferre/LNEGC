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
        self.target_language = target_language or 'python'  # Define python como padrão inicial
        
        # Carrega a configuração automaticamente se o diretório existir
        if self.directory.exists():
            try:
                self._load_config()
            except FileNotFoundError:
                # Se não encontrar o arquivo de configuração, mantém as configurações padrão
                pass

    def _load_config(self) -> None:
        """Carrega o arquivo de configuração do projeto."""
        config_paths = [
            self.directory / "config.lnegc",
            self.directory / ".lnegc" / "config.lnegc",
            Path(self.directory).parent / ".lnegc" / "config.lnegc",
            Path(self.directory).parent / "config.lnegc",
            Path(self.directory).parent.parent / ".lnegc" / "config.lnegc",
            Path(self.directory).parent.parent / "config.lnegc"
        ]

        config_file = None
        for path in config_paths:
            if path.exists():
                print(f"Carregando configuração de: {path}")
                config_file = path
                break

        if not config_file:
            paths_str = "\n".join(str(p) for p in config_paths)
            raise FileNotFoundError(
                f"Arquivo de configuração não encontrado. Tentei os seguintes caminhos:\n{paths_str}"
            )

        # Lê o arquivo de configuração
        with open(config_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Procura a linguagem nas configurações
        for line in content.split('\n'):
            if '**Linguagem**:' in line:
                self.target_language = line.split(':')[1].strip().lower()
                break

    def _load_files(self) -> None:
        """Carrega todos os arquivos .lnegc do projeto."""
        # Carrega componentes
        components_dir = self.directory
        if components_dir.exists():
            for file in components_dir.glob("**/*.lnegc"):
                if "componentes" in str(file) or "components" in str(file):
                    parser = LNEGCParser(file)
                    self._components.append(parser.parse())

        # Carrega entidades
        entities_dir = self.directory
        if entities_dir.exists():
            for file in entities_dir.glob("**/*.lnegc"):
                if "entidades" in str(file) or "entities" in str(file):
                    parser = LNEGCParser(file)
                    self._entities.append(parser.parse())

        # Carrega interfaces
        interfaces_dir = self.directory
        if interfaces_dir.exists():
            for file in interfaces_dir.glob("**/*.lnegc"):
                if "interfaces" in str(file):
                    parser = LNEGCParser(file)
                    self._interfaces.append(parser.parse())

        # Carrega testes
        tests_dir = self.directory
        if tests_dir.exists():
            for file in tests_dir.glob("**/*.lnegc"):
                if "testes" in str(file) or "tests" in str(file):
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

        # Sempre inclui a implementação padrão
        prompt += f"\nImplementação de Referência:\n{self.implementacao_padrao}"

        return prompt

    def _generate_entity_prompt(self, entity: dict) -> str:
        """Gera o prompt para uma entidade."""
        metadata = entity.get('metadata', {})
        attributes = entity.get('attributes', [])
        validations = entity.get('validations', [])
        relationships = entity.get('relationships', [])
        methods = entity.get('methods', [])
        indexes = entity.get('indexes', [])
        permissions = entity.get('permissions', [])
        audit = entity.get('auditoria', [])

        prompt = f"""Por favor, gere uma entidade em {self.target_language} com as seguintes especificações:

# Metadados
- Nome: {metadata.get('Nome', 'Não definido')}
- Tipo: {metadata.get('Tipo', 'Não definido')}
- Descrição: {metadata.get('Descrição', 'Não definido')}
- Autor: {metadata.get('Autor', 'Não definido')}
- Versão: {metadata.get('Versão', 'Não definido')}

# Atributos
{self._format_attributes(attributes)}

# Validações de Negócio
{self._format_validations(validations)}

# Relacionamentos
{self._format_relationships(relationships)}

# Métodos de Domínio
{self._format_methods(methods)}

# Índices do Banco de Dados
{self._format_indexes(indexes)}

# Regras de Permissão
{self._format_permissions(permissions)}

# Requisitos de Auditoria
{self._format_audit(audit)}

# Requisitos Técnicos
1. Use TypeScript com decorators para validação
2. Implemente validações usando Zod
3. Use classes de domínio com encapsulamento
4. Implemente todos os métodos de domínio
5. Adicione validações de negócio
6. Use tipos fortes e interfaces
7. Implemente tratamento de erros
8. Adicione documentação JSDoc
9. Siga os princípios SOLID
10. Implemente testes unitários

# Exemplo de Implementação
```typescript
import {{ z }} from 'zod';
import {{ Entity, Column, PrimaryGeneratedColumn, CreateDateColumn, UpdateDateColumn }} from 'typeorm';

/* Schema de validação */
export const entitySchema = z.object({{
    /* ... schema definition */
}});

/* Interface da entidade */
export interface IEntity {{
    /* ... interface definition */
}}

/* Classe de domínio */
export class EntityDomain {{
    constructor(private data: IEntity) {{
        this.validate();
    }}

    private validate(): void {{
        /* Validações de negócio */
    }}

    /* Métodos de domínio */
}}

/* Entidade do banco de dados */
@Entity()
export class EntityModel {{
    /* ... entity definition */
}}
```

Por favor, gere uma implementação completa seguindo estas especificações e requisitos técnicos."""
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
        # Sempre inclui a implementação padrão
        prompt += f"\nImplementação de Referência:\n{self.implementacao_padrao_interface}"

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
{test['sections'].get('Cenários', test['sections'].get('CENÁRIOS', '''
1. CPF Válido
   Entrada: "529.982.247-25"
   Esperado: true
   Descrição: Deve retornar true para um CPF válido

2. CPF Inválido
   Entrada: "529.982.247-26"
   Esperado: false
   Descrição: Deve retornar false para um CPF inválido

3. CPF com Dígitos Iguais
   Entrada: "111.111.111-11"
   Esperado: false
   Descrição: Deve retornar false para CPF com todos dígitos iguais

4. CPF com Formato Inválido
   Entrada: "123.456.789"
   Esperado: Error
   Descrição: Deve lançar erro para CPF com formato inválido'''))}

Mocks:
{test['sections'].get('Mocks', test['sections'].get('MOCKS', '''
- Não são necessários mocks para estes testes
'''))}

Fixtures:
{test['sections'].get('Fixtures', test['sections'].get('FIXTURES', '''
- cpfsValidos: Array de CPFs válidos para teste
- cpfsInvalidos: Array de CPFs inválidos para teste
'''))}
"""
        # Sempre inclui a implementação padrão
        prompt += f"\nImplementação de Referência:\n{self.implementacao_padrao_teste}"

        return prompt

    @property
    def implementacao_padrao(self) -> str:
        return '''```typescript
import { useState, useEffect } from 'react';

interface ValidadorCPFProps {
    cpf: string;
    onValidate?: (isValid: boolean) => void;
}

export const ValidadorCPF: React.FC<ValidadorCPFProps> = ({ cpf, onValidate }) => {
    // Estado para controlar a validação
    const [isValid, setIsValid] = useState<boolean>(false);
    const [error, setError] = useState<string | null>(null);

    // Função de validação do CPF
    const validarCPF = (cpf: string): boolean => {
        // Remove caracteres não numéricos
        const cpfLimpo = cpf.replace(/\D/g, '');
        
        // Verifica se tem 11 dígitos
        if (cpfLimpo.length !== 11) {
            throw new Error("CPF deve ter 11 dígitos");
        }
        
        // Verifica se todos os dígitos são iguais
        if (new Set(cpfLimpo).size === 1) {
            return false;
        }
        
        // Calcula primeiro dígito verificador
        let soma = 0;
        for (let i = 0; i < 9; i++) {
            soma += parseInt(cpfLimpo[i]) * (10 - i);
        }
        let digito1 = (soma * 10) % 11;
        if (digito1 === 10) digito1 = 0;
        
        // Calcula segundo dígito verificador
        soma = 0;
        for (let i = 0; i < 10; i++) {
            soma += parseInt(cpfLimpo[i]) * (11 - i);
        }
        let digito2 = (soma * 10) % 11;
        if (digito2 === 10) digito2 = 0;
        
        // Verifica os dígitos
        return cpfLimpo.slice(-2) === `${digito1}${digito2}`;
    };

    // Efeito para validar o CPF quando mudar
    useEffect(() => {
        try {
            const resultado = validarCPF(cpf);
            setIsValid(resultado);
            setError(null);
            onValidate?.(resultado);
        } catch (erro) {
            setIsValid(false);
            setError(erro.message);
            onValidate?.(false);
        }
    }, [cpf, onValidate]);

    return (
        <div className="validador-cpf">
            <div className={`status ${isValid ? 'valido' : 'invalido'}`}>
                {isValid ? '✓ CPF Válido' : '✗ CPF Inválido'}
            </div>
            {error && <div className="erro">{error}</div>}
        </div>
    );
};
```'''

    @property
    def implementacao_padrao_entidade(self) -> str:
        return '''```typescript
import { z } from 'zod';

// Definição do schema de validação
export const clienteSchema = z.object({
    id: z.number(),
    nome: z.string().min(3).max(100),
    email: z.string().email(),
    cpf: z.string(),
    telefone: z.string().regex(/^\(\d{2}\) \d{5}-\d{4}$/).optional(),
    dataNascimento: z.date().max(new Date()).optional(),
    ativo: z.boolean().default(true)
});

// Tipo gerado a partir do schema
export type Cliente = z.infer<typeof clienteSchema>;

// Classe de domínio
export class ClienteDomain {
    constructor(private data: Cliente) {
        this.validar();
    }

    private validar(): void {
        // Valida usando o schema
        const resultado = clienteSchema.safeParse(this.data);
        
        if (!resultado.success) {
            throw new Error(resultado.error.message);
        }
        
        // Validações adicionais
        if (!validarCPF(this.data.cpf)) {
            throw new Error("CPF inválido");
        }
    }

    // Getters
    get id(): number { return this.data.id; }
    get nome(): string { return this.data.nome; }
    get email(): string { return this.data.email; }
    get cpf(): string { return this.data.cpf; }
    get telefone(): string | undefined { return this.data.telefone; }
    get dataNascimento(): Date | undefined { return this.data.dataNascimento; }
    get ativo(): boolean { return this.data.ativo; }

    // Métodos de domínio
    desativar(): void {
        this.data.ativo = false;
    }

    ativar(): void {
        this.data.ativo = true;
    }

    atualizarTelefone(novoTelefone?: string): void {
        if (novoTelefone && !/^\(\d{2}\) \d{5}-\d{4}$/.test(novoTelefone)) {
            throw new Error("Telefone deve seguir formato (XX) XXXXX-XXXX");
        }
        this.data.telefone = novoTelefone;
    }
}
```'''

    @property
    def implementacao_padrao_interface(self) -> str:
        return '''```typescript
import { z } from 'zod';

// Interface genérica para o repositório
export interface IRepositorio<T> {
    criar(entidade: T): Promise<T>;
    ler(id: number): Promise<T>;
    atualizar(entidade: T): Promise<T>;
    deletar(id: number): Promise<boolean>;
    listar(): Promise<T[]>;
    buscar(filtro: Record<string, unknown>): Promise<T[]>;
}

// Implementação base abstrata
export abstract class RepositorioBase<T extends { id: number }> implements IRepositorio<T> {
    protected cache: Map<number, T> = new Map();
    protected logger: Logger;

    constructor(logger: Logger) {
        this.logger = logger;
    }

    // Método para invalidar o cache
    protected invalidarCache(): void {
        this.cache.clear();
        this.logger.info('Cache invalidado');
    }

    // Implementação dos métodos abstratos
    abstract criar(entidade: T): Promise<T>;
    abstract ler(id: number): Promise<T>;
    abstract atualizar(entidade: T): Promise<T>;
    abstract deletar(id: number): Promise<boolean>;
    abstract listar(): Promise<T[]>;
    abstract buscar(filtro: Record<string, unknown>): Promise<T[]>;
}

// Exemplo de implementação concreta
export class ClienteRepositorio extends RepositorioBase<Cliente> {
    async criar(cliente: Cliente): Promise<Cliente> {
        try {
            // Implementação específica para persistir o cliente
            const resultado = await db.clientes.create(cliente);
            
            // Invalida o cache após a escrita
            this.invalidarCache();
            
            return resultado;
        } catch (erro) {
            this.logger.error('Erro ao criar cliente:', erro);
            throw erro;
        }
    }

    // ... implementação dos outros métodos
}
```'''

    @property
    def implementacao_padrao_teste(self) -> str:
        return '''```typescript
import { describe, it, expect } from 'vitest';
import { validarCPF } from '../components/ValidadorCPF';

describe('ValidadorCPF', () => {
    // Fixtures
    const cpfsValidos = [
        '529.982.247-25',
        '123.456.789-09',
        '111.444.777-35'
    ];

    const cpfsInvalidos = [
        '529.982.247-26',
        '123.456.789-10',
        '111.111.111-11'
    ];

    // Testes para CPFs válidos
    it('deve retornar true para CPFs válidos', () => {
        cpfsValidos.forEach(cpf => {
            expect(validarCPF(cpf)).toBe(true);
        });
    });

    // Testes para CPFs inválidos
    it('deve retornar false para CPFs inválidos', () => {
        cpfsInvalidos.forEach(cpf => {
            expect(validarCPF(cpf)).toBe(false);
        });
    });

    // Teste para CPF com dígitos iguais
    it('deve retornar false para CPF com todos os dígitos iguais', () => {
        expect(validarCPF('111.111.111-11')).toBe(false);
        expect(validarCPF('000.000.000-00')).toBe(false);
    });

    // Teste para CPF com formato inválido
    it('deve lançar erro para CPF com formato inválido', () => {
        expect(() => validarCPF('123.456.789')).toThrow('CPF deve ter 11 dígitos');
        expect(() => validarCPF('')).toThrow('CPF deve ter 11 dígitos');
    });
});
```'''

    def process(self) -> Dict[str, List[str]]:
        """
        Processa todos os arquivos do projeto e gera os prompts.

        Returns:
            Dicionário com os prompts gerados para cada tipo de arquivo
        """
        self._load_config()  # Carrega configuração apenas quando necessário
        self._load_files()

        # Usa dicionários para garantir unicidade baseada no nome do arquivo
        unique_components = {}
        unique_entities = {}
        unique_interfaces = {}
        unique_tests = {}

        # Processa componentes
        for c in self._components:
            file_name = c.get('metadata', {}).get('nome', 'Componente')
            c = c.copy()  # Cria uma cópia para não modificar o original
            if 'sections' in c:
                c['sections'] = c['sections'].copy()
                c['sections'].pop('Implementação', None)
                c['sections'].pop('IMPLEMENTAÇÃO', None)
            unique_components[file_name] = c

        # Processa entidades
        for e in self._entities:
            file_name = e.get('metadata', {}).get('nome', 'Entidade')
            e = e.copy()  # Cria uma cópia para não modificar o original
            if 'sections' in e:
                e['sections'] = e['sections'].copy()
                e['sections'].pop('Implementação', None)
                e['sections'].pop('IMPLEMENTAÇÃO', None)
            unique_entities[file_name] = e

        # Processa interfaces
        for i in self._interfaces:
            file_name = i.get('metadata', {}).get('nome', 'Interface')
            i = i.copy()  # Cria uma cópia para não modificar o original
            if 'sections' in i:
                i['sections'] = i['sections'].copy()
                i['sections'].pop('Implementação', None)
                i['sections'].pop('IMPLEMENTAÇÃO', None)
            unique_interfaces[file_name] = i

        # Processa testes
        for t in self._tests:
            file_name = t.get('metadata', {}).get('nome', 'Teste')
            t = t.copy()  # Cria uma cópia para não modificar o original
            if 'sections' in t:
                t['sections'] = t['sections'].copy()
                t['sections'].pop('Implementação', None)
                t['sections'].pop('IMPLEMENTAÇÃO', None)
            unique_tests[file_name] = t

        # Gera os prompts com as implementações padrão
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

    def _format_attributes(self, attributes: List[str]) -> str:
        """Formata a lista de atributos para o prompt."""
        if not attributes:
            return "Sem atributos definidos."
        return "\n".join(f"- {attr}" for attr in attributes)

    def _format_validations(self, validations: List[str]) -> str:
        """Formata a lista de validações para o prompt."""
        if not validations:
            return "Sem validações definidas."
        return "\n".join(f"- {val}" for val in validations)

    def _format_relationships(self, relationships: List[str]) -> str:
        """Formata a lista de relacionamentos para o prompt."""
        if not relationships:
            return "Sem relacionamentos definidos."
        return "\n".join(f"- {rel}" for rel in relationships)

    def _format_methods(self, methods: List[str]) -> str:
        """Formata a lista de métodos para o prompt."""
        if not methods:
            return "Sem métodos definidos."
        return "\n".join(f"- {method}" for method in methods)

    def _format_indexes(self, indexes: List[str]) -> str:
        """Formata a lista de índices para o prompt."""
        if not indexes:
            return "Sem índices definidos."
        return "\n".join(f"- {idx}" for idx in indexes)

    def _format_permissions(self, permissions: List[str]) -> str:
        """Formata a lista de permissões para o prompt."""
        if not permissions:
            return "Sem permissões definidas."
        return "\n".join(f"- {perm}" for perm in permissions)

    def _format_audit(self, audit: List[str]) -> str:
        """Formata a lista de requisitos de auditoria para o prompt."""
        if not audit:
            return "Sem requisitos de auditoria definidos."
        return "\n".join(f"- {req}" for req in audit) 