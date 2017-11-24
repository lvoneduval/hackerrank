i,j,k = [int(x) for x in input().split()]
beauti = [nb for nb in range(i , j) if (nb - int(str(nb)[::-1])) % k == 0]
print(len(beauti))
