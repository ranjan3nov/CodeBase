import os

oldname="FILE_IO/rename.txt"
newname="FILE_IO/rename_by_pr_08.txt"

with open(oldname) as f:
    content = f.read()

with open(newname,"w") as f:
    f.write(content)

os.remove(oldname)