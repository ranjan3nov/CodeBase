def game():
    return 9

score = game()

with open("FILE_IO/highscore.txt") as f:
    hiscoreStr = f.read()

if hiscoreStr=='':
     with open("FILE_IO/highscore.txt", "w") as f:
        f.write(str(score))

elif int(hiscoreStr)<score:
    with open("FILE_IO/highscore.txt", "w") as f:
        f.write(str(score))

