'''Solution to 'Set Mutations' under Python in HackerRank '''

n = int(input())
main_set = set(input().split())
t = int(input())
commands = []
for i in range(t*2):
    commands.append(input())
    if i%2 != 0:
        if "int" in commands[i-1]:
            main_set.intersection_update(set(commands[i].split()))
        elif "sym" in commands[i-1]:
            main_set.symmetric_difference_update(set(commands[i].split()))
        elif "diff" in commands[i-1]:
            main_set.difference_update(set(commands[i].split()))
        else:
            main_set.update(set(commands[i].split()))
print(sum(map(int,main_set)))





