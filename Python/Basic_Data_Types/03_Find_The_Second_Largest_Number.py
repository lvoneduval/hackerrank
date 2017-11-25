if __name__ == '__main__':
    n = int(input())
    arr = [int(a) for a in input().split(" ")]
    l = max(arr)
    i = l
    while (l == i):
      arr.remove(l)
      l = max(arr)
    print(l)
