import os
#name = input("name bede")
name = "ghasem"
os.chdir("d:\\")
os.makedirs(name)
os.chdir(name)
n= 10
f = open("sample.txt","w+")
for i in range(n):
    f.write(str(i))
    f.close