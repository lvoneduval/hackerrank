s = input().strip()
n = 0
for a in s:
  if (a.isalpha()):
    n |= (1 << (ord(a.lower()) - ord("a")))
print("pangram" if n == 67108863 else "not pangram")
