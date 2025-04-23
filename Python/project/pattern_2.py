# ***
# * *
# ***

# n =3
# for i in range(1, 4):
    # if(i == 2):
    #     print("*   *")
    # else:
    #     print("* " * 3)

size = 4

for i in range(size):
    for j in range(size):
        # Print a star if the current position is on the edge of the square
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()