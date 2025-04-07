"""Core do LNEGC.

Este módulo contém a lógica principal do LNEGC, incluindo:
- Parser da linguagem
- Processador de código
- Sistema de plugins
- Validação
- Métricas
"""

from .parser import Parser  # noqa
from .processor import Processor  # noqa
from .validation import Validator  # noqa
from .metrics import MetricsCollector  # noqa
from .plugins import PluginManager  # noqa

__all__ = [
    "Parser",
    "Processor",
    "Validator",
    "MetricsCollector",
    "PluginManager",
] 