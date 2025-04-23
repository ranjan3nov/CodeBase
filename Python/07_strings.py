# we use sing qoute double adn triple  qoute as per our needs
#string concatenating
fname = "Alok"
lname = " Ranjan"
print(fname + lname)
print(fname[0])
# name[3] = "d" -----> Does not Work

#string slicing
print(fname[0:3])

#python support negative indexes
# -1 will give the index
print(fname[-1])

#slicing with skip value
lname = "Ranjan is a coder"
d = lname[0:17:2]  # it says print evry twice character from 0 to 13 Rj iace
print(d)

#strings function

story = "once upon a time alok was fan of Gurukul"
print(len(story))#return the length of string
print(story.endswith("asdf"))
print(story.count("i"))
print(story.capitalize())
print(story.find("upon"))# tells about the first occurance
print(story.replace("upon","lastone"))
