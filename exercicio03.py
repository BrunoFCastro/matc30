import random
def activityNotifications(expenditure, d):
    notificacao = 0
    for i in range(len(expenditure)-d-1):
        mediana = expenditure[i:d]
        n = len(mediana)
        for i in range(1,n):
            insert_index = i
            current_value = mediana.pop(i)
            for j in range(i-1, -1, -1):
                if mediana[j] > current_value:
                    insert_index = j
            mediana.insert(insert_index, current_value)
        if d%2 == 0:
            if expenditure[i+d] > (mediana[n/2] + mediana [(n/2)-1]):
                notificacao = notificacao + 1
        else:
            if expenditure[i+d] > 2*(mediana[int(n/2)]):
                notificacao = notificacao + 1



    return notificacao

def gerar_dados(n, max_val=200):
    return [random.randint(0, max_val) for _ in range(n)]

def main():
    n, d = 10, 5
    gastos = gerar_dados(n)
    print(f"n = {n}, d = {d}")
    print("Gastos:", gastos)
    resultado = activityNotifications(gastos, d)
    print("Notificações:", resultado)

if __name__ == '__main__':
    main()