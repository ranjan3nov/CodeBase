import random

def gameResult(comp, player):
    if comp == player:
        return None
    elif comp == 'S':
        if player =='W':
            return False
        elif player =="G":
            return True
    elif comp == 'W':
        if player =='G':
            return False
        elif player =="S":
            return True
    elif comp == 'G':
        if player =='S':
            return False
        elif player =="W":
            return True
while True:
    randNo = random.randint(1,3)
    a =print("Computer Turn 1 Turn: Sanke(S) Water(w) or Gun(G)")
    if randNo == 1:
        comp ='S'
    elif randNo == 2:
        comp = 'W'
    elif randNo == 3:
        comp = 'G'

    player =input("Your Turn: Sanke(1) Water(2) or Gun(G): ")
    player = player.upper()

    a = gameResult(comp,player)

    print("Comp Choose : ",comp)
    print("You Choose : ",player)
    if a == None:
        print("THe game is tie")
    elif a:
        print("You win")
    else:
        print("You lose")