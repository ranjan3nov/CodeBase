#readline funciton read only one line at a time each time we call it read the new line
f = open('FILE_IO/sample.txt')
# data = f.read()
data = f.readline()
print(data)
data = f.readline()
print(data)

f.close()

# Other Method to read the file
""" 
r -> open for reading (by default)
w -> open for writing 
a -> open for appending
+ -> open for updating

'rb' will open for read in binary mode
'rt' will open for read in text mode
"""