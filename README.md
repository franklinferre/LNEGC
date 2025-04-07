# LNEGC - Linguagem Natural Estruturada para Geração de Código

## Visão Geral

LNEGC é uma linguagem controlada em português do Brasil projetada para descrever algoritmos, estruturas de dados e requisitos de software de forma estruturada, facilitando a geração automática de código por sistemas de IA.

## Estrutura do Projeto

```
lnegc/
├── componentes/     # Componentes reutilizáveis
├── entidades/       # Definições de entidades
├── interfaces/      # Definições de interfaces
├── testes/          # Especificações de testes
└── config.lnegc     # Configuração global do projeto
```

## Formato dos Arquivos LNEGC

Cada arquivo `.lnegc` segue um formato estruturado com:

1. **Cabeçalho**:
   ```
   # Nome do Componente/Entidade/Interface
   Versão: 1.0.0
   Autor: Nome do Autor
   Data: YYYY-MM-DD
   Domínio: Domínio do Componente
   Tags: tag1, tag2, tag3
   ```

2. **Seções**:
   - Cada seção começa com `## Nome da Seção`
   - O conteúdo é escrito em português do Brasil
   - Podem incluir exemplos, algoritmos, regras de negócio, etc.

## Exemplos

### Componente (validador_cpf.lnegc)
```
# Validador de CPF
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2023-10-15
Domínio: Validação
Tags: cpf, validação, brasileiro

## Descrição
Componente para validação de CPF brasileiro.

## Interface
- Entrada: String (CPF)
- Saída: Boolean (válido/inválido)
- Exceções: FormatoInvalidoException

## Algoritmo
1. Limpar entrada (remover pontuação)
2. Verificar comprimento (11 dígitos)
3. Verificar dígitos repetidos
4. Calcular dígitos verificadores
5. Comparar com dígitos informados
```

### Entidade (cliente.lnegc)
```
# Cliente
Versão: 1.0.0
Autor: Equipe LNEGC
Data: 2023-10-15
Domínio: CRM
Tags: cliente, pessoa, cadastro

## Atributos
- id: UUID (obrigatório, auto-gerado)
- nome: String (obrigatório, 3-100 caracteres)
- cpf: String (obrigatório, CPF válido)
- email: String (obrigatório, formato válido)
- telefone: String (opcional)
- status: Enum (ATIVO, INATIVO)

## Relacionamentos
- Pedidos: One-to-Many
- Categorias: Many-to-Many
```

## Processador LNEGC

O processador LNEGC é uma ferramenta Python que:

1. Lê arquivos `.lnegc`
2. Extrai metadados e seções
3. Gera um prompt estruturado para alimentar sistemas de IA
4. Suporta múltiplas linguagens de programação

### Uso

```bash
python lnegc_processor.py --dir lnegc --output prompt.txt --language python
```

### Opções

- `--dir`: Diretório base com arquivos LNEGC (padrão: 'lnegc')
- `--output`: Arquivo de saída para o prompt (padrão: 'prompt.txt')
- `--language`: Linguagem alvo para geração de código (padrão: 'python')

## Integração com IA

O prompt gerado pelo processador pode ser usado com:

1. OpenAI GPT-4
2. Claude
3. Outros modelos de linguagem avançados

O prompt inclui:
- Configuração do projeto
- Entidades e relacionamentos
- Interfaces e contratos
- Componentes e algoritmos
- Testes e cenários

## Contribuindo

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes. 