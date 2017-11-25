def pourcentage(tab):
  res = 0
  for i in range(len(tab)):
    res += tab[i]
  return(res/(i + 1))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{0:.2f}".format(pourcentage(student_marks[query_name])))
