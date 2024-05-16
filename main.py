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


def atualizar_elemento():
    
    try:
        while True:
            receita_escolhida = input('Digite o nome da receita que você deseja atualizar: ').lower().strip()
            categoria = input('Digite a categoria da receita que você deseja atualizar [nome] [pais] [ingredientes] [preparo]: ').lower().strip()

            receita_encontrada = False
            for receita in receitas:
                if receita['nome'].lower() == receita_escolhida:
                    receita_encontrada = True
                    if categoria == 'nome':
                        substituido = input(f'Qual nome você deseja atualizar na receita {receita_escolhida}: ').strip()
                        receita['nome'] = substituido
                        break

                    elif categoria == 'pais':
                        substituido = input(f'Digite o nome do novo país atualizado da receita {receita_escolhida}: ').strip()
                        receita['pais'] = substituido
                        break

                    elif categoria == 'ingredientes':
                        escolha = input('Você deseja adicionar ingredientes à categoria ou atualizar todos os ingredientes: [add] para adicionar e [att] para atualizar: ').lower().strip()

                        if escolha == 'add':
                            add = input(f'Qual item você deseja adicionar na receita {receita_escolhida}: ').strip()
                            receita['ingredientes'] += f',{add}'
                            break

                        elif escolha == 'att':
                            att = input(f'Quais ingredientes você deseja atualizar na receita {receita_escolhida}: ').strip()
                            receita['ingredientes'] = att
                            break

                    elif categoria == 'preparo':
                        substituido = input(f'Qual o modo de preparo você deseja alterar na receita {receita_escolhida}: ').strip()
                        receita['preparo'] = substituido
                        break

                    else:
                        print("Categoria inválida. Por favor, escolha uma das opções válidas.")
                        continue

            if not receita_encontrada:
                print(f"Receita '{receita_escolhida}' não encontrada. Por favor, tente novamente.")
                continue

            with open('receitas.csv', 'w', encoding='utf-8') as file:
                file.write('nome,pais,ingredientes,preparo\n')
                for rec in receitas:
                    file.write(f"{rec['nome']},{rec['pais']},\"{rec['ingredientes']}\",\"{rec['preparo']}\"\n")
            break

    except FileNotFoundError:
        print("Arquivo 'receitas.csv' não encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao atualizar a receita. Mensagem: {e}")


