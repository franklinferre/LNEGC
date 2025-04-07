# Especificação dos Prompts LNEGC

Este documento define a especificação dos prompts gerados pelo processador LNEGC.

## 1. Estrutura do Prompt

O prompt gerado segue uma estrutura padronizada:

```
# Título
[Descrição do componente/entidade/interface]

## Contexto
[Informações de contexto e domínio]

## Requisitos
[Lista de requisitos e restrições]

## Implementação
[Instruções de implementação]

## Exemplos
[Exemplos de uso]

## Testes
[Cenários de teste]
```

## 2. Seções do Prompt

### 2.1 Título

O título é extraído do cabeçalho do arquivo `.lnegc`:

```
# Nome do Componente/Entidade/Interface
```

### 2.2 Descrição

A descrição é gerada a partir do contexto do arquivo:

```
Este componente/entidade/interface é responsável por [responsabilidade].
Ele é parte do domínio [domínio] e segue as seguintes regras de negócio:
- [regra 1]
- [regra 2]
- [regra 3]
```

### 2.3 Contexto

O contexto é construído a partir das tags e metadados:

```
## Contexto

- **Domínio**: [domínio]
- **Tags**: [tags]
- **Versão**: [versão]
- **Autor**: [autor]
- **Data**: [data]
```

### 2.4 Requisitos

Os requisitos são extraídos das seções relevantes:

```
## Requisitos

### Funcionais
- [requisito 1]
- [requisito 2]
- [requisito 3]

### Não Funcionais
- [requisito 1]
- [requisito 2]
- [requisito 3]
```

### 2.5 Implementação

A seção de implementação é gerada a partir do algoritmo:

```
## Implementação

### Interface
```typescript
interface Nome {
    // propriedades
    prop1: Tipo1;
    prop2: Tipo2;
    
    // métodos
    metodo1(): Retorno1;
    metodo2(param: Tipo3): Retorno2;
}
```

### Algoritmo
1. [passo 1]
2. [passo 2]
3. [passo 3]

### Tratamento de Erros
- [erro 1]: [tratamento]
- [erro 2]: [tratamento]
```

### 2.6 Exemplos

Os exemplos são formatados de acordo com o tipo:

```
## Exemplos

### Exemplo 1: [descrição]
```typescript
// código de exemplo
const resultado = componente.metodo(param);
console.log(resultado);
```

### Exemplo 2: [descrição]
```typescript
// código de exemplo
try {
    const resultado = componente.metodo(param);
} catch (erro) {
    console.error(erro);
}
```
```

### 2.7 Testes

Os testes são gerados a partir dos cenários:

```
## Testes

### Cenário 1: [descrição]
```typescript
describe('Nome', () => {
    it('deve [comportamento esperado]', () => {
        // arrange
        const input = ...;
        
        // act
        const result = ...;
        
        // assert
        expect(result).toBe(...);
    });
});
```

### Cenário 2: [descrição]
```typescript
describe('Nome', () => {
    it('deve [comportamento esperado]', () => {
        // arrange
        const input = ...;
        
        // act & assert
        expect(() => {
            // código que deve lançar erro
        }).toThrow(ErroEsperado);
    });
});
```
```

## 3. Templates por Tipo

### 3.1 Componente

```
# [Nome do Componente]

[Descrição do componente]

## Contexto
[Contexto do componente]

## Requisitos
[Requisitos do componente]

## Implementação

### Interface
[Interface do componente]

### Algoritmo
[Algoritmo do componente]

### Tratamento de Erros
[Tratamento de erros]

## Exemplos
[Exemplos de uso]

## Testes
[Cenários de teste]
```

### 3.2 Entidade

```
# [Nome da Entidade]

[Descrição da entidade]

## Contexto
[Contexto da entidade]

## Requisitos
[Requisitos da entidade]

## Implementação

### Atributos
[Atributos da entidade]

### Relacionamentos
[Relacionamentos da entidade]

### Validações
[Validações da entidade]

## Exemplos
[Exemplos de uso]

## Testes
[Cenários de teste]
```

### 3.3 Interface

```
# [Nome da Interface]

[Descrição da interface]

## Contexto
[Contexto da interface]

## Requisitos
[Requisitos da interface]

## Implementação

### Métodos
[Métodos da interface]

### Propriedades
[Propriedades da interface]

### Eventos
[Eventos da interface]

## Exemplos
[Exemplos de uso]

## Testes
[Cenários de teste]
```

## 4. Formatação

### 4.1 Markdown

O prompt é formatado em Markdown para melhor legibilidade:

- Títulos usam `#`
- Listas usam `-`
- Código usa ``` ```
- Ênfase usa `*` ou `_`

### 4.2 Código

O código é formatado de acordo com a linguagem alvo:

```typescript
// TypeScript
interface Nome {
    prop: Tipo;
    metodo(): Retorno;
}
```

```python
# Python
class Nome:
    def __init__(self):
        self.prop = None
    
    def metodo(self) -> Retorno:
        pass
```

```java
// Java
public class Nome {
    private Tipo prop;
    
    public Retorno metodo() {
        return null;
    }
}
```

## 5. Personalização

### 5.1 Variáveis

O prompt pode incluir variáveis para personalização:

```
# ${nome}
[${descricao}]

## Contexto
- **Domínio**: ${dominio}
- **Tags**: ${tags}
```

### 5.2 Condicionais

Seções podem ser condicionais:

```
#if ${tem_interface}
## Interface
${interface}
#endif

#if ${tem_testes}
## Testes
${testes}
#endif
```

### 5.3 Loops

Listas podem ser geradas com loops:

```
## Requisitos
#for ${requisito} in ${requisitos}
- ${requisito}
#end
```

