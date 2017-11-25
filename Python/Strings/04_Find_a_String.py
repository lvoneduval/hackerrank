def count_substring(string, sub_string):
    res = 0
    for i in range(len(string) - len(sub_string) + 1):
      res += (string[i:i + len(sub_string)] == sub_string)
    return (res)
