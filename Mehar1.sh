#! /bin/bash

wget /resources/data/test.txt https://raw.githubusercontent.com/top4u/top4me/main/test.txt &> /dev/null
txt = "test.txt"
file1 = open(txt, "r")
filecontent = file1.read()
print(filecontent)
