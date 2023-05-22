def is_similar(names1, names2):
    names1 = names1.lower()
    names2 = names2.lower()

    if names1[1] == names2[1]:
        return True
    
    return False

def sequential_search(names, book_phone):
    for names in phones:
        if is_similar(names['title'], book_phone):
            return names['shelf']
        
    return " Nomer tidak ditemukan"

phones = [
    {'title' : 'John Doe', 'shelf': '081234567890'},
    {'title' : 'Jane Smith', 'shelf': '089876543210'},
    {'title' : 'Michael Johnson', 'shelf': '087811223344'},
    {'title' : 'Emily Davis', 'shelf': '082122232425'}
]

book_phone = input("Masukan Nama yang ingin di cari : ")
shelf_location = sequential_search(phones, book_phone)
print(shelf_location)