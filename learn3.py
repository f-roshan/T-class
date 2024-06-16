import os
#name = input("esm bede")
name = "fatemeh"
os.chdir("d:\\")
os.makedirs(name)
os.chdir(name)
for i in range(9):
    os.mkdir(str(i))
    