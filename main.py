import os
from random import randint
os.system('cls')

def pega_receita(nome_arquivo):
   receitas = []
   with open(f'{nome_arquivo}', 'r', encoding='utf-8') as file:
      next(file)
      for line in file:
         nome, pais, *resto = line.strip().split(',', maxsplit=2)
         
         if resto[0][0] == '"':
            resto[0] = resto[0][1:]  
         ingredientes, preparo = resto[0].split('","')
         preparo = preparo.strip('"')

         item = {
            'nome': nome,
            'pais': pais.strip(),
            'ingredientes': ingredientes.strip(),
            'preparo': preparo
         }
         receitas.append(item)
   
   return receitas
