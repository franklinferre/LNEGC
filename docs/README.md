# Linguagem Natural Estruturada para Geração de Código (LNEGC)

Esta especificação define uma linguagem natural controlada (CNL) otimizada para descrever algoritmos e estruturas de dados com propósito de geração automática de código por sistemas de IA. Inspirada em abordagens como CABERNET, REX, Gherkin e práticas de LLMs de código, a LNEGC combina a expressividade da linguagem natural com regras estruturais que reduzem ambiguidades.

## 1. Estrutura de Arquivos e Organização

```
/projeto
  /lnegc
    /componentes
      componente_1.lnegc
      componente_2.lnegc
    /entidades
      entidade_1.lnegc
      entidade_2.lnegc
    /interfaces
      interface_1.lnegc
    /testes
      teste_componente_1.lnegc
    config.lnegc
```

Cada arquivo `.lnegc` é um documento independente que segue as regras gramaticais desta linguagem. Os arquivos são agrupados por tipo para facilitar a organização e processamento.

## 2. Regras Gramaticais Básicas

A LNEGC segue um conjunto limitado de construções gramaticais para garantir interpretação consistente:

1. **Declarações** começam com um dos verbos de definição: `Definir`, `Criar`, `Implementar`
2. **Ações** usam verbos no infinitivo no início da frase
3. **Condições** seguem o padrão `Se [condição], então [ação]`
4. **Iterações** seguem o padrão `Para cada [item] em [coleção], [ação]`
5. **Propriedades** são definidas com o padrão `[entidade] tem [propriedade] como [tipo]`
6. **Relacionamentos** seguem o padrão `[entidade A] se relaciona com [entidade B] como [tipo de relação]`

Todas as frases devem terminar com ponto final. A indentação por 4 espaços indica hierarquia ou escopo.

## 3. Seções Padronizadas

### 3.1 Cabeçalho 

Todo arquivo LNEGC começa com um cabeçalho de metadados:

```
# [Nome do Componente/Entidade]
Versão: [X.Y.Z]
Autor: [Nome]
Data: [YYYY-MM-DD]
Domínio: [Contexto de aplicação]
Tags: [palavras-chave separadas por vírgula]
```

### 3.2 Descrição

Uma descrição em texto livre que contextualiza o propósito do componente. Embora em formato livre, deve seguir princípios de clareza e objetividade:

```
## Descrição
Este componente é responsável por [função principal] no contexto de [domínio].
Ele implementa [algoritmo/padrão] para [objetivo].
```

### 3.3 Dependências

Lista explícita de componentes, bibliotecas ou serviços externos necessários:

```
## Dependências
Requer [nome da dependência] para [propósito].
Utiliza [nome da biblioteca] versão [versão] ou superior.
```

### 3.4 Seções Específicas por Tipo de Arquivo

Dependendo do tipo de arquivo (componente, entidade, interface ou teste), seções específicas são definidas conforme as próximas partes.

## 4. Componentes

Um componente representa uma unidade funcional do software, como uma classe, módulo ou função.

### 4.1 Interface

```
## Interface

Definir [Nome] como [tipo de componente].

[Nome] aceita os seguintes parâmetros:
    - [nome do parâmetro]: [tipo] - [descrição] - [restrições]
    - [nome do parâmetro]: [tipo] - [descrição] - [opcional/obrigatório]

[Nome] retorna [tipo] que representa [descrição].

[Nome] pode lançar as seguintes exceções:
    - [nome da exceção]: quando [condição].
```

### 4.2 Algoritmo

```
## Algoritmo

Inicializar [variável] como [valor/tipo].

Se [condição], então:
    [ação]
Senão se [outra condição], então:
    [ação alternativa]
Senão:
    [ação padrão]

Para cada [item] em [coleção], fazer:
    [ação para cada item]
    Se [condição de parada], então:
        Parar iteração.

Enquanto [condição] for verdadeira, fazer:
    [ação repetitiva]

Chamar [outro componente] com [parâmetros].

Retornar [resultado].
```

### 4.3 Regras de Negócio

```
## Regras de Negócio

RN01: [Nome] deve [comportamento esperado] quando [condição].
RN02: Se [situação], então [Nome] deve [ação].
RN03: [Nome] não deve permitir [comportamento indesejado].
```

### 4.4 Exemplos

