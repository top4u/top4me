import urllib
import request
import urllib.request

with urllib.request.urlopen("https://raw.githubusercontent.com/top4u/top4me/main/test.txt") as url:
s = url.read()
print(s)
