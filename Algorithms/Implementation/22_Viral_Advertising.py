n = int(input())
f = [2]
for i in range(n - 1):
    f.append(int(3 * f[i] / 2))
print(sum(f))