```
## Exemplos

Exemplo 1: [breve descrição]
    Entrada:
        [nome do parâmetro] = [valor]
        [nome do parâmetro] = [valor]
    Processamento:
        1. [etapa 1]
        2. [etapa 2]
    Saída:
        [valor esperado]

Exemplo 2: [outro cenário]
    ...
```

## 5. Entidades

Entidades representam estruturas de dados ou modelos de domínio.

### 5.1 Atributos

```
## Atributos

[Nome da entidade] tem os seguintes atributos:
    - [nome do atributo]: [tipo] - [descrição] - [restrições]
        Restrições: [lista de validações aplicáveis]
    - [nome do atributo]: [tipo] - [descrição]
        Valor padrão: [valor inicial]
```

### 5.2 Relacionamentos

```
## Relacionamentos

[Nome da entidade] se relaciona com [outra entidade] como [tipo de relação].
    Cardinalidade: [1:1, 1:N, N:M]
    Campos de ligação: [campo atual] referencia [campo da outra entidade]
    Comportamento em cascata: [ações de cascata]
```

### 5.3 Validações

```
## Validações

[Nome da entidade] exige que:
    - [atributo] seja [regra de validação].
    - [atributo] esteja entre [valor mínimo] e [valor máximo].
    - [atributo] siga o padrão [expressão regular/formato].
```

### 5.4 Exemplos de Instâncias

```
## Exemplos de Instâncias

Instância 1: [descrição do cenário]
    [atributo] = [valor]
    [atributo] = [valor]
    Relacionado a [outra entidade] com [atributo de ligação] = [valor]
```

## 6. Interfaces

Interfaces descrevem contratos que outros componentes podem implementar.

### 6.1 Métodos Requeridos

```
## Métodos Requeridos

[Nome da interface] exige a implementação de:

Método [nome do método]:
    Entrada:
        - [parâmetro]: [tipo] - [descrição]
    Saída:
        - [tipo retorno] - [descrição]
    Comportamento esperado:
        [descrição do que o método deve fazer]
```

### 6.2 Propriedades Requeridas

```
## Propriedades Requeridas

[Nome da interface] exige as seguintes propriedades:
    - [nome da propriedade]: [tipo] - [descrição]
        Acesso: [leitura/escrita/ambos]
```

## 7. Testes

Testes descrevem cenários de validação para componentes ou entidades.

### 7.1 Cenários de Teste

```
## Cenários de Teste

Cenário: [nome do cenário de teste]
    Dado que [pré-condição]
    E que [outra pré-condição]
    Quando [ação é executada]
    Então [resultado esperado]
    E [outro resultado esperado]
```

### 7.2 Mocks e Stubs

```
## Mocks e Stubs

Para testar [componente], é necessário simular:
    - [dependência] retornando [valor] quando [condição]
    - [serviço externo] que deve responder com [resposta]
```

## 8. Especificação de Banco de Dados

### 8.1 Definição de Esquema

```
## Esquema

Definir tabela [nome da tabela].

[Nome da tabela] tem as seguintes colunas:
    - [nome da coluna]: [tipo de dados] [restrições]
        Descrição: [finalidade desta coluna]
        Índice: [tipo de índice, se aplicável]
```

### 8.2 Índices

```
## Índices

[Nome da tabela] possui os seguintes índices:
    - [nome do índice] sobre ([coluna], [coluna]) - [tipo de índice]
        Propósito: [razão deste índice]
```

### 8.3 Procedimentos Armazenados

```
## Procedimentos Armazenados

Procedimento [nome do procedimento]:
    Parâmetros:
        - [nome]: [tipo] - [descrição]
    Lógica:
        1. [passo 1]
        2. [passo 2]
    Retorno:
        [tipo de resultado]
```

## 9. Construções Especiais

### 9.1 Fluxos de Processamento

Para descrever fluxos complexos, use a notação de passos numerados:

```
## Fluxo

Fluxo [nome do fluxo]:
    1. Iniciar com [entrada].
    2. Verificar se [condição].
    3. Se verdadeiro:
        3.1. Executar [ação A].
        3.2. Depois processar [subtarefa].
    4. Senão:
        4.1. Executar [ação B].
    5. Finalizar retornando [resultado].
```

### 9.2 Anotações de Otimização

Para indicar considerações de desempenho:

```
## Otimizações

@Cacheable: [nome do componente/método] deve cachear resultados por [tempo].
@Paralelo: [operação] pode ser executada em paralelo com tamanho de lote [N].
@Crítico: [operação] é um ponto crítico de desempenho.
```

### 9.3 Anotações de Segurança

