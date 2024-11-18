#importando rando para escolher palavra aleatória.
import random

#função para definir palavra aleatória. 
def escolherPalavra():
    palavras = ["python", "programação", "desenvolvimento", "computador", "algoritmo"]
    return random.choice(palavras)

def jogoDaForca():
    palavraSecreta = escolherPalavra()
    letrasDescobertas = ['_' for _ in palavraSecreta]
    tentativas = 6
    letrasErradas = []

    print("Bem vindo ao jogo da forca!")

    while tentativas > 0 and '_' in letrasDescobertas:
        print("\palavra: " + ''.join(letrasDescobertas))
        print(f"Tentativas restantes: {tentativas}")
        print("Letras erradas: " + ', '.join(letrasErradas))

        letra = input("Digite uma letra ").lower()

        if letra in palavraSecreta:
            for indice, caractere in enumerate(palavraSecreta):
                if caractere == letra:
                    letrasDescobertas[indice] = letra
        else:
             tentativas -= 1
             letrasErradas.append(letra)
             print(f"A letra {letra} não esta na palavra. ")

    if '_' not in letrasDescobertas:
            print(f"\\Parabéns! você adivinhou a palavra: {palavraSecreta}")
    else: 
            print(f"\\Você perdeu! A palavra era: {palavraSecreta}")

jogoDaForca()