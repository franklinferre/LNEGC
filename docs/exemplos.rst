Exemplos
========

Nesta seção, apresentamos exemplos práticos de uso do LNEGC em diferentes cenários.

Validador de CPF
-------------

Este exemplo demonstra como criar um validador de CPF usando LNEGC:

.. code-block:: text

    # LNEGC v1.0
    # Autor: João Silva
    # Data: 2024-03-20
    # Descrição: Validador de CPF

    [COMPONENTE]
    Nome: ValidadorCPF
    Tipo: Utilitário
    Linguagem: Python
    Versão: 1.0.0

    [ALGORITMO]
    1. Receber o CPF como string
    2. Remover caracteres não numéricos
    3. Verificar se tem 11 dígitos
    4. Calcular primeiro dígito verificador
    5. Calcular segundo dígito verificador
    6. Comparar com os dígitos fornecidos
    7. Retornar resultado da validação

    [REGRAS]
    - CPF deve ter 11 dígitos
    - Todos os dígitos não podem ser iguais
    - Primeiro dígito verificador deve ser válido
    - Segundo dígito verificador deve ser válido

    [TESTES]
    - CPF válido: deve retornar True
    - CPF inválido: deve retornar False
    - CPF com formato inválido: deve lançar exceção
    - CPF com todos dígitos iguais: deve retornar False

O código Python gerado seria:

.. code-block:: python

    def validar_cpf(cpf: str) -> bool:
        # Remove caracteres não numéricos
        cpf = ''.join(filter(str.isdigit, cpf))
        
        # Verifica se tem 11 dígitos
        if len(cpf) != 11:
            raise ValueError("CPF deve ter 11 dígitos")
            
        # Verifica se todos os dígitos são iguais
        if len(set(cpf)) == 1:
            return False
            
        # Calcula primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10) % 11
        if digito1 == 10:
            digito1 = 0
            
        # Calcula segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10) % 11
        if digito2 == 10:
            digito2 = 0
            
        # Verifica os dígitos
        return cpf[-2:] == f"{digito1}{digito2}"

Sistema de Vendas
--------------

Este exemplo demonstra um sistema de vendas simples:

1. **Entidade Produto**:

   .. code-block:: text

       # LNEGC v1.0
       # Autor: Maria Santos
       # Data: 2024-03-20
       # Descrição: Entidade Produto

       [ENTIDADE]
       Nome: Produto
       Tipo: Domínio
       Linguagem: Python
       Versão: 1.0.0

       [ATRIBUTOS]
       - id: int (chave primária)
       - nome: str (obrigatório)
       - preco: decimal (obrigatório)
       - estoque: int (obrigatório)
       - ativo: bool (padrão: True)

       [REGRAS]
       - Nome deve ter entre 3 e 100 caracteres
       - Preço deve ser maior que zero
       - Estoque não pode ser negativo
       - Produto inativo não pode ser vendido

2. **Entidade Venda**:

   .. code-block:: text

       # LNEGC v1.0
       # Autor: Maria Santos
       # Data: 2024-03-20
       # Descrição: Entidade Venda

       [ENTIDADE]
       Nome: Venda
       Tipo: Domínio
       Linguagem: Python
       Versão: 1.0.0

       [ATRIBUTOS]
       - id: int (chave primária)
       - data: datetime (obrigatório)
       - cliente_id: int (obrigatório)
       - valor_total: decimal (obrigatório)
       - status: str (obrigatório)
       - itens: List[ItemVenda] (obrigatório)

       [REGRAS]
       - Data não pode ser futura
       - Valor total deve ser maior que zero
       - Status deve ser: 'pendente', 'aprovada', 'cancelada'
       - Deve ter pelo menos um item

3. **Serviço de Venda**:

   .. code-block:: text

       # LNEGC v1.0
       # Autor: Maria Santos
       # Data: 2024-03-20
       # Descrição: Serviço de Venda

       [SERVIÇO]
       Nome: VendaService
       Tipo: Aplicação
       Linguagem: Python
       Versão: 1.0.0

       [MÉTODOS]
       - criar_venda(cliente_id: int, itens: List[Dict]) -> Venda
       - aprovar_venda(venda_id: int) -> Venda
       - cancelar_venda(venda_id: int) -> Venda
       - calcular_total(itens: List[Dict]) -> decimal

       [REGRAS]
       - Verificar estoque antes de criar venda
       - Atualizar estoque após aprovar venda
       - Não permitir cancelar venda aprovada
       - Calcular desconto para compras acima de R$ 1000

API REST
-------

Este exemplo demonstra uma API REST usando LNEGC:

1. **Controlador de Cliente**:

   .. code-block:: text

       # LNEGC v1.0
       # Autor: Pedro Oliveira
       # Data: 2024-03-20
       # Descrição: Controlador de Cliente

       [CONTROLADOR]
       Nome: ClienteController
       Tipo: API
       Linguagem: Python
       Framework: FastAPI
       Versão: 1.0.0

       [ROTAS]
       - GET /clientes - Lista todos os clientes
       - GET /clientes/{id} - Obtém um cliente
       - POST /clientes - Cria um cliente
       - PUT /clientes/{id} - Atualiza um cliente
       - DELETE /clientes/{id} - Remove um cliente

       [REGRAS]
       - Usar autenticação JWT
       - Validar dados de entrada
       - Retornar códigos HTTP apropriados
       - Registrar todas as operações

2. **Modelo de Resposta**:

   .. code-block:: text

       # LNEGC v1.0
       # Autor: Pedro Oliveira
       # Data: 2024-03-20
       # Descrição: Modelo de Resposta

       [MODELO]
       Nome: RespostaAPI
       Tipo: DTO
       Linguagem: Python
       Framework: Pydantic
       Versão: 1.0.0

       [ATRIBUTOS]
       - sucesso: bool (obrigatório)
       - mensagem: str (opcional)
       - dados: Any (opcional)
       - erros: List[str] (opcional)

       [REGRAS]
       - Sucesso deve ser True para respostas 2xx
       - Mensagem deve ser informativa
       - Dados devem ser serializáveis
       - Erros devem ser claros e úteis

Testes de Integração
-----------------

Este exemplo demonstra testes de integração:

.. code-block:: text

    # LNEGC v1.0
    # Autor: Ana Costa
    # Data: 2024-03-20
    # Descrição: Testes de Integração

    [TESTES]
    Nome: VendaIntegrationTests
    Tipo: Integração
    Linguagem: Python
    Framework: pytest
    Versão: 1.0.0

    [CENÁRIOS]
    1. Criar venda com sucesso
       - Dado um cliente válido
       - E produtos em estoque
       - Quando criar uma venda
       - Então deve retornar venda criada
       - E atualizar estoque

    2. Falhar ao criar venda sem estoque
       - Dado um cliente válido
       - E produtos sem estoque
       - Quando tentar criar venda
       - Então deve lançar exceção
       - E não deve atualizar estoque

    3. Cancelar venda pendente
       - Dado uma venda pendente
       - Quando cancelar a venda
       - Então deve atualizar status
       - E não deve atualizar estoque

    [REGRAS]
    - Usar banco de dados de teste
    - Limpar dados entre testes
    - Verificar estado final
    - Validar todas as regras

Próximos Passos
-------------

1. Explore os exemplos fornecidos
2. Adapte para seu contexto
3. Crie seus próprios exemplos
4. Compartilhe com a comunidade 