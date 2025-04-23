# Collection of  key Value Pairs

myDict ={
    "Fast":"In a Qucik Manner",
    "Ranjan":"A Coder",
    "Marks":['1,2,5'],#list
    "insideDict":{'Ranjan':'Programmer'}
}
print(myDict['Fast'])
print(myDict['Ranjan'])
print(myDict['Marks'])
print(myDict['insideDict'])
print(myDict['insideDict']['Ranjan'])
#Dictionary is Unorderd
#Dictionary is mutable
#Dictionary is indexed

#Methods of Dictionary
print(list(myDict.keys()))#print the keys
print(type(myDict.keys()))
print(myDict.values())#Print the values
print(myDict.items())#print the keys , values for all the contents of the dictionary , tuples

print(myDict)
updateDict={
    "Singh":"Friend"
}
myDict.update(updateDict)
print(myDict)
print(myDict.get("Ranjan2"))# Not give the error it return none if key is not present while print(myDict["Ranjan2"]) give the error

