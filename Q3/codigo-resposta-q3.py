#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:28:05 2020

@author: gferraz
"""

import pandas as pd
import re

arquivo_texto = pd.read_csv("corpus-q3.csv")

def gerar_flexoes_possiveis(lista_verbos, arquivo):
    # Parte do código que isola tudo que não for qualificador direcional
    for match in lista_verbos:
        tokens = re.split('\s', match)
        verbo = tokens[1][2:-2]
            
        # Loop que gera todas as flexões possíveis de pessoa e número
        for primeira_flexao in range(0,2):
            for segunda_flexao in range(0,2):
                for i in range(1,4):
                    for j in range(1,4):
                        if primeira_flexao % 2 == 0 and segunda_flexao % 2 == 0:    
                            line = tokens[0]+' '+str(i)+'S'+verbo+str(j)+'S '+tokens[2]+'\n'   
                        elif primeira_flexao % 2 == 0 and segunda_flexao % 2 == 1:
                            line = tokens[0]+' '+str(i)+'S'+verbo+str(j)+'P '+tokens[2]+'\n'  
                        elif primeira_flexao % 2 == 1 and segunda_flexao % 2 == 0:
                            line = tokens[0]+' '+str(i)+'P'+verbo+str(j)+'S '+tokens[2]+'\n' 
                        elif primeira_flexao % 2 == 1 and segunda_flexao % 2 == 1:
                            line = tokens[0]+' '+str(i)+'P'+verbo+str(j)+'P '+tokens[2]+'\n' 
                        arquivo.write(line) 
    
with open('corpus-resposta-q3.txt', 'w', encoding='utf-8') as f:
    for index, data in arquivo_texto.iterrows():
        # Retorna todos os casos com o verbo e as palavra anteriores e sucessores a ele
        lista_de_verbos = re.findall('\w+\s[1-3][SP]_\w+_[1-3][SP]\s[A-Z\[\]]+', data.gi)
        gerar_flexoes_possiveis(lista_de_verbos, f)
        
        lista_de_verbos = re.findall('\w+\s[1-3][SP]_\w+_[1-3][SP]\s[A-Z\[\]]+', data.gr)
        gerar_flexoes_possiveis(lista_de_verbos, f)
        