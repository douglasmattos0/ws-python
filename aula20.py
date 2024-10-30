"""
Script Name:    aula20.py
Author:         Douglas Ribas de Mattos
Date Created:   2024-10-30
Last Modified:  2024-10-30
Version:        1.0

Description:
    This script describe the initial concepst about Python programming.
    Exercise

Usage:
    Run the script in a Python environment:
    `python aula20.py`

Requirements:
    - N/A

Change Log:
    - 2024-10-30 - Douglas Ribas de Mattos - Initial version

Notes:
    Ensure the input file is in the specified format and located in the same directory as this script.

"""
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor=} é maior ou igual ao {segundo_valor=}')
else:
    print(f'{segundo_valor=} é maior do que {primeiro_valor=}')
