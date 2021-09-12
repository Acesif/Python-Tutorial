#This game is about you guessing a random number picked by the bot
from random import *
print('I have a number in my mind which is between 0-10, can you guess it?')
num = randint(0,10)
for i in range(0,6):
    x = int(input())
    if(x > num):
        print('Nope, too high')
    elif(x < num):
        print('Nope, too low')
    elif(x is num):
        print('Damn, that\'s the right guess')
        break
    else:
        print('Lmao, I guess you couldn\'t figure it out but the number was ',str(num))