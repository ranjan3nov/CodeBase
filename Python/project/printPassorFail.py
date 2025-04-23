sub1 = int(input("Enter marks of Subject 1 :"))
sub2 = int(input("Enter marks of Subject 2 :"))
sub3 = int(input("Enter marks of Subject 3 :"))

if(sub3<33 or sub2<33 or sub1<33):
    print("You are Fail due to less in one of the subject")

elif(sub1+sub2+sub3)/3 < 40:
    print("You are Fail due to total percentage less than 40 ")
else:
    print("Congratulation : You are pass!!")
