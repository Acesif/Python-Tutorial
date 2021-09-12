

from math import *
from random import *
def numberRandomizer():
    print("From what range of numbers you want to pick from?")
    one = int(input("Pick your lower bound"))
    two = int(input("Pick your upper bound"))
    print(randint(one,two))

def endingOrSeparators():
    s = input()
    print("Now, to present you:",end = " ")
    print("a","b","c", sep=s)

def globalLocalchecker():
    global haha #try the code with and without commenting out this line
    haha = 1
    print(haha)
# haha = 20
# globalLocalchecker()
# print(haha)

def errorShitter():
    num = input()
    try:
        if int(num)>=4:
            print('lotta puss')
        elif 4>int(num)>=0:
            print('empty puss')
        else:
            print('das minus bro')
    except:
        print('bruh that not a valid number')

# errorShitter()


