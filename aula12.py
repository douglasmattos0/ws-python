"""
Script Name:    aula12.py
Author:         Douglas Ribas de Mattos
Date Created:   2024-10-27
Last Modified:  2024-10-27
Version:        1.0

Description:
    This script describe the initial concepst about Python programming.
    Exercise to calculate the IMC

Usage:
    Run the script in a Python environment:
    `python aula12.py`

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

print(nome, 'tem', altura , 'de altura,')
print('possui massa de', massa, 'e seu IMC é')
print(imc)