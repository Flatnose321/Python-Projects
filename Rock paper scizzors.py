from random import randint
Number=randint(1,3)
#^Random number generater very usefull.
#1 is rock 2 is paper 3 is scizzors
user=str(input("Rock, Paper or Scizzors"))
if Number==1 and user=="Rock":
    print("Tie")
elif Number==2 and user=="Rock":
    print("You lose")
elif Number==3 and user=="Rock":
    print("You win")
elif Number==1 and user=="Paper":
    print("Win")
elif Number==2 and user=="Paper":
    print("Tie")
elif Number==3 and user=="paper":
    print("You lose")
elif Number==1 and user=="Scizzors":
    print("You lose")
elif Number==2 and user=="Scizzors":
    print("You win")
elif Number==3 and user=="Scizzors":
    print("Tie")
else:
    print("Error")

if Number==1:
    print("The computer picked Rock and you picked " + user)
elif Number==2:
    print("The computer picked Paper and you picked " + user)
elif Number==3:
    print("The computer picked Scizzors and you picked " + user)
else:
    print("Error")