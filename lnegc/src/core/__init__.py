"""Core do LNEGC.

Este módulo contém a lógica principal do LNEGC, incluindo:
- Parser da linguagem
- Processador de código
"""

from .parser import LNEGCParser  # noqa
from .processor import LNEGCProcessor  # noqa

__all__ = [
    "LNEGCParser",
    "LNEGCProcessor",
] 