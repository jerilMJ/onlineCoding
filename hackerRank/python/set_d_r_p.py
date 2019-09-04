''' Solution to 'Set .discard(), .remove() & .pop()' under Python in HackerRank '''

n = int(input())
s = set(map(int, input().split()))
numOfCommands = int(input())
commands = []

skip = 0
for _ in range(numOfCommands):
    command = input().split()
    commands.extend(command)

for i in range(len(commands)):
    if skip == 1:
        skip = 0
        continue
    if commands[i].lower() == "pop":
        s.pop()
    elif commands[i].lower() == "remove":
        s.remove(int(commands[i+1]))
        skip = 1
    elif commands[i].lower() == "discard":
        s.discard(int(commands[i+1]))
        skip = 1

print(sum(s))


