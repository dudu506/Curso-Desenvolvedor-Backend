    
class usuario:
      def __init__(self,nome,email,senha):
       self.nome = nome
       self.email = email
       self.senha = senha

      def exibir_dados(self):
         print(f"Digite o nome e o email do usuario: {self.nome}: {self.email}")
           
      def alterar_senha(self,nova_senha):
            self.senha = nova_senha
            print(f"Sua senha foi alterada com sucesso")
 
      def autenticar(self,email,senha):
          return self.email == email and self.senha == senha
      
      def __str__(self):
          return f"usuario: {self.nome}-{self.senha}"

p1= usuario("Eduardo", "ed555203@email.com","1234")
p2 = usuario("Ana Beatriz","AnaBeatriz@email.com","1234")
print("dados do usuario")

p1.exibir_dados()
p2.exibir_dados()

print("\n 🔹 Alterada senha de Eduardo")
print("\n 🔹 testando autenticação")
print(p1.autenticar("ed555203@email.com","1234")) #true
print(p2.autenticar("AnaBeatriz@email.com","1244"))   #false
print("\n usando __str__: ")
print(p1)
print(p2)
