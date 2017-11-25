from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  def handle_data(self, data):
    if (data.strip()):
      print(">>> Data")
      print(data)
      
  def handle_comment(self, data):
    nb_line = len(data.split("\n"))
    if (nb_line > 1):
      print(">>> Multi-line Comment")
    else:
      print(">>> Single-line Comment")
    if (data.strip()):
      print(data)