## 6. Validação

### 6.1 Estrutura

O prompt deve seguir a estrutura definida:

1. Título
2. Descrição
3. Contexto
4. Requisitos
5. Implementação
6. Exemplos
7. Testes

### 6.2 Conteúdo

O conteúdo deve ser válido:

- Código deve ser sintaticamente correto
- Exemplos devem ser executáveis
- Testes devem ser completos

### 6.3 Formatação

A formatação deve ser consistente:

- Indentação correta
- Espaçamento adequado
- Markdown válido

## 7. Exemplos

### 7.1 Componente

```
# Calculadora

Este componente implementa operações matemáticas básicas.

## Contexto
- **Domínio**: Matemática
- **Tags**: calculadora, operações, matemática
- **Versão**: 1.0.0
- **Autor**: João Silva
- **Data**: 2024-03-20

## Requisitos

### Funcionais
- Implementar operações básicas (soma, subtração, multiplicação, divisão)
- Validar entrada de dados
- Tratar divisão por zero

### Não Funcionais
- Performance: operações devem ser O(1)
- Memória: uso mínimo de memória
- Thread-safe: operações thread-safe

## Implementação

### Interface
```typescript
interface Calculadora {
    soma(a: number, b: number): number;
    subtracao(a: number, b: number): number;
    multiplicacao(a: number, b: number): number;
    divisao(a: number, b: number): number;
}
```

### Algoritmo
1. Receber operação e operandos
2. Validar operandos
3. Executar operação
4. Retornar resultado

### Tratamento de Erros
- DivisaoPorZero: quando divisor é zero
- OperandosInvalidos: quando operandos não são números

## Exemplos

### Exemplo 1: Soma
```typescript
const calc = new Calculadora();
const resultado = calc.soma(5, 3);
console.log(resultado); // 8
```

### Exemplo 2: Divisão por Zero
```typescript
const calc = new Calculadora();
try {
    const resultado = calc.divisao(10, 0);
} catch (erro) {
    console.error(erro); // DivisaoPorZero: Divisor não pode ser zero
}
```

## Testes

### Cenário 1: Soma de Números Positivos
```typescript
describe('Calculadora', () => {
    it('deve somar dois números positivos', () => {
        const calc = new Calculadora();
        const resultado = calc.soma(5, 3);
        expect(resultado).toBe(8);
    });
});
```

### Cenário 2: Divisão por Zero
```typescript
describe('Calculadora', () => {
    it('deve lançar erro ao dividir por zero', () => {
        const calc = new Calculadora();
        expect(() => {
            calc.divisao(10, 0);
        }).toThrow(DivisaoPorZero);
    });
});
```
```

### 7.2 Entidade

```
# Usuário

Esta entidade representa um usuário do sistema.

## Contexto
- **Domínio**: Autenticação
- **Tags**: usuário, autenticação, perfil
- **Versão**: 1.0.0
- **Autor**: Maria Santos
- **Data**: 2024-03-20

## Requisitos

### Funcionais
- Armazenar dados do usuário
- Validar dados do usuário
- Gerenciar relacionamentos

### Não Funcionais
- Performance: consultas otimizadas
- Segurança: dados sensíveis criptografados
- Integridade: dados consistentes

## Implementação

### Atributos
```typescript
interface Usuario {
    id: number;
    nome: string;
    email: string;
    senha: string;
    dataCriacao: Date;
    ativo: boolean;
}
```

### Relacionamentos
- Um-para-um com Perfil
- Um-para-muitos com Permissões
- Muitos-para-muitos com Grupos

### Validações
- Nome: mínimo 3 caracteres
- Email: formato válido
- Senha: mínimo 8 caracteres, números, maiúsculas, minúsculas e especiais

## Exemplos

### Exemplo 1: Criar Usuário
```typescript
const usuario = new Usuario({
    nome: 'João Silva',
    email: 'joao@email.com',
    senha: 'Senha123!'
});
await usuario.save();
```

### Exemplo 2: Validar Senha
```typescript
const usuario = await Usuario.findById(1);
const senhaValida = usuario.validarSenha('Senha123!');
console.log(senhaValida); // true
```

## Testes

### Cenário 1: Criar Usuário Válido
```typescript
describe('Usuário', () => {
    it('deve criar usuário com dados válidos', async () => {
        const usuario = new Usuario({
            nome: 'João Silva',
            email: 'joao@email.com',
            senha: 'Senha123!'
        });
        await expect(usuario.save()).resolves.toBeDefined();
    });
});
```

### Cenário 2: Validar Senha Inválida
```typescript
describe('Usuário', () => {
    it('deve rejeitar senha fraca', () => {
        const usuario = new Usuario();
        expect(() => {
            usuario.senha = '123';
        }).toThrow(SenhaInvalida);
    });
});
```
```

## 8. Integração

### 8.1 IDEs

O prompt pode ser integrado com IDEs:

- VSCode: extensão para preview
- IntelliJ: plugin para formatação
- Eclipse: plugin para geração

### 8.2 Ferramentas

Ferramentas de suporte:

- Linters: validação de código
- Formatadores: formatação consistente
- Geradores: geração de código

### 8.3 APIs

APIs de integração:

- REST: geração de prompts
- GraphQL: consulta de templates
- WebSocket: atualização em tempo real

## 9. Manutenção

### 9.1 Versionamento

O prompt deve ser versionado:

- Seguir SemVer
- Manter changelog
- Preservar compatibilidade

### 9.2 Documentação

Documentação necessária:

- Guias de uso
- Exemplos práticos
- Troubleshooting

### 9.3 Suporte

Canais de suporte:

- Issues no GitHub
- Fórum de discussão
- Documentação online 