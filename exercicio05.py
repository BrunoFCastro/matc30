import random
def similar_pair(n, k, edges):
    # IMPLEMENTAR AQUI
    sort = True
    array = edges
    resultado = 0
    while (sort):
        sort = False
        for i in range(n-1):
            for j in range(i+1,n-1):
                if edges[i][1] == edges[j][0] and (edges[i][0],edges[j][1]) not in array:
                    array.append((edges[i][0],edges[j][1]))
                    sort = True
    print(array)
    for i in range(n):
        for j in range(i+1,len(array)):
            if edges[i][0] == array[j][0]:
                resultado += 1        
    return resultado

def generateTestCases():
    return [
        (5, 2, [(3, 2), (3, 1), (1, 4), (1, 5)]),
        (6, 3, [(1, 2), (1, 3), (2, 4), (3, 5), (3, 6)]),
        (4, 1, [(1, 2), (2, 3), (3, 4)]),
        (7, 4, [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7)]),
        (3, 0, [(1, 2), (2, 3)])
    ]
def main():
    testCases = generateTestCases()
    for idx, (n, k, edges) in enumerate(testCases, 1):
        print(f"🧪 Teste {idx}")
        print(f"n = {n}, k = {k}, edges = {edges}")
        result = similar_pair(n, k, edges)
        print(f"➡️ Resultado: {result}\n")

if __name__ == "__main__":
    main()