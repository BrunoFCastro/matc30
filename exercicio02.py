import random

def insertionSort(arr):
    desloc = 0
    n = len(arr)
    for i in range(1,n):
        insert_index = i
        current_value = arr.pop(i)
        for j in range(i-1, -1, -1):
            if arr[j] > current_value:
                desloc = desloc + 1
                insert_index = j
        arr.insert(insert_index, current_value)
    return desloc

def generate_random_array(size, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]

def main():
    arr = generate_random_array(10)
    print("Array de entrada:", arr)
    result = insertionSort(arr)
    print("Deslocamentos realizados:", result)

if __name__ == '__main__':
    main()