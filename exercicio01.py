import random

def resolver_labirinto(n, m, k, maze, tunnels):
    fim = 0
    sai = 0
    for i in range(n):
        linha = maze[i]
        for j in range(m):
            if linha[j] == '%' and not ((i-1 == '#' or i-1<0)and(j-1 == '#' or j-1<0)and(i+1 == '#' or i+1>n)and(j+1 == '#' or j+1<m)):
                sai = sai + 1
                fim = fim + 1
            if linha[j] == '*'and not ((i-1 == '#' or i-1<0)and(j-1 == '#' or j-1<0)and(i+1 == '#' or i+1>n)and(j+1 == '#' or j+1<m)):
                fim = fim + 1
    for i in range(k):
        tunel = tunnels[i]
        if  ((tunel[0]-1 == '#' or tunel[0]-1<0)and(tunel[1]-1 == '#' or tunel[1]-1<0)and(tunel[0]+1 == '#' or tunel[0]+1>n)and(tunel[1]+1 == '#' or tunel[1]+1<m)) ^  ((tunel[2]-1 == '#' or tunel[2]-1<0)and(tunel[3]-1 == '#' or tunel[3]-1<0)and(tunel[2]+1 == '#' or tunel[2]+1>n)and(tunel[3]+1 == '#' or tunel[3]+1<m)):
            fim = fim + 1
        elif maze[tunel[0]][tunel[1]] == '%' or maze[tunel[2]][tunel[3]] == '%':
            sai = sai + 1
            fim = fim + 1
        elif maze[tunel[0]][tunel[1]] == '*' or maze[tunel[2]][tunel[3]] == '*':
            fim = fim + 1
    return sai/fim

def gerar_labirinto(n, m):
    elementos = ['O'] * 5 + ['#', '*', '%']
    labirinto = [''.join(random.choice(elementos) for _ in
    range(m)) for _ in range(n)]
    i, j = random.randint(0, n-1), random.randint(0, m-1)
    linha = list(labirinto[i])
    linha[j] = 'A'
    labirinto[i] = ''.join(linha)
    return labirinto

def gerar_tuneis(k, n, m):
    tuneis = set()
    while len(tuneis) < k:
        i1, j1 = random.randint(0, n-1), random.randint(0, m-1)
        i2, j2 = random.randint(0, n-1), random.randint(0, m-1)
        if (i1 != i2 or j1 != j2):
            tuneis.add((i1, j1, i2, j2))
    return list(tuneis)

def main():
    n, m, k = 5, 6, 2
    maze = gerar_labirinto(n, m)
    tunnels = gerar_tuneis(k, n, m)

    print("Maze:")
    for linha in maze:
        print(linha)
    print("Tunnels:", tunnels)

    resultado = resolver_labirinto(n, m, k, maze, tunnels)
    print("Probabilidade de fuga:", resultado)

if __name__ == '__main__':
    main()