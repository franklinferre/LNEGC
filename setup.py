#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Setup configuration for LNEGC package.
"""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="lnegc",
    version="1.0.0",
    author="Equipe LNEGC",
    author_email="equipe@lnegc.com.br",
    description="Linguagem Natural Estruturada para Geração de Código",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/lnegc",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: Portuguese (Brazilian)",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "lnegc=lnegc.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "lnegc": ["py.typed"],
    },
    zip_safe=False,
    project_urls={
        "Bug Reports": "https://github.com/seu-usuario/lnegc/issues",
        "Source": "https://github.com/seu-usuario/lnegc",
        "Documentation": "https://lnegc.readthedocs.io/",
    },
) 