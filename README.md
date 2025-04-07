# LNEGC - Linguagem Natural Estruturada para Geração de Código

[![Python Version](https://img.shields.io/pypi/pyversions/lnegc.svg)](https://pypi.org/project/lnegc/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Type Checking: mypy](https://img.shields.io/badge/type%20checking-mypy-blue)](http://mypy-lang.org/)
[![Tests](https://github.com/franklinferre/LNEGC/actions/workflows/ci.yml/badge.svg)](https://github.com/franklinferre/LNEGC/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/franklinferre/LNEGC/branch/main/graph/badge.svg)](https://codecov.io/gh/franklinferre/LNEGC)
[![Documentation Status](https://readthedocs.org/projects/lnegc/badge/?version=latest)](https://lnegc.readthedocs.io/pt/latest/?badge=latest)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)

## 🚀 Sobre

LNEGC é uma linguagem e ferramenta inovadora para gerar código a partir de descrições em linguagem natural estruturada. Ela permite que desenvolvedores e equipes criem código de forma mais eficiente, mantendo a documentação sempre atualizada e seguindo as melhores práticas de desenvolvimento.

## ✨ Características

- 🎯 Geração de código a partir de descrições em linguagem natural
- 📚 Documentação automática e sempre atualizada
- 🛠️ Suporte a múltiplas linguagens de programação
- 🔍 Validação e análise de código
- 🧪 Testes automatizados
- 🔄 Integração contínua
- 📊 Métricas e relatórios
- 🔌 Sistema de plugins extensível

## 🛠️ Tecnologias

- Python 3.10+
- TypeScript
- React
- Node.js
- Docker
- GitHub Actions
- OpenAI API
- PostgreSQL
- Redis

## 📦 Instalação

```bash
# Usando pip
pip install lnegc

# Usando npm
npm install -g lnegc

# Usando yarn
yarn global add lnegc
```

## 🚀 Uso Rápido

1. Crie um arquivo `validador_cpf.lnegc`:
```lnegc
@componente ValidadorCPF
@descricao Valida CPF usando algoritmo oficial
@interface
  @metodo validar(cpf: string): boolean
  @retorno true se CPF válido, false caso contrário
@exemplo
  const validador = new ValidadorCPF();
  const valido = validador.validar("123.456.789-00");
```

2. Gere o código:
```bash
lnegc generate validador_cpf.lnegc
```

3. Use o componente:
```typescript
import { ValidadorCPF } from './validador_cpf';

const validador = new ValidadorCPF();
const valido = validador.validar("123.456.789-00");
```

## 📚 Documentação

- [Guia de Instalação](docs/guias/instalacao.md)
- [Uso Básico](docs/guias/uso-basico.md)
- [Uso Avançado](docs/guias/uso-avancado.md)
- [API](docs/referencias/api.md)
- [Exemplos](docs/exemplos/)
- [Boas Práticas](docs/boas-praticas/)

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, leia nosso [guia de contribuição](CONTRIBUTING.md) para detalhes sobre nosso código de conduta e processo de submissão de pull requests.

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes. 