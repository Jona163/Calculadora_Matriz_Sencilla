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

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)

def val(tp):
    while tp!="N" and tp!="M":
        tp=input("Introduzca \'N\' para dato numérico y \'M\' para matriz: ")
    return tp

#FUNCIÓN DE TIPO DE DATO
def dato():
    tipo_dato=val(input("Tipo de dato: "))
    if tipo_dato=="M":
        matr=crea_matriz(fil,col)
    else:
        matr=OK(input("Introduce número: "))
    return matr

#FUNCIÓN PARA DEFINIR MATRIZ
def crea_matriz(fil,col):
    f=-1;c=-1
    e_fil=[]
    for f in range(fil):
        e_col=[]
        f+=1
        for c in range(col):
            c+=1
            valor=OK(input('Introduzca el componente (%d,%d): '%(f,c)))
            e_col.append(valor)
        e_fil.append(e_col)
        matri=np.array(e_fil,float)
    return matri
