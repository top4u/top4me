! pip install pyperclip
import pyperclip as content
text1 = "This is content for copying"
read = content.copy(text1)
print(read + "copied")
