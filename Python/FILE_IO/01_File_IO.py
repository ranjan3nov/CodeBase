# By default mode is r which means reading a file
# f = open('sample.txt','r')
f = open('FILE_IO/sample.txt')
# data = f.read()
data = f.read(5)
print(data)

f.close()

# Other Method to read the file