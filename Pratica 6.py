#explicação
"""#

frutas =  ['maçã','banana','laranja']
for fruta in frutas:
 print(fruta)

list = [1,2,3]
list.append(4)
print(list)

list = [1,2,3]
list.insert(1,"a")
print(list)

list = [1,2]
list.extend([3,4])
print(list)

list = [1,2,3,4]
list.remove(2)
print(list)

list = [10,20,30]
valor=list.pop(0)
print(list)

list = [1,2,3,4]
list.clear()
print(list)

list = ['a','b','c','b']
list.index('b')
print(list)

list.index('b', 2)
print(list)

list = [1,2,2,3]
list.count(2)
print(list)

list = [3,1,4,2]
list.sort()
print(list)

list = [3,1,4]
nova = sorted(list)
print(nova)

list = [1,2,3]
list,reversed()
print(list)

list = [1,2,3]
list.copy()
print(list)

soma=[1+2],[2+3]
print(soma)
 

"""#
 #Exercicio
list_compras=[]

Sair="sair"
lista_produtos= input("lista de produtos:")
while True:
 Produtos = (input("Digite o nome dos produtos: ("sair para parar"):",))
 if lista_produtos == (Sair):
  break
 print(lista_produtos)
