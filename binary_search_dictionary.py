def search_binary_search(dictionary, target_word):
    left = 0
    right = len(dictionary) - 1

    while left <= right:
        mid = (left + right) // 2
        if dictionary[mid][0] == target_word:
            return dictionary[mid][1]
        elif dictionary[mid][0] < target_word:
            left = mid + 1
        else:
            right = mid - 1

    return "Kata tidak ditemukan dalam kamus."

kamus = [
    ("Apple", "Buah Apel"),
    ("Banana", "Buah Pisang"),
    ("Cat", "Kucing"),
    ("Duck", "Bebek"),
    ("Elephant", "Gajah")
]

katadicari = input("Kata Yang Ingin Dicari ? : ")
definisi = search_binary_search(kamus, katadicari)
print(f"Definisi kata '{katadicari}': {definisi}")