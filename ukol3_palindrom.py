def nextPalindrome(from_num, radix, next):
    # Kontrola platnosti číselné soustavy
    if radix < 2 or radix > 36:
        return 0
    
    # Funkce pro kontrolu palindromu v dané soustavě
    def is_palindrome(n, base):
        num_str = ''
        while n > 0:
            num_str += str(n % base)
            n //= base
        return num_str == num_str[::-1]
    
    # Hledání nejbližšího většího palindromu
    while True:
        from_num += 1
        if is_palindrome(from_num, radix):
            next[0] = from_num
            return 1

# Získání vstupních hodnot od uživatele
from_num = int(input("Zadejte počáteční číslo: "))
radix = int(input("Zadejte číselnou soustavu (2 až 36): "))

# Kontrola platnosti vstupních hodnot
if radix < 2 or radix > 36:
    print("Neplatná číselná soustava.")
else:
    next_palindrome_num = [0]  # Pole pro uchování výsledku

    if nextPalindrome(from_num, radix, next_palindrome_num):
        print("Nejbližší větší palindrom než", from_num, "je", next_palindrome_num[0])
    else:
        print("Nelze nalézt nejbližší větší palindrom.")
