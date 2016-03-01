import random

try:
    sides = int(raw_input("How many sides per dice? "))
    dice = int(raw_input("How many dice to roll? "))
    roll = int(random.random()*sides*dice)
except Exception as e:
    print "Please enter numerical values only, will roll one d20"
    sides = 20
    dice = 1
    roll = int(random.random()*sides*dice)
while roll < dice:
    if sides == 1:
        print "There is no such dice. Flipping coins instead"
        sides = 2
    else:
        roll = int(random.random()*sides*dice)



print "Your roll is: " + str(roll)
