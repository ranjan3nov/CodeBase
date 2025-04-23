with open('FILE_IO/another.txt', 'r') as f:
    a = f.read()
# print(a)
with open('FILE_IO/another.txt', 'w') as f:
    a = f.write("I love INDIA")
print(a)