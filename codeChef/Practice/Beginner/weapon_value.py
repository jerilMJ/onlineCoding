t = int(input())

for _ in range(t):
    n = int(input())
    weapons = []
    for _ in range(n):
        weapons.append(input())
    weapon_sets = []
    diff = set([])
    for weapon_types in weapons:
        weapon_set = set([i+1 for i, weapon in enumerate(weapon_types) if weapon == '1'])
        weapon_sets.append(weapon_set)
    for w_set in weapon_sets:
        diff = w_set.symmetric_difference(diff)
    print(len(diff))
