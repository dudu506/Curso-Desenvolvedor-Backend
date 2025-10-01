#Herança

#1
class ContaBancaria:
    def __init__(self,titular,saldo):
        self.__titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    def depositar(self, valor):
        self.__saldo += valor

conta = ContaBancaria("Ana",1000)
print(conta.get_saldo())
conta.depositar(500)
print(conta.get_saldo())

#2
class animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("som generico...")

class Cachorro(animal):
    def emitir_som(self):
        print("Au Au!")
              
class gato(animal):
    def emitir_som(self):
        print("miau!")

dog = Cachorro("rex")
cat = gato("Mimi")
dog.emitir_som()
cat.emitir_som()

#3
# class Funcionario:
    def __init__(self, nome, salario):
     self.nome = nome
     self._salario = salario
    
    def get_salario(self):
     return self.nome and self._salario

    def set_salario(self, novo_salario):
      if novo_salario >0:
       self.Salario = novo_salario
      else:
       print("salario invalido!")

  
    def mostrar_dados (self):
      print(f"nome:{self.nome} Salario: R${self._salario:.2f}")

      
class  Gerente(Funcionario):
    def __init__ (self, nome, salario, departamento):
      Funcionario.__init__(self,nome,salario)
      self.departamento = departamento

    def mostrar_departamento(self):
       print(f"O gerente {self.nome} é responsavel pelo departamento de {self.departamento}.")
    
f1 = Funcionario("Ana", 1500)
f1.mostrar_dados()
f1.set_salario(2500)
print("novo salario:", f1.get_salario())

g1 = Gerente("Eduardo", 5000, "vendas")
g1.mostrar_dados()
g1.mostrar_departamento()

#4
class Produto:
    def __init__(self,nome,preço):
        self.__nome = nome
        self.__preço = preço
    
    def get_preço(self):
       return self.__preço
    
    def descontos(self):
        self.__preço *=0.9
          

produtoa = Produto("Celular", 5000)
produtob = Produto("Notebook", 7000)


print("Sem desconto:" ,produtoa.get_preço())
produtoa.descontos()
print("Com desconto:" ,produtoa.get_preço())

print("Sem desconto:"  ,produtob.get_preço())
produtob.descontos()
print("Com desconto:"  ,produtob.get_preço())

#5
class Funcionario:
    def trabalhar(self):
        print("O funcionario esta trabalhando normalmento.")
class Estagiario(Funcionario):
    def trabalhar(self):
        print("O estagiario esta aprendendo enquanto trabalha.")

f1 = Funcionario()
e1 = Estagiario()

f1.trabalhar()
e1.trabalhar()

#6
class ContaCorrente:
    def __init__(self,titular):
     self._titular = titular
     self._saldo = 100

    def depositar(self, valor):
     self._saldo += valor
     print(f"Você depositou R${valor:.2f}.")

    def sacar_dinheiro(self, valor):
       if valor <= self._saldo:
           self._saldo -= valor
           print(f"Você acabou de sacar R${valor:.2f}.")
       else:
        print("Saldo insuficiente para realizar o saque")
        
    def mostrar_saldo(self):
        print(f"Saldo atual de {self._titular}: R${self._saldo:.2f}")

conta = ContaCorrente("Eduardo")
conta.depositar(500)
conta.sacar_dinheiro(400)
conta.sacar_dinheiro(200)
conta.mostrar_saldo()

#7
class Aluno:
    def __init__(self, nome, nota):
        self._nome = nome
        self._nota = nota

    def mostrar_nota(self):
        print(f"{self._nome}, a nota que você tirou foi {self._nota}")

    def apenas(self):
        if self._nota > 0 and self._nota <= 10:
            print("sua nota foi aceita")
        else:
            print("sua nota é inexistente")

al1 = Aluno("eduardo",10)
al2 = Aluno("Raissa",1)
al3 = Aluno("junio",-1)

al1.mostrar_nota()
al1.apenas()
al2.mostrar_nota()
al2.apenas()
al3.mostrar_nota()
al3.apenas()

#8
class pessoa:
    def __init__(self,nome, idade):
        self._nome = nome
        self._idade = idade

class teacher(pessoa):
    def materia(self):

        super(pai)
class pai:
    def __init__(self):

#9
class veiculo:
    def mover(self):
       print("O veiculo esta se movendo...")

class carro(veiculo):
    def mover(self):
        print(" O carro esta dirigindo pela estrada")

class bicicleta(veiculo):
    def mover(self):
        print("A bicicleta esta pedalando pela ciclovia.")

v1 = carro()
v2 = bicicleta()

v1.mover()
v2.mover()


#10
class usuario:
    def __init__(self, senha):
        self.__senha = senha

    def login(self, senha):
        if senha == self.__senha:
            print("O login realizado com sucesso!")
        else:
            print("senha incorreta!")
    def alterar_senha(self, antiga, nova):
        if antiga == self.__senha:
            self.__senha = nova
            print("senha alterda com sucesso")
        else:
            print("senha antiga incorreta")
u1 = usuario("1234")
u1.login("1234")
u1.alterar_senha("1234", "abcd")
u1.login("abcd")

#11
class animal:
    def respirar(self):
        print("O animal esta respirando.")
class mamifero(animal):
    def amamentar(self):
        print("O mamifera esta amamentando.")
class cachorro(mamifero):
    def latir(self):
        print("O cachorro esta latindo: au au !")        
dog = cachorro()
dog.respirar()
dog.amamentar()
dog.latir()