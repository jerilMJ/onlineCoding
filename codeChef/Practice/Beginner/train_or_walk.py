t = int(input())
minimum = []
for _ in range(t):
    n, a, b, c, d, p, q, y = map(int, input().split())
    axis = map(int, input().split())
    dist = {}

    for city, coords in enumerate(axis):
        dist[city + 1] = coords

    walk_total_time = abs(dist[b] - dist[a]) * p

    time_from_A_to_C = abs(dist[c] - dist[a]) * p

    if time_from_A_to_C <= y:
        train_total_time = y + abs(dist[d] - dist[c]) * q + abs(dist[d] - dist[b]) * p
    else:
        train_total_time = walk_total_time + 100

    print(min([walk_total_time, train_total_time]))

