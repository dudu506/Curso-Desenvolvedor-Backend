#funções

def saudação(nome):
 print(f"Olá,{nome}!")
saudação("eduardo")

def soma (a,b):
 return a + b
resultado = soma (3,5)
print(resultado)

def soma_todos(*numeros):
 return sum(numeros)
print(soma_todos(1,2,3))

def soma(a,b):
 """retorna a soma dos dois numeros."""
 return a + b

#funções
#Função para calcular o imc

def calcular_imc (peso, altura):
 imc = peso / (altura ** 2)
 return imc
#função para classificar o imc
def classificar_IMC(imc):
 
  if imc <18.5:
     return "Abaixo do peso"
  elif imc < 25:
    return "peso normal"
  elif imc < 30:
    return "sobrepeso"
  elif imc <40:
    return "obesidade"
  else:
    return "obesidade grave"
## PROGRAMA PRINCIPAL ##
#Entrada de dados do usuário
def main():
  peso = float(input("Digite sua Massa(kg): ")) 
  altura =float(input("Digite sua altura(m): "))

  imc = calcular_imc(peso, altura)
  classificação = classificar_IMC(imc)
  print(f"\nSeu IMC é: {imc:.2f}")
  print(f"Classificação: {classificação}")
main()