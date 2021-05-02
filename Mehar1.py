print(" COPY ALL CONTENT FROM BOX BELOW")
print(" OPEN NEW NOTEBOOK")
print(" PASTE COPIED CONTENT & FOLLOW INSTRUCTIONS")
TGREEN =  '\033[32m' # Green Text

print(TGREEN + "---------------------Copy from Here to end-----------------------------------")


print(Fore.RED + 'some red text')

import urllib.request
urllib.request.urlretrieve('https://raw.githubusercontent.com/top4u/top4me/main/test.py', "test.txt")
example1 = "test.txt"
file1 = open(example1, "r")
filecontent = file1.read()
print(filecontent)

