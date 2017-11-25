vowel = ["A","E","I","O","U"]
def minion_game(string):
    lens = len(string)
    sscore = 0
    kscore = 0
    for i in range(lens):
      if (s[i] in vowel):
        kscore += lens - i
      else:
        sscore += lens - i
    if (kscore < sscore):
      print("Stuart {}".format(sscore))
    elif(kscore > sscore):
      print("Kevin {}".format(kscore))
    else:
      print("Draw")
      
    # your code goes here
