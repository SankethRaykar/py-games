import random
again = True
#we use while loop for random loop of the numbers
while again:
    print(random.randint(1,6))
    for_user_another_diceroll =input("do u want ot roll the dice again? (y/n):")
    if for_user_another_diceroll.lower() == 'y':
        continue
    else:
        break #can also use again=false instead of break y