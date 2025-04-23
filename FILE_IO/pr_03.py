# with open("FILE_IO/sample.txt") as f:
#     content = f.read()

# content = content.replace("donkey","$%&@$^#")

# with open("FILE_IO/sample.txt","w") as f:
#     f.write(content)


# Replacing more than one variable

words = ["donkey","kaddu","mote"]

with open("FILE_IO/sample.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"$%&@$^#")
    with open("FILE_IO/sample.txt","w") as f:
        f.write(content)
