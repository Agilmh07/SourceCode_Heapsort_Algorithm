def heapify(arr, indeks, ukuran):
    terbesar = indeks
    anak_kiri = 2 * indeks
    anak_kanan = 2 * indeks + 1

    if anak_kiri < ukuran and arr[anak_kiri] > arr[terbesar]:
        terbesar = anak_kiri

    if anak_kanan < ukuran and arr[anak_kanan] > arr[terbesar]:
        terbesar = anak_kanan

    if terbesar != indeks:
        arr[indeks], arr[terbesar] = arr[terbesar], arr[indeks]
        heapify(arr, terbesar, ukuran)

def heapsort(arr):
    ukuran = len(arr)

    for i in range(ukuran // 2 - 1, -1, -1):
        heapify(arr, i, ukuran)

    for i in range(ukuran - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  
        heapify(arr, 0, i) 

if __name__ == "__main__":
    array_awal = [9, 6, 8, 2, 5, 7]
    print("Array sebelum diurutkan:", array_awal)

    heapsort(array_awal)
    print("Array setelah diurutkan:", array_awal)
