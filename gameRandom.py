import random
import os

#VARIAVEIS
tentativa = 0
palpite = 0
a=1 #limite inicial
b=10 #limite final

#ESCOLHA DO NUM ALEATORIO
num = random.randint(a,b)

#JOGO
print('JOGO DE ADIVINHAÇÃO \n\n')
print(f'Tente adivinhar o número escolhido ({a} a {b})')
while 1:
    tentativa += 1
    print ('Tentativa ' + str(tentativa))
    palpite = int(input('Digite o seu palpite: '))

    if palpite > 10 or palpite < 1 :
        print ('palpite inválido')
        continue
    elif palpite > num :
        print ('palpite maior que o número')
    elif palpite < num :
        print ('palpite menor que o número')
    elif palpite == num :
        print ('parabens!!! você acertou')
        break
    
    input('Pressione para continuar...')
    os.system('cls')  # Limpa a tela a cada tentativa

print (f"Você acertou em {tentativa} tentativas")
input('Pressione enter para sair...')