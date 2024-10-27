"""
Script Name:    aula13.py
Author:         Douglas Ribas de Mattos
Date Created:   2024-10-27
Last Modified:  2024-10-27
Version:        1.0

Description:
    This script describe the initial concepst about Python programming.
    How to use f-gtring in Python

Usage:
    Run the script in a Python environment:
    `python aula13.py`

Requirements:
    - N/A

Change Log:
    - 2024-10-27 - Douglas Ribas de Mattos - Initial version

Notes:
    Ensure the input file is in the specified format and located in the same directory as this script.

"""
nome = 'Joaquim Eusébio'
altura = 1.5
massa = 80.9
imc = massa / (altura ** 2)

linha_1 = f'{nome} tem {altura:.2f} (m) de altura,'
linha_2 = f'possui massa de {massa:.2f} (Kg) e seu IMC é {imc:.2f}'
print(linha_1)
print(linha_2)
