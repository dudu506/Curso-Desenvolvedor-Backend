#tuplas
minha_tuplas = (1,2,3)

tupla_com_um = (5)
não_tupla = (5)

x,y,z = (1,2,3)
print(x,y,z)

t = (1,2,2,2,3,5,4)
print(t.count(2)) # serve para contar quantas vezea o número se repete
print(t.index(3))  # sece para saber qual posicão vai estar o número
print(len(t))

#test
meu_conjunto= {1,"banana",3,14,1}
print(meu_conjunto)

numeros =[10,11,12,13,14,15,10]
conj = set(numeros)
print(conj)
vazio = set ()

a ={1,2,3}
b = {3,4,5}
uniao = a|b
print ("uniao:", uniao)
uniao = a.union(b)
print ("uniao:", uniao)

diferença = a-b
print("diferença:", diferença)

interseção = a&b
print("interseção:", interseção)

interseção = a.intersection(b)
print("interseção:", interseção)

c= {1,2,3}

c.add(2)
c.remove(2)
c.discard(2)
c.clear()

#exercicios

numeros =[1,2,2,3,4,4,5,1,]
conj = set(numeros)
print(conj)

numeros =[1,2,2,3,4,5,6]
conj = set(numeros)
print(conj)

lista1 =["Ana","Carlos","joão"]
lista2 =["maria","Carlos","Pedro"]

conj1 = set (lista1)
conj2 = set (lista2)

comum = conj1.intersection(conj2)

print(comum)