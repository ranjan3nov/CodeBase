#Sets  Does not have non repetetive element
a ={1,2,3,4,5}
print(type(a))
print(a)

# How to Create Empty sets

b=set()
print(type(b))
b.add(8)
b.add(10)

#Methods in Sets
b.add(5)
b.add(5)
b.add(5) #it only add one item

#lit Or Dictionary cannot be added in a set
# b.add([4,5,6])

#You can add tulip in a set
b.add((4,5,6))
print(len(b)) #Print the length of set b

b.remove(5)
print(b)
print(b.pop()) #remove random value from set
print(b.clear()) #Clear
print(b.union(a))
#Properties
#Unidexed
#Unorderd
#Cannot Change the value
#Cannot Contain Duplicate Value