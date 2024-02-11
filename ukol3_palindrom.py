def nextPalindrome(from_num, radix, next):
    if radix < 2 or radix > 36:
        return 0
    
    def is_palindrome(n, base):
        num_str = ''
        while n > 0:
            num_str += str(n % base)
            n //= base
        return num_str == num_str[::-1]
    
    while True:
        from_num += 1
        if is_palindrome(from_num, radix):
            next[0] = from_num
            return 1

from_num = int(input("Zadejte počáteční číslo: "))
radix = int(input("Zadejte číselnou soustavu (2 až 36): "))

if radix < 2 or radix > 36:
    print("Neplatná číselná soustava.")
else:
    next_palindrome_num = [0]

    if nextPalindrome(from_num, radix, next_palindrome_num):
        print("Nejbližší větší palindrom než", from_num, "je", next_palindrome_num[0])
    else:
        print("Nelze nalézt nejbližší větší palindrom.")
