def search_insert_position(data, target):
    left = 0
    right = len(data) - 1
    next_larger = None
    
    while left < right:
        mid = (left + right) // 2
        
        if data[mid] > target:
            next_larger = data[mid]
            right = mid - 1
        else:
            left = mid + 1
        return next_larger

data = [2, 4, 6, 8, 10, 12, 14]
target = 7

position = search_insert_position(data, target)

print(f"Elemen {target} dapat disisipkan pada indeks {position} untuk menjaga daftar tetap terurut.")