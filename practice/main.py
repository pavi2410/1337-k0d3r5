MAX, N = map(int, input().split())
types = map(int, input().split())

r = list(enumerate(types))

f = []

maxsum = 0

for i, t in r[::-1]:
    isums = [i]
    sum = t
    for j, tt in r[:i][::-1]:
        s = sum + tt
        if s < MAX:
            sum = s
            isums.append(j)
            continue
        elif s == MAX:
            sum = s
            isums.append(j)
            break
        elif s > MAX:
            continue
    if sum > maxsum:
        maxsum = sum
        f = isums

f.sort()

print(len(f), maxsum)
print(' '.join(map(str, f)))