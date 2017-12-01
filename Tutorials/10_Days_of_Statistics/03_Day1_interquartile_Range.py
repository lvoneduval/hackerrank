from collections import Counter
def median(l,size):
  if (size % 2):
    return(l[size//2])
  else:
    return((l[size//2 - 1] + l[size//2]) / 2)

# Get inputs.
n = int(input())
l = list(map(int,input().split(" ")))
f = list(map(int,input().split(" ")))

# Create S containing the data from set l at the respective frequencies specified by f.
S = sorted(Counter(dict(zip(l,f))).elements(), key=lambda x: x)

# Split this data set exactly in half.
len_half = len(S)//2
L = S[:len_half]
U = S[-len_half:]

# Next, we find Q1 and Q3.
Q1 = median(L, len(L))
Q3 = median(U, len(U))

# From this, calculate the interquartile range and print it.
print("{0:.1f}".format(Q3 - Q1))
