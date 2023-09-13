import random

def boas_vindas():
    print("--------------------------")
    print("Jogo da Forca selecionado com sucesso!")

def sortear_palavra():
    arquivo = open("palavras.txt", "r")

    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    return palavras[numero].upper()

def verificar_chute(palavra, chute, letras_acertadas):
    index = 1

    for letra in palavra:
        if (chute == letra):
            print(f'A palavra secreta possui a letra "{chute}" na posição {index}')
            letras_acertadas[index-1] = chute

        index += 1

def mensagem_gameover(acertou, enforcou, palavra):
    if (acertou):
        print(f'Parabéns! Você descobriu a palavra secreta: "{palavra}"')
        print("       ___________      ")
        print("     '._===__==_=_.'    ")
        print("     .-\\:        /-.    ")
        print("    | (|:.       |) |   ")
        print("     '-|:.       |-'    ")
        print("        \\::.    /       ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    elif (enforcou):
        print(f'Que pena!! Você não conseguiu descobrir a palavra secreta "{palavra}"')

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \\     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \\|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      / \\   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
    boas_vindas()

    palavra_secreta = sortear_palavra()
    letras_acertadas = ["_" for letra in palavra_secreta]

    tentativas = 0
    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        
        print(f'A palavra: {"".join(letras_acertadas)} possui {len(letras_acertadas)} letras')
        chute = input("Escolha uma letra: ").strip().upper()
        
        if (chute in palavra_secreta):
            verificar_chute(palavra_secreta, chute, letras_acertadas)
        else:
            print(f'Que pena, você errou! A palavra secreta não possui a letra "{chute}"')
            tentativas += 1
            desenha_forca(tentativas)

        acertou = "_" not in letras_acertadas
        enforcou = tentativas == 7

    mensagem_gameover(acertou, enforcou, palavra_secreta)

if (__name__ == "__main__"):
    jogar()