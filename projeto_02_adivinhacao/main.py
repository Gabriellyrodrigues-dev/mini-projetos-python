import random

print("🎯 Jogo de Adivinhação")
print("Estou pensando em um número entre 1 e 10.")

numero_secreto = random.randint(1, 10)
tentativas = 0

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("📉 Muito baixo. Tente novamente.")
    else:
        print("📈 Muito alto. Tente novamente.")