```
## Segurança

@Autenticação: [operação] requer usuário autenticado.
@Autorização: [operação] requer as permissões [lista de permissões].
@Sanitização: [entrada] deve ser sanitizada contra [tipo de vulnerabilidade].
```

## 10. Exemplos Completos

### 10.1 Exemplo de Componente

```
# Validador de CPF
Versão: 1.0.0
Autor: João Silva
Data: 2025-04-06
Domínio: Validação de Documentos
Tags: validação, documento, brasil, cpf

## Descrição
Este componente verifica a validade de números de CPF brasileiros.
Implementa o algoritmo padrão de verificação com dígitos verificadores.

## Dependências
Requer StringUtils para formatação e limpeza.

## Interface

Definir ValidadorCPF como serviço.

ValidadorCPF aceita os seguintes parâmetros:
    - cpf: String - número do CPF a ser validado - obrigatório

ValidadorCPF retorna Boolean que representa se o CPF é válido.

ValidadorCPF pode lançar as seguintes exceções:
    - FormatoInvalidoException: quando o input não contém apenas números após limpeza.

## Algoritmo

Inicializar cpfLimpo como resultado da remoção de caracteres não numéricos.

Se comprimento de cpfLimpo for diferente de 11, então:
    Retornar falso.

Se cpfLimpo corresponder a um padrão de dígitos repetidos, então:
    Retornar falso.

Calcular primeiro dígito verificador:
    Inicializar soma como 0.
    Para cada posição de 0 a 8, fazer:
        Adicionar a soma o produto do dígito pela ponderação (10 - posição).
    Calcular resto da divisão de soma por 11.
    Se resto menor que 2, então:
        Definir dígito1 como 0.
    Senão:
        Definir dígito1 como (11 - resto).
    
Calcular segundo dígito verificador:
    Inicializar soma como 0.
    Para cada posição de 0 a 9, fazer:
        Adicionar a soma o produto do dígito pela ponderação (11 - posição).
    Calcular resto da divisão de soma por 11.
    Se resto menor que 2, então:
        Definir dígito2 como 0.
    Senão:
        Definir dígito2 como (11 - resto).

Se dígito1 for igual ao valor na posição 9 e dígito2 for igual ao valor na posição 10, então:
    Retornar verdadeiro.
Senão:
    Retornar falso.

## Regras de Negócio

RN01: ValidadorCPF deve rejeitar CPFs com todos os dígitos idênticos.
RN02: ValidadorCPF deve considerar válido apenas CPFs que atendam ao algoritmo dos dígitos verificadores.
RN03: ValidadorCPF deve limpar formatação (pontos e traços) antes da validação.

## Exemplos

Exemplo 1: CPF válido
    Entrada:
        cpf = "529.982.247-25"
    Processamento:
        1. Limpar para "52998224725"
        2. Verificar comprimento (11 dígitos) ✓
        3. Verificar padrão de repetição ✓
        4. Calcular primeiro dígito verificador -> 2 ✓
        5. Calcular segundo dígito verificador -> 5 ✓
    Saída:
        true

Exemplo 2: CPF inválido (dígitos incorretos)
    Entrada:
        cpf = "529.982.247-26"
    Saída:
        false
```

### 10.2 Exemplo de Entidade

```
# Cliente
Versão: 1.0.0
Autor: Maria Santos
Data: 2025-04-06
Domínio: Gestão de Clientes
Tags: cliente, pessoa, cadastro

## Descrição
Entidade que representa um cliente no sistema de CRM.
Armazena dados pessoais e informações de contato.

## Atributos

Cliente tem os seguintes atributos:
    - id: UUID - identificador único - obrigatório
        Restrições: gerado automaticamente
    - nome: String - nome completo do cliente - obrigatório
        Restrições: mínimo 3 caracteres, máximo 100 caracteres
    - cpf: String - número de documento CPF - obrigatório
        Restrições: deve ser um CPF válido conforme ValidadorCPF
    - dataNascimento: Date - data de nascimento - obrigatório
        Restrições: deve ser data no passado, cliente deve ter ao menos 18 anos
    - email: String - endereço de e-mail principal - obrigatório
        Restrições: deve seguir o formato de e-mail válido
    - telefone: String - número de telefone com DDD - opcional
        Restrições: apenas números, entre 10 e 11 dígitos
    - endereco: Endereco - endereço principal - opcional
    - dataRegistro: DateTime - momento de criação do cadastro - obrigatório
        Valor padrão: data e hora atual
    - status: Enum(ATIVO, INATIVO, BLOQUEADO) - situação atual - obrigatório
        Valor padrão: ATIVO

## Relacionamentos

Cliente se relaciona com Pedido como um-para-muitos.
    Cardinalidade: 1:N
    Campos de ligação: id referencia Pedido.clienteId
    Comportamento em cascata: nenhum

Cliente se relaciona com Categoria como muitos-para-muitos.
    Cardinalidade: N:M
    Tabela de junção: ClienteCategoria
    Campos de ligação: id referencia ClienteCategoria.clienteId

## Validações

Cliente exige que:
    - nome seja composto apenas por letras, espaços e hífens.
    - email seja único no sistema.
    - não seja possível alterar o CPF após a criação.

## Exemplos de Instâncias

Instância 1: Cliente padrão
    id = "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    nome = "João da Silva"
    cpf = "52998224725"
    dataNascimento = "1985-07-15"
    email = "joao.silva@exemplo.com"
    telefone = "11987654321"
    endereco = Referência para Endereco#123
    dataRegistro = "2025-01-10T14:30:00Z"
    status = ATIVO
```

