print(" COPY ALL CONTENT FROM BOX BELOW")
print(" OPEN NEW NOTEBOOK")
print( " PASTE COPIED CONTENT & FOLLOW INSTRUCTIONS")


print( "---------------------'\033[1mCopy from Here to end'-----------------------------------"/n)


import urllib.request
urllib.request.urlretrieve('https://raw.githubusercontent.com/top4u/top4me/main/test.py', "test.txt")
example1 = "test.txt"
file1 = open(example1, "r")
filecontent = file1.read()
print(filecontent)

