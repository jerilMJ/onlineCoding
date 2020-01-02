def compress(compressed_string, starter_num, check_list):
    if len(checklist) > 2:
        compressed_string = compressed_string + str(starter_num) + '...' + str(check_list[-1]) + ','
    elif len(checklist) == 2:
        compressed_string = compressed_string + str(starter_num) + ',' + str(check_list[-1]) + ','
    else:
        compressed_string = compressed_string + str(starter_num) + ','
    return compressed_string


t = int(input())

for _ in range(t):
    compressed = ''
    n = int(input())
    number_list = list(map(int, input().split()))
    starter = number_list[0]
    checklist = [starter]
    for num in number_list[1:]:
        if checklist == list(range(starter, num)):
            checklist.append(num)
        else:
            compressed = compress(compressed, starter, checklist)
            starter = num
            checklist = [starter]
    else:
        compressed = compress(compressed, starter, checklist)

    print(compressed.rstrip(','))


