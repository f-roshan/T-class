#print("hi")
#print("ali")

#print("hi", end=" ")
#print("ali")
#** key value
#age = int(input("age"))
#print(type(age))

#my=list(range(100))
#print(my)

#m=[1,2,3,4]
#m.append(3)
#m.insert(2,9)
#m.remove(3)
#n=m.pop()
#del m[0]
#del m
#print(n)
#print(m)


#```````tupel`````````no apend```` cast to list then append then cast again
l=(1,2,3,4)
for item in l:
    print(item*2,sep=",",end=" ")


#```````SET```````

myset=set(range(10))
print("\n")
print(myset,)


#````````dictionary`````` dadash set!!!!!!!

mydict = {"name":"ali","family":"ahmadi"}
mydict["age"]="23"
print(mydict)

for k in mydict:
    print(k)

for k in mydict:
    print(mydict[k])

for item in mydict.items():
    print(item)    

for key, value in mydict.items():
    print(key,value,sep=" = ")


#````````````function~~~~~~~~~~~~
def sum(q,b):
    return q+b

def zarb(n):
    
    for i in range(n):
        for j in range(n):
            print(i,'*',j,'=',i*j, end=" ,")
        print('\n')    

zarb(5)        


