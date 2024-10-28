"""
Script Name:    aula15.py
Author:         Douglas Ribas de Mattos
Date Created:   2024-10-28
Last Modified:  2024-10-28
Version:        1.0

Description:
    This script describe the initial concepst about Python programming.
    How to use input function in Python

Usage:
    Run the script in a Python environment:
    `python aula15.py`

Requirements:
    - N/A

Change Log:
    - 2024-10-28 - Douglas Ribas de Mattos - Initial version

Notes:
    Ensure the input file is in the specified format and located in the same directory as this script.

"""

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
