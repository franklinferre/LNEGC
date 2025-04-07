#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Servidor web simples para servir o relatório de cobertura de testes.
"""

import http.server
import socketserver
import webbrowser
from pathlib import Path

# Configuração do servidor
PORT = 8777
HOST = "191.101.70.96"  # IP externo
DIRECTORY = Path("htmlcov")

class Handler(http.server.SimpleHTTPRequestHandler):
    """Handler personalizado para servir arquivos do diretório htmlcov."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

def main():
    """Função principal que inicia o servidor."""
    # Verifica se o diretório htmlcov existe
    if not DIRECTORY.exists():
        print(f"Erro: Diretório {DIRECTORY} não encontrado.")
        print("Execute os testes primeiro com: python -m pytest tests/ --cov")
        return 1

    # Configura o servidor
    with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
        print(f"Servindo relatório de cobertura em http://{HOST}:{PORT}")
        print("Pressione Ctrl+C para parar o servidor")
        
        # Abre o navegador automaticamente
        webbrowser.open(f"http://{HOST}:{PORT}")
        
        try:
            # Inicia o servidor
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor parado.")
            return 0

if __name__ == "__main__":
    exit(main()) 