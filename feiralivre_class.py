from feiralivre import Feiralivre

fruta_0 = Feiralivre("maça")
fruta_1 = Feiralivre("uva")
fruta_2 = Feiralivre("perá")
fruta_3 = Feiralivre("laranja")
fruta_4 = Feiralivre("mamão")
fruta_5 = Feiralivre("goiaba")
fruta_6 = Feiralivre("limão")
fruta_7 = Feiralivre("guarana")
fruta_8 = Feiralivre("amora")
fruta_9 = Feiralivre("banana")

print("============================"
      '''
      ''')
print("bem-Vindo! feira santos!"
      '''
      ''')
cliente = input("Digite seu nome para começarmos: ")
print(f"{cliente} temos 10 frutas que você pode gostar: "
      '''
      [0] maça
      [1] uva
      [2] perá
      [3] laranja
      [4] mamão
      [5] goiaba
      [6] limão
      [7] guarana
      [8] amora
      [9] banana
    ''')
seleção = int(input("Selecione o número da fruta esolhida: "))
lista_frutas = [fruta_0,fruta_1,fruta_2,fruta_3,fruta_4,fruta_5,fruta_6,fruta_7,fruta_8,fruta_9]
opção_selecionada = int(seleção)
for opção in lista_frutas:
    if opção_selecionada <= 10:
         print(f"{cliente} Obrigado por comprar {lista_frutas[opção_selecionada].frutas} . ")
         print("✨ VOLTE SEMPRE! ✨")
         break
    if opção_selecionada >= 11:
         print("Esta opção não esta incluida em nossa feira.")
         break