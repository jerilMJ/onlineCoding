t = int(input())

strings = []

for _ in range(t):
    strings.append(input())
for string in strings:
    compressed = ''
    starting = True
    current_ch = ''
    current_ch_amount = 0
    for ch in string:
        if current_ch != ch and not starting:
            compressed = compressed + current_ch + str(current_ch_amount)
            current_ch = ch
            current_ch_amount = 1
        elif starting:
            current_ch = ch
            current_ch_amount = 1
            starting = False
        else:
            current_ch_amount += 1
    else:
        compressed = compressed + current_ch + str(current_ch_amount)
    print('YES' if len(compressed) < len(string) else 'NO')
