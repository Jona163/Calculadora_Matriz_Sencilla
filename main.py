# Autor: Jonathan Hernández
# Fecha: 16 octubre 2024
# Descripción: Calculadora matrix Python.
# GitHub: https://github.com/Jona163
import numpy as np
import subprocess

def OKI(n):
    try:
        n=int(n)
    except:
        n=OKI(input("Caracter no valido: "))
    return n

def OK(n):
    try:
        n=float(n)
    except:
        n=OK(input("Caracter no valido: "))
    return n
