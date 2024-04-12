def find_pairs(sequence):
    if len(sequence) > 2000 or len(sequence) < 2:
        return "Chyba: vstupní posloupnost je prázdná nebo příliš dlouhá"
    try:
        sequence = [int(num) for num in sequence]
    except ValueError:
        return "Chyba: hodnota na vstupu není platné celé číslo"
    sums = {}
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            interval_sum = sum(sequence[i:j+1])
            if interval_sum not in sums:
                sums[interval_sum] = 1
            else:
                sums[interval_sum] += 1
    pairs = sum([val*(val-1)//2 for val in sums.values() if val > 1])
    return pairs

sequence = input("Zadejte posloupnost čísel oddělených mezerou: ").split()
print(find_pairs(sequence))
