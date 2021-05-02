* print("\033[1;31;40m Bright Red COPY ALL CONTENT FROM BOX BELOW/n")
* print("\033[1;31;40m Bright Red OPEN NEW NOTEBOOK/n")
* print("\033[1;31;40m Bright Red PASTE COPIED CONTENT & FOLLOW INSTRUCTIONS/n")

prin("---------------------Copy from Here to end-----------------------------------")

import urllib.request
urllib.request.urlretrieve('https://raw.githubusercontent.com/top4u/top4me/main/test.py', "test.txt")
example1 = "test.txt"
file1 = open(example1, "r")
filecontent = file1.read()
print(filecontent)

