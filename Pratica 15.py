"""
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

class Funcionario:
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

"""
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