if __name__ == '__main__':
    n = int(input())
    if (n % 2 or (n >= 6 and n <= 20)):
      print("Weird")
    else:
      print("Not Weird")