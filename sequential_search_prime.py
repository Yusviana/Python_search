def sequential_search_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def search_prime_numbers(numbers):
    bilangan_primer = []
    for num in numbers:
        if sequential_search_prime(num):
            bilangan_primer.append(num)
    return bilangan_primer

numbers = [7, 10, 13, 6, 17, 22, 19]

bilangan_primer = search_prime_numbers(numbers)

print("Bilangan prima yang ditemukan:", bilangan_primer)
