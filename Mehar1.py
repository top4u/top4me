import urllib.request
urllib.request.urlretrieve('https://raw.githubusercontent.com/top4u/top4me/main/test.py', "test.txt")
example1 = "test.txt"
file1 = open(example1, "r")
filecontent = file1.read()
print(filecontent)
