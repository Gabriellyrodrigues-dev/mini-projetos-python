import random
import string

def pedir_tamanho():
    while True:
        valor = input("Digite o tamanho da senha (mínimo 4): ").strip()
        try:
            tamanho = int(valor)
            if tamanho < 4:
                print("❌ O tamanho mínimo é 4.\n")
                continue
            return tamanho
        except ValueError:
            print("❌ Digite um número inteiro.\n")


def pedir_sim_nao(pergunta):
    while True:
        resp = input(pergunta + " (s/n): ").strip().lower()
        if resp in ("s", "n"):
            return resp == "s"
        print("❌ Responda com 's' ou 'n'.\n")


def gerar_senha(tamanho, usar_especiais):
    caracteres = string.ascii_letters + string.digits
    if usar_especiais:
        caracteres += string.punctuation

    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def main():
    print("=== Projeto 04 — Gerador de Senhas ===\n")

    tamanho = pedir_tamanho()
    usar_especiais = pedir_sim_nao("Incluir caracteres especiais?")

    senha = gerar_senha(tamanho, usar_especiais)
    print("\n✅ Senha gerada:")
    print(senha)

if __name__ == "__main__":
    main()
