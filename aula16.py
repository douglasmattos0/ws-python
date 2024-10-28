"""
Script Name:    aula16.py
Author:         Douglas Ribas de Mattos
Date Created:   2024-10-28
Last Modified:  2024-10-28
Version:        1.0

Description:
    This script describe the initial concepst about Python programming.
    How to use 'if elif else' in Python

Usage:
    Run the script in a Python environment:
    `python aula16.py`

Requirements:
    - N/A

Change Log:
    - 2024-10-28 - Douglas Ribas de Mattos - Initial version

Notes:
    Ensure the input file is in the specified format and located in the same directory as this script.

"""
entrada = input('Você quer "entrar" ou "sair" ?')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')