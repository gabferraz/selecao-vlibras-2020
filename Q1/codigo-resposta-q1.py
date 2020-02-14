#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:51:38 2020

@author: gferraz
"""

import pandas as pd
import re

libras_textual = pd.read_csv("corpus-q1-v2.csv")
for index, data in libras_textual.iterrows():
    # Corrigindo caracteres invertidos
    char_invertido = re.findall(r'[SP][1-3]', data.gi)
    for match in char_invertido:
        data.gi = re.sub(r'[SP][1-3]', match[::-1], data.gi, 1)
           
    char_invertido = re.findall(r'[SP][1-3]', data.gr)
    for match in char_invertido:
        data.gr = re.sub(r'[SP][1-3]', match[::-1], data.gr, 1)            
         
    # Simplficando multiplos + entre parênteses
    data.gi = re.sub(r'\(\+{2,}\)', '(+)', data.gi)
    data.gr = re.sub(r'\(\+{2,}\)', '(+)', data.gr)
    
    # Simplificando multiplos espaços
    data.gi = re.sub(r'\s+', ' ', data.gi)
    data.gr = re.sub(r'\s+', ' ', data.gr)
    
    # Removendo hifen entre digitos
    hifen_entre_digitos = re.search(r'\d-+\d', data.gi)
    if hifen_entre_digitos:
        data.gi = re.sub(r'-', '', hifen_entre_digitos.string)
        
    hifen_entre_digitos = re.search(r'\d-+\d', data.gr)
    if hifen_entre_digitos:
        data.gr = re.sub(r'-', '', hifen_entre_digitos.string) 

    # Removendo espaço antes de qualificadores de local
    data.gi = re.sub(r'\s_CIDADE', '_CIDADE', data.gi)
    data.gi = re.sub(r'\s_ESTADO', '_ESTADO', data.gi)
    data.gi = re.sub(r'\s_PAIS', '_PAIS', data.gi)    
    
    data.gr = re.sub(r'\s_CIDADE', '_CIDADE', data.gr)
    data.gr = re.sub(r'\s_ESTADO', '_ESTADO', data.gr)
    data.gr = re.sub(r'\s_PAIS', '_PAIS', data.gr)
    
    # Removendo espaço antes de qualificador na direita
    espaco_qualificador_direita = re.search(r'\s_[1-3][SP]', data.gi)
    if espaco_qualificador_direita:
        pos = espaco_qualificador_direita.span()
        data.gi = data.gi[:pos[0]] + data.gi[pos[0]+1:]
        
    espaco_qualificador_direita = re.search(r'\s_[1-3][SP]', data.gr)
    if espaco_qualificador_direita:
        pos = espaco_qualificador_direita.span()
        data.gr = data.gr[:pos[0]] + data.gr[pos[0]+1:]  
        
    # Adicionando espaço depois de qualificador na esquerda
    espaco_qualificador_esquerda = re.search(r'[1-3][SP]_', data.gi)
    if espaco_qualificador_esquerda:
        pos = espaco_qualificador_esquerda.span()
        data.gi = data.gi[:pos[1]] + ' ' + data.gi[pos[1]:]    
        
    espaco_qualificador_esquerda = re.search(r'[1-3][SP]_', data.gr)
    if espaco_qualificador_esquerda:
        pos = espaco_qualificador_esquerda.span()
        data.gr = data.gr[:pos[1]] + ' ' + data.gr[pos[1]:]   

    # Remover espaço a esquerda de quantificador
    data.gi = re.sub(r'\s+\(\+\)', '(+)', data.gi)
    data.gi = re.sub(r'\s+\(\-\)', '(-)', data.gi)
    
    data.gr = re.sub(r'\s+\(\+\)', '(+)', data.gr)
    data.gr = re.sub(r'\s+\(\-\)', '(-)', data.gr)  
    
    # Substituir espaço na frente de NÃO por um hifen
    data.gi = re.sub(r'NÃO\s', 'NÃO_', data.gi)
    data.gr = re.sub(r'NÃO\s', 'NÃO_', data.gr)
    
    # Substituir sublinhado antes de FAMOSA/FAMOSO por &
    data.gi = re.sub('_FAMOSA', '&FAMOSA', data.gi)
    data.gi = re.sub('_FAMOSO', '&FAMOSO', data.gi)
    
    data.gr = re.sub('_FAMOSA', '&FAMOSA', data.gr)
    data.gr = re.sub('_FAMOSO', '&FAMOSO', data.gr)
    
    # Removendo ponto entre caracteres não numéricos
    ponto_n_numerico = re.findall(r'[^\d]\.[^\d]', data.gi)
    for match in ponto_n_numerico:
        data.gi = re.sub(match, match[:1] + match[2:], data.gi)
        
    ponto_n_numerico = re.findall(r'[^\d]\.[^\d]', data.gr)
    for match in ponto_n_numerico:
        data.gr = re.sub(match, match[:1] + match[2:], data.gr)

    # Adicionando zero implicito em números decimais 
    zero_implicito = re.findall(r'\s\.\d', data.gi)
    for match in zero_implicito:
        data.gi = re.sub(match, ' 0' + match[1:], data.gi)
        
    zero_implicito = re.findall(r'\s\.\d', data.gr)
    for match in zero_implicito:
        data.gr = re.sub(match, ' 0' + match[1:], data.gr)      
        
# Exportando a resposta para um arquivo csv
libras_textual.to_csv('corpus-resposta-q1.csv', index=False)