import os
from random import randint
os.system('cls')

def pega_receita(nome_arquivo):
   receitas = []
   try:
      with open(f'{nome_arquivo}', 'r', encoding='utf-8') as file:
         next(file)
         for line in file:
               try:
                  nome, pais, *resto = line.strip().split(',', maxsplit=2)
                  
                  if resto[0][0] == '"':
                     resto[0] = resto[0][1:]  # Remove a primeira aspas duplas
                  ingredientes, preparo = resto[0].split('","')
                  preparo = preparo.strip('"')

                  item = {
                     'nome': nome,
                     'pais': pais.strip(),
                     'ingredientes': ingredientes.strip(),
                     'preparo': preparo
                  }
                  receitas.append(item)
               except ValueError as erro:
                  print(f"Erro: {erro}.")
               except Exception as erro:
                  print(f"Erro: {erro}.")
   except FileNotFoundError:
      print(f"Arquivo '{nome_arquivo}' não encontrado.")
   except Exception as e:
      print(f"Erro inesperado ao abrir o arquivo '{nome_arquivo}'.")
   
   return receitas


receitas = pega_receita('receitas.csv')


def adicionar():
   try:
      with open('receitas.csv', 'a') as file:
         novo_elemento = {}
         tipos = ['o nome da receita','o país de origem','os ingredientes','o modo de preparo']

         for i in range(len(tipos)):
               try:
                  a = input(f'Digite {tipos[i]}: ')

                  if i == 0:
                     novo_elemento['nome'] = a
                  elif i == 1:
                     novo_elemento['pais'] = a
                  elif i == 2:
                     novo_elemento['ingredientes'] = a
                  elif i == 3:
                     novo_elemento['preparo'] = a

                  if i > 2:
                     if ' ' in a:
                           file.write(f'"{a}"' + '\n')
                     else:
                           file.write(a + '\n')
                  else:
                     if ' ' in a:
                           file.write(f'"{a}"' + ',')
                     else:
                           file.write(a + ',')
               except Exception as e:
                  print(f"Erro: {e}.")
   except FileNotFoundError:
      print("Arquivo não encontrado.")
   except Exception as e:
      print(f"Erro: {e}.")


def visualizar_elemento():
   try:
      nome = input('Digite o nome da receita que você deseja visualizar no cardápio: ').lower().strip()

      cont = 0
      for receita in receitas:
         try:
               if receita['nome'].lower() == nome:
                  for key, value in receita.items():
                     print(f'{key}: {value}\n')
                     cont += 1
         except Exception as e:
               print(f"Erro ao visualizar a receita. Mensagem: {e}")
      if cont == 0:
         print('O nome dessa receita não foi cadastrado')
   except Exception as e:
      print(f"Erro inesperado ao visualizar a receita. Mensagem: {e}")


def filtra_por_pais():
   try:
      nacionalidade = str(input('Digite o país que você deseja filtrar: ')).strip().lower()

      cont = 0
      for receita in receitas:
         try:
               if receita['pais'].lower() == nacionalidade:
                  for key, value in receita.items():
                     print(f'{key}: {value}\n')
                     cont += 1
         except Exception as e:
               print(f"Erro ao filtrar por país. Mensagem: {e}")
      
      if cont == 0:
         print('País não encontrado')
   except Exception as e:
      print(f"Erro inesperado ao filtrar por país. Mensagem: {e}")


def atualizar_elemento():
   try:
      while True:
         receita_escolhida = input('Digite o nome da receita que você deseja atualizar: ').lower().strip()
         categoria = input('Digite a categoria da receita que você deseja atualizar: ').lower().strip()

         for receita in receitas:
               if receita['nome'].lower() == receita_escolhida:
                  if 'nome' in categoria:
                     sub = input(f'Qual nome você deseja atualizar na receita {receita_escolhida}: ').lower().strip()
                     receita['nome'] = sub
                     break

                  elif 'pais' in categoria:
                     sub = input(f'Digite o nome do novo país atualizado da receita {receita_escolhida}: ').lower().strip()
                     receita['pais'] = sub
                     break

                  elif 'ing' in categoria:
                     escolha = input('Você deseja adicionar ingredientes a categoria ou atualizar todos os ingredientes: [add] para adicionar e [att] para atualizar: ').lower().strip()

                     if 'add' in escolha:
                           add = input(f'Qual item você deseja adicionar na receita {receita_escolhida}: ').lower().strip()
                           receita['ingredientes'] += f',{add}'
                           break

                     elif 'att' in escolha:
                           att = input(f'Qual item você deseja atualizar nos ingredientes da receita {receita_escolhida}: ').lower().strip()
                           receita['ingredientes'] = att
                           break

                  elif 'preparo' in categoria:
                     sub = input(f'Qual nome você deseja atualizar na receita {receita_escolhida}: ').lower().strip()
                     receita['preparo'] = sub
                     break

         else:
               print("Categoria inválida. Por favor, escolha uma das opções válidas.")
               continue

         with open('receitas.csv', 'w', encoding='utf-8') as file:
               file.write('nome,pais,ingredientes,preparo\n')
               for rec in receitas:
                  file.write(f"{rec['nome']},{rec['pais']},{f'"{rec['ingredientes']}"'},{f'"{rec['preparo']}"'}\n")
         break

   except FileNotFoundError:
      print("Arquivo 'receitas.csv' não encontrado.")
   except Exception as e:
      print(f"Erro inesperado ao atualizar a receita. Mensagem: {e}")


