import random
def countRecognizedStrings(R, L):
    # 🧠 Implemente aqui sua lógica
    # Deve retornar um inteiro com a quantidade de strings reconhecidas de tamanho L
    return 0

def gerar_expressao():
    # Simples gerador de expressões balanceadas
    bases = ["a", "b"]
    exp = random.choice(bases)
    for _ in range(random.randint(1, 3)):
        op = random.choice(["|", "", "*"])
        if op == "":
            exp = f"({exp}{random.choice(bases)})"
        elif op == "|":
            exp = f"({exp}|{random.choice(bases)})"
        elif op == "*":
            exp = f"({exp}*)"
    return exp

def main():
    T = 3
    casos = []
    for _ in range(T):
        R = gerar_expressao()
        L = random.randint(1, 6)
        casos.append((R, L))
    for R, L in casos:
        print(f"Expressão: {R}, Tamanho: {L}")
        resultado = countRecognizedStrings(R, L)
        print("Reconhecidas:", resultado)

if __name__ == '__main__':
    main()