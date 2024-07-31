def swap(s, i, j):
    s[i], s[j] = s[j], s[i]

def permute(s, left, right):
    if left == right:
        perms.add(''.join(s))
    for i in range(left, right):
        swap(s, left, i)
        permute(s, left + 1, right)
        swap(s, left, i)

s = list(input())
s.sort()
perms = set()
permute(s, 0, len(s))
for p in sorted(perms):
    print(p)