## 11. Práticas Recomendadas

### 11.1 Gerais

1. **Seja específico e preciso**: Evite termos vagos como "processar dados" - especifique exatamente qual processamento.
2. **Uma ação por linha**: Cada linha deve descrever apenas uma operação atômica.
3. **Nomes significativos**: Use nomes que descrevem o propósito (ex: `calcularImpostoTotal` em vez de `calcular`).
4. **Evite negações duplas**: Use "Se idade maior que 18" em vez de "Se não for menor ou igual a 18".

### 11.2 Para otimização de IA

1. **Inclua exemplos concretos**: Sempre forneça pelo menos um exemplo de entrada/saída.
2. **Especifique tipos explicitamente**: Nunca deixe o tipo de dado implícito.
3. **Expresse regras como afirmações**: "X deve ser Y" é melhor que "X não pode ser não-Y".
4. **Decomponha algoritmos complexos**: Use subseções ou etapas numeradas para clareza.
5. **Defina termos de domínio**: Inclua um glossário ou definições para termos específicos do negócio.

### 11.3 Consistência sintática

1. **Tempo verbal**: Use verbos no infinitivo para ações (Calcular, Verificar, Buscar).
2. **Estruturas condicionais**: Sempre use o formato "Se [condição], então: [consequência]".
3. **Listas**: Use marcadores consistentes (traços) para listas.
4. **Indentação**: Use 4 espaços para indicar hierarquia.

## 12. Extensibilidade

A LNEGC pode ser estendida conforme necessário, seguindo estas diretrizes:

1. Novas seções devem começar com `##` seguido do nome da seção.
2. Novas construções gramaticais devem ser documentadas e seguir os padrões existentes.
3. Extensões específicas de domínio devem ser agrupadas em seções com prefixo do domínio.

## 13. Conversão para Código

A LNEGC foi projetada para ser traduzida automaticamente para código. O processo típico segue estas etapas:

1. **Parsing:** Análise sintática do arquivo LNEGC
2. **Representação intermediária:** Geração de um AST ou modelo abstrato
3. **Geração de código:** Transformação para código-fonte na linguagem alvo
4. **Validação:** Verificação de consistência entre especificação e código

Implementações podem usar diferentes abordagens:
- Ferramentas baseadas em regras/templates
- Modelos de IA generativa com prompts estruturados
- Geradores de código DSL-to-code
- Compiladores customizados

## 14. Integração com IDEs e Ferramentas

LNEGC pode ser integrada com ferramentas de desenvolvimento através de:

1. **Extensões de editor:** Realce de sintaxe, autocompletar e validação em tempo real
2. **Geradores de código interativos:** Assistentes que geram código a partir de descrições LNEGC
3. **Sincronização bidirecional:** Atualizações de código refletidas na especificação LNEGC e vice-versa
4. **Validação automática:** Verificação de consistência entre especificação e implementação

## 15. Glossário

- **CNL:** Controlled Natural Language (Linguagem Natural Controlada)
- **DSL:** Domain-Specific Language (Linguagem Específica de Domínio)
- **LNEGC:** Linguagem Natural Estruturada para Geração de Código
- **Entidade:** Estrutura de dados ou modelo de domínio
- **Componente:** Unidade funcional como classe, módulo ou função
- **Interface:** Contrato que define comportamentos a serem implementados