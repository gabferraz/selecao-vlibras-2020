#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:31:43 2020

@author: gferraz
"""

import pandas as pd
import re
import json

def preenche_dicionario(dicionario, palavras):
    for palavra in palavras:
        if palavra in dicionario:
            dicionario[palavra] = dicionario[palavra] + 1
        else:
            dicionario[palavra] = 1
    

arquivo_texto = pd.read_csv("corpus-q2.csv")
json_dicionario = {}

for index, data in arquivo_texto.iterrows():
    preenche_dicionario(json_dicionario, re.split("\s", data.gr))
    preenche_dicionario(json_dicionario, re.split("\s", data.gi))

with open('corpus-resposta-q2.json', 'w', encoding='utf-8') as f:
    json.dump(json_dicionario, f, ensure_ascii=False, indent=4)
