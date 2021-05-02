import urllib
url = "https://raw.githubusercontent.com/top4u/top4me/main/test.txt"
f = urllib.urlopen(url)
print f.read()
txt = "test.txt"
file1 = open(txt, "r")
filecontent = file1.read()
print(filecontent)
