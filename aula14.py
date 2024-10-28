"""
Script Name:    aula14.py
Author:         Douglas Ribas de Mattos
Date Created:   2024-10-28
Last Modified:  2024-10-28
Version:        1.0

Description:
    This script describe the initial concepst about Python programming.
    How to use format in Python

Usage:
    Run the script in a Python environment:
    `python aula14.py`

Requirements:
    - N/A

Change Log:
    - 2024-10-28 - Douglas Ribas de Mattos - Initial version

Notes:
    Ensure the input file is in the specified format and located in the same directory as this script.

"""
a = 'A'
b = 'B'
c = 1.1
formato = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'.format(nome1=a, nome2=b, nome3=c)

print(formato)
