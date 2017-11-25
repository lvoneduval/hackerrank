from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    print ("Start :", tag)
    for a in attrs:
      print ("-> {} > {}".format(a[0],a[1]))

  def handle_endtag(self, tag):
    print ("End   :", tag)
  
  def handle_startendtag(self, tag, attrs):
    print ("Empty :", tag)
    for a in attrs:
      print ("-> {} > {}".format(a[0],a[1]))

parser = MyHTMLParser()
i = int(input())
l = ""
for _ in range(i):
  parser.feed(input())