def add_lista_fav():
   try:
      nome = input('Digite o nome da receita que você deseja adicionar como favorita: ').strip().lower()

      with open('receitas_favoritas.csv', 'r', encoding='utf-8') as file:
         favoritas = file.readlines()
         for fav in favoritas:
               if nome in fav.lower():
                  print('A receita já está cadastrada como favorita.')
                  return

      for receita in receitas:
         if receita['nome'].lower() == nome:
               with open('receitas_favoritas.csv', 'a', encoding='utf-8') as file:
                  file.write(f"{receita['nome']},{receita['pais']},{f'\"{receita['ingredientes']}\"'},{f'\"{receita['preparo']}\"'}\n")
               print('Receita adicionada aos favoritos com sucesso.')
               return

      print('A receita digitada não foi encontrada.')
   except FileNotFoundError:
      print("Arquivo não encontrado.")
   except Exception as e:
      print(f"Erro: {e}")


def visualizar_favoritos():
   try:      
      lista_fav = pega_receita('receitas_favoritas.csv')

      print('\nLista Receitas Favoritas\n\n')

      for receita in lista_fav:
         print(f"{receita['nome']} que seu pais original é {receita['pais']} os ingredientes necessarios para a sua realização seram {receita['ingredientes']} e o modo de preparo será feito dessa forma: {receita['preparo']}\n")

      return lista_fav
   
   except FileNotFoundError:
      print("Arquivo não encontrado.")
   except Exception as e:
      print(f"Erro: {e}")


def excluir_receita():
   try:
      nome = input("Digite o nome da receita que você deseja excluir: ").strip().lower()

      for receita in receitas:
         if receita['nome'].lower() == nome:
               receitas.remove(receita)
               print("Receita excluída com sucesso.")
               break
      else:
         print("A receita digitada não foi encontrada.")

      with open('receitas.csv', 'w', encoding='utf-8') as file:
         file.write('nome,pais,ingredientes,preparo\n')
         for receita in receitas:
               file.write(f"{receita['nome']},{receita['pais']},{f'\"{receita['ingredientes']}\"'},{f'\"{receita['preparo']}\"'}\n")
   except FileNotFoundError:
      print("Arquivo não encontrado.")
   except Exception as e:
      print(f"Erro: {e}")


def sugerir_receitas():
   try:
      n_aleatorio = randint(0, (len(receitas) - 1))
      receita_sugerida = receitas[n_aleatorio]

      print(f"Que tal experimentar a deliciosa {receita_sugerida['nome']}? Originária do {receita_sugerida['pais']}, os ingredientes necessários são {receita_sugerida['ingredientes']}, e seu modo de preparo é: {receita_sugerida['preparo']}\n")
      
   except IndexError:
      print("Não há receitas cadastradas para sugerir.")
   except Exception as e:
      print(f"Erro: {e}")


def sugerir_receitas_fav():
   try:         
      list_fav = pega_receita('receitas_favoritas.csv')
      n_aleatorio = randint(0, (len(list_fav) - 1))
      receita_sugerida = list_fav[n_aleatorio]

      print(f"Que tal experimentar a deliciosa {receita_sugerida['nome']}? Originária do {receita_sugerida['pais']}, os ingredientes necessários são {receita_sugerida['ingredientes']}, e seu modo de preparo é: {receita_sugerida['preparo']}\n")
         
   except FileNotFoundError:
      print("Arquivo não encontrado.")
   except IndexError:
      print("Não há receitas cadastradas para sugerir.")
   except Exception as e:
      print(f"Erro: {e}")


tam = 55

opcoes = {
   "1": "Adicionar Receita",
   "2": "Visualizar Receita",
   "3": "Filtrar Receita por País",
   "4": "Atualizar Receita",
   "5": "Excluir Receita",
   "6": "Salvar como Favorita",
   "7": "Visualizar Receitas Favoritas",
   "8": "Sugerir Receita Aleatória",
   "9": "Sugerir Receita Aleatória da lista de Favoritos",
   "999": "Sair"   
}

while True:
   print(f"+{'-'*tam}+")
   print(f"|{'MENU':^{tam}}")
   print(f"+{'-'*tam}+")
   for k, v in opcoes.items():
      print(f"|{f' {k} - {v}':{tam}}|")
   print(f"+{'-'*tam}+")

   op = input("Escolha uma opção: ")

   if op not in opcoes:
      print("Opção inválida")
      continue

   if op == "999":
      break
   else:
      print(f"\n{opcoes[op]}\n")

      if op == "1":
         adicionar()
      elif op == "2":
         visualizar_elemento()
      elif op == "3":
         filtra_por_pais()
      elif op == "4":
         atualizar_elemento()
      elif op == "5":
         excluir_receita()
      elif op == "6":
         add_lista_fav()
      elif op == "7":
         visualizar_favoritos()
      elif op == "8":
         sugerir_receitas()
      elif op == "9":
          sugerir_receitas_fav()
