import forca
import adivinhacao

print("Seja Bem-Vindo!")
print("Escolha um jogo abaixo:")

jogo = int(input("1 - Forca\n2 - Adivinhação\n"))

if (jogo == 1):
    forca.jogar()
elif (jogo == 2):
    adivinhacao.jogar()

print("Fim de jogo")