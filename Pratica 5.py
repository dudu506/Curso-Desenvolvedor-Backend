# exercicios - Estruturas de controle REPETIÇÃO

#1
Contador = 1
while Contador <= 10:
    print("número:", Contador)
    Contador +=1

#2
for i in range(2,21,2):
 print("número:",i)

 
 #3
numero1= int(input("número 1="))
numero2= int(input("número 2="))
numero3= int(input("número 3="))
numero4= int(input("número 4="))
numero5= int(input("número 5="))
Soma=(numero1 + numero2 + numero3 + numero4 + numero5)
print("Soma:",Soma)

 #4
for i in range(1,11):
    Soma=(i*7)
    print("tabuada:",(f"7x{i} = {7 * i}"))

#5
soma = 0
while True:
    número = float(input("Digite um número (0 para parar): "))
    if número == 0:
     break
    soma += número
print("A soma dos números é:",soma )

try:
   x = 5 / 1
except ZeroDivisionError:
   print("Divisão por zero não permitida")
else:
   print("Divisão Realizada com sucesso")
finally:
   print("Este bloco sempre será eecutado")
