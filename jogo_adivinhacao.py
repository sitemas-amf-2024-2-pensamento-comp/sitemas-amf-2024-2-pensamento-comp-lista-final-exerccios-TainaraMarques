import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        palpite = int(input("Digite o seu palpite: "))

        if palpite < numero_secreto:
            print("O número secreto é maior. Tente novamente.")
        elif palpite > numero_secreto:
            print("O número secreto é menor. Tente novamente.")
        else:
            print("Parabéns! Você acertou o número secreto.")
            break  

jogo_adivinhacao()
