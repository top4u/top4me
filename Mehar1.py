TRED =  '\033[31m' # Green Text
TGREEN =  '\033[32m' # Green Text
TBOLD =  '\033[1m' # BOLD Text
TBACKRED =  '\033[41m' # BACKGROUND Text

print(TRED + " COPY ALL CONTENT FROM BOX BELOW")
print(TRED + " OPEN NEW NOTEBOOK")
print(TRED +  " PASTE COPIED CONTENT & FOLLOW INSTRUCTIONS")


print( "---------------------Copy from Here to end-----------------------------------")


import urllib.request
urllib.request.urlretrieve('https://raw.githubusercontent.com/top4u/top4me/main/test.py', "test.txt")
example1 = "test.txt"
file1 = open(example1, "r")
filecontent = file1.read()
print(filecontent)

