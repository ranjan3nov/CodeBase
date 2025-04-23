# Check wether the files content are same or not

file1 ="FILE_IO/copy.txt"
file2 ="FILE_IO/sample.txt"

with open(file1) as f:
    f1 =f.read()

with open(file2) as f:
    f2 =f.read()


if f1 == f2:
    print("They are identical")
else:
    print("They are not identical")

