def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'George']

target_nama = input("Masukan nama yang ingin dicari : ")
index = binary_search(names, target_nama)

if index != -1:
    print("Nama yang ditemukan pada indeks", index)
else:
    print("Nama tidak ditemukan.")