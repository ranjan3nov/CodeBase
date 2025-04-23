with open('FILE_IO/sample.txt') as f:
    content = f.read()

with open("FILE_IO/copy.txt", 'w') as a:
    a.write(content)