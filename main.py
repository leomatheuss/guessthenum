from random import randint
import os


gamecount = 0

def gameplay():
    tentativas = 5
    numero = randint(1, 100)
    error = False
    print("Você tem 5 tentativas para advinhar o número, se você errar, você ganha uma dica\nOs números estão no intervalo de [1,100]")
    print("Vamos lá:")

    while tentativas > 0:
        tentativa = int(input())
        if tentativa == numero:
            print("Parabéns, você acertou o número era",numero)
            error = False
            break
        else:
            error = True
        
            if tentativa > numero:
                print("Você deveria tentar um número menor")
                tentativas -= 1
                print("Você ainda possui {} tentativas".format(tentativas))
            elif tentativa < numero:
                print('Você deveria tentar um número maior')
                tentativas -= 1
                print("Você ainda possui {} tentativas".format(tentativas))
    
        if tentativas == 0 and error == True:
            os.system('clear')
            print("Você não conseguiu, o número era:",numero)

gameplay()
gamecount = 1

while True:

    count = input(("Quer jogar novamente? [S/N]: "))
    if count == 'n' or count == 'N':
        print("Você jogou um total de {} vezes".format(gamecount))
        break
    elif count =='S' or count =='s':
        gameplay()

        gamecount += 1
    