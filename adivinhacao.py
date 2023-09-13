import random

def jogar():
    
    print("--------------------------")
    print("Jogo da Adivinhação selecionado com sucesso!")

    numero_secreto = random.randrange(1,101)
    i = 1

    while(i <= 5):
        print("Tentativa {} de 5".format(i))
        tentativa = int(input("Digite um número entre 1 e 100: "))

        if(tentativa < 1 or tentativa > 100):
            print("Você deve escolher um número de 1 a 100")
            continue

        if(numero_secreto == tentativa) :
            print("Você acertou")
            break
        else :
            if(tentativa > numero_secreto):
                print("O número escolhido é maior que o número secreto")
            elif(tentativa < numero_secreto):
                print("O número escolhido é menor que o número secreto")

        i = i + 1

if (__name__ == "__main__"):
    jogar()