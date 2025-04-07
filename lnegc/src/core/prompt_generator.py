from typing import List

class PromptGenerator:
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
import { z } from 'zod';
import { Entity, Column, PrimaryGeneratedColumn, CreateDateColumn, UpdateDateColumn } from 'typeorm';

// Schema de validação
export const entitySchema = z.object({
    // ... schema definition
});

// Interface da entidade
export interface IEntity {
    // ... interface definition
}

// Classe de domínio
export class EntityDomain {
    constructor(private data: IEntity) {
        this.validate();
    }

    private validate(): void {
        // Validações de negócio
    }

    // Métodos de domínio
}

// Entidade do banco de dados
@Entity()
export class EntityModel {
    // ... entity definition
}
```

Por favor, gere uma implementação completa seguindo estas especificações e requisitos técnicos."""
        return prompt

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