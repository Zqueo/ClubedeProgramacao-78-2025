print ('Hello World')

nota1 = input('Digite o primeiro número:')
nota2 = input('Digite o segundo número:')
nota3 = input('Digite o terceiro número:')
nota4 = input('Digite o querto número:')

nota1 = int(nota1)
nota2 = int(nota2)
nota3 = int(nota3)
nota4 = int(nota4)

res = (nota1 + nota2 + nota3 + nota4)/4

if res>=6 and res<=10: 
    print('Aluno Aprovado')
    print('Parabens!!')
elif res<6 and res>=0: 
    print('Aluno Reprovado')
    print('Estude mais')
else:
    print('Média Inválida')