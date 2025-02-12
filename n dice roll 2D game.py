import random
#the below are the ascii codes for the shape of the dice
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

#● ┌ ─ ┐ │ └ ┘   

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

different_dice_arts={
    1:("┌─────────┐" ,
       "│         │" ,
       "│    ●    │" ,
       "│         │",
       "└─────────┘"),

    2:("┌─────────┐" ,
       "│ ●       │" ,
       "│         │" ,
       "│       ● │",
       "└─────────┘"),

    3:("┌─────────┐" ,
       "│ ●       │" ,
       "│    ●    │" ,
       "│       ● │",
       "└─────────┘"),

    4:("┌─────────┐" ,
       "│ ●     ● │" ,
       "│         │" ,
       "│ ●     ● │",
       "└─────────┘"),

    5:("┌─────────┐" ,
       "│ ●     ● │" ,
       "│    ●    │" ,
       "│ ●     ● │",
       "└─────────┘"),

    
    6:("┌─────────┐" ,
       "│ ●  ●  ● │" ,
       "│         │" ,
       "│ ●  ●  ● │",
       "└─────────┘")

}

dice = []
total =0
num_of_dice = int(input("define the number of dice u want to display:"))
#for generating the random numbers
for die in range(num_of_dice):
    dice.append(random.randint(1,6))
#this for loop is to enter every tuples(the die_arts) {to display the dice in vertical follow the comment code}
'''for die in range(num_of_dice):
    for line in different_dice_arts.get(dice[die]):
        print(line)'''
# for horizontal display of the dices
for line in range(5):
    for die in dice:
        print(different_dice_arts.get(die)[line], end ="")
    print()
#for total of all the dices
for die in dice:
    total +=die
print(f"total: {total}")

