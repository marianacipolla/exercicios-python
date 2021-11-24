# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:23:11 2021

@author: Mariana
"""

"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex: APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
"""

entrada = str(input('Digite a frase a ser analisada (sem acentos): ')).strip().lower()
frase = entrada.replace(' ', '') # retira os espaços da frase
tamanho = len(frase) 
c2 = tamanho - 1 # variável que vai percorre as letras de trás para frente
checagem = True # variável para checar se as letras são iguais
for c in range(0, len(frase) // 2): # o laço é iterado um número de vezes igual a metade do comprimento da frase (sem espaços)
    if frase[c] != frase[c2]: # se a letra da frente é diferente à de trás
        c = len(frase) // 2 # fará com que o laço pare de se repetir
        checagem = False # não é palíndromo
    c2 -= 1 
if checagem == True:
    print('A frase "{}" é um palíndromo!' .format(entrada))
else:
    print('A frase "{}" não é um palíndromo.' .format(entrada))
