#CLASSES

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

#classe de conta bancaria

class ContaBancaria:
 def __init__(self,titular):
        self.titular = titular
        self.saldo = 0

 def depositar_valor(self,valor):
        self.saldo += valor
        print(f"\nVoçê acabou de depositar {valor:.2f} realizado com sucesso.")

 def sacar_valor(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("\nVoçê acabou de sacar  {valor:.2f} da sua conta!")
        else:
            print("\nVoçê não tem saldo suficiente")
 def mostrar_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")

conta = ContaBancaria("Eduardo")
conta.depositar_valor(500)
conta.sacar_valor(200)
conta.sacar_valor(400)
conta.mostrar_saldo()

#exercicio
vendedor = "josé"
vendas = 800
meta = 500

class Vendedor:
    def __init__(self,nome,vendas,meta):
        self.nome = nome
        self.vendas = vendas
        self.meta = meta
    def bateu_meta(self):
      return self.vendas >= self.meta
vendedor1 = Vendedor(vendedor, vendas , meta)
if vendedor1.bateu_meta():
 print(f"{vendedor1.nome} bateu a meta")
else:
   print(f"{vendedor1.nome} não bateu a meta")