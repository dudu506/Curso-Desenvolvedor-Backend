#1 fazer um cadastro de viagem(deve pedir o nome do 
# viajante, dar as opções de destino e imprimir a
# selecionada)-criar usando class

from Viagem_class import Viagem_class

viagem_0 = Viagem_class("Florida")
viagem_1 = Viagem_class("havai")
viagem_2 = Viagem_class("Toquio")
viagem_3 = Viagem_class("Egito")
viagem_4 = Viagem_class("Londres")

print("============================"
      '''
      ''')
print("bem-Vindo! senai Viagems tem algumas pfertas para você!"
      '''
      ''')
viajante = input("Digite seu nome para começarmos: ")

print(f"{viajante} temos 5 destinos que combinam com você: "
      '''
      [0] Flórida
      [1] Havai
      [2] Toquio
      [3] Egito
      [4] Londres
      
    ''')

seleção = int(input("Selecione o número da viagem desejada: "))
lista_viagem = [viagem_0,viagem_1,viagem_2,viagem_3,viagem_4]
opção_selecionada = int(seleção)
for opção in lista_viagem:
    if opção_selecionada >= 5:
        print("Esta opção não esta incluida em nossos destinos.")
        break
    if opção_selecionada <= 4:
        print(f"{viajante} sua viagem para {lista_viagem[opção_selecionada].destino} esta marcada. ")
        print("✨ VOLTE SEMPRE! ✨")
        break
