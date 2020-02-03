max, numTypes = map(int, input().split())
types = map(int, input().split())

r = [(i, t) for i, t in enumerate(types)]
r.sort(key=lambda i: i[1], reverse=True)

f = []
k = 0
for i, t in r:
    if k + t <= max:
        k += t
        f.append(i)

f.sort()
print(len(f))
print(' '.join(map(str, f)))