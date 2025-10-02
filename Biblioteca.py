from biblioteca1 import Biblioteca

livro_0 = Biblioteca("Harry Potter")
Livro_1 = Biblioteca("Turma da monica")
livro_2 = Biblioteca("Diario de um banana")
livro_3 = Biblioteca("Metamorfose")
livro_4 = Biblioteca("Dom Quixote de La Mancha")
livro_5 = Biblioteca("O Sol é Para Todos")
livro_6 = Biblioteca("Ensaio Sobre a Cegueira")
livro_7 = Biblioteca("Crime e Castigo")
livro_8 = Biblioteca("O Senhor dos Anéis")
livro_9 = Biblioteca("O Pequeno Príncipe")

print("============================"
      '''
      ''')
print("bem-Vindo! Biblioteca Santos!"
      '''
      ''')
Leitor = input("Digite seu nome para começarmos: ")
print(f"{Leitor} temos 10 livros que combinam com você: "
      '''
      [0] Harry Potter
      [1] Turma da monica
      [2] Diario de um banana
      [3] Metamorfos
      [4] Dom Quixote de La Mancha
      [5] O Sol é Para Todos
      [6] Ensaio Sobre a Cegueira
      [7] Crime e Castigo
      [8] O Senhor dos Anéis
      [9] O Pequeno Príncipe
    ''')
seleção = int(input("Selecione o número do seu livro esolhido: "))
lista_livros = [livro_0,Livro_1,livro_2,livro_3,livro_4,livro_5,livro_6,livro_7,livro_8,livro_9]
opção_selecionada = int(seleção)
for opção in lista_livros:
    if opção_selecionada >= 10:
        print("Esta opção não esta incluida em nossa biblioteca.")
        break
    if opção_selecionada <= 9:
        print(f"{Leitor} o livro  {lista_livros[opção_selecionada].livros} esta tudo certo e você poderá ler em breve. ")
        print("✨ VOLTE SEMPRE! ✨")
        break