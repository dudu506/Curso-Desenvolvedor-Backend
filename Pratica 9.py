#CLASSES
"""#
class pessoa:
    def __init__(self,nome,idade):
     self.nome = nome
     self.idade = idade
     self.aniversario = self.idade +1
    def apresentar(self):
       print(f"Ola, Meu nome é {self.nome} e tenho {self.idade} anos.")
    def fazer_aniversario(self):
     self.idade +=1
     print(f"minnha idade daqui um ano é {self.idade}.")
p1 = pessoa("Eduardo", 16)
p1.apresentar()
p1.fazer_aniversario()
p2 = pessoa("junio", 16)
p2.apresentar()
p2.fazer_aniversario()
"""#
#classe de conta bancaria
class conta_Bancaria:
    def __init__(self,titular,saldo):
     self.titular = titular
     self.saldo = 0

    def depositar(self, valor):
     self.saldo += valor
    print(f"\nVocê depositou R${"valor:.2f"}.")
    def sacar_dinheiro(self, valor):
       if valor <= self.saldo:
        print(f"Você acabou de sacar R${valor:.2f}.")
       else:
        print("saldo insuficiente para realizar o saque")
def mostrar_saldo(self):
           print(f"saldo atual de {self.titular}: R${self.saldo:2f}")

conta = conta_Bancaria("marco")
conta.depositar(500)
conta.sacar(400)
conta.sacar(200)
conta.mostrar()