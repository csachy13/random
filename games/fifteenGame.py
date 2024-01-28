import random
import sys
import os
import re
import time
from termcolor import cprint, colored
from art import *

def indexMatrix(arr: list, val):
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            
            if arr[x][y] == '__':
                return x , y
    return 0,0

def neighbors(list: list, x: int, y: int):
    result = []
    try:
        result.append(list[x][y+1])
    except: pass
    try:
        result.append(list[x+1][y])
    except: pass
    try:
        result.append(list[x][y-1])
    except: pass
    try:
        result.append(list[x-1][y])
    except: pass
    return result
def group(li):
    return [li[:4], li[4:8], li[8:12], li[12:16]]
def pad(a):
    if len(a) == 1:
        return '0'+ a

    else:
        return a
def gic(l,x,y):
    num = str(l[x][y])
    if str(4*x+y+1).rjust(2,"0") == num:
        return colored(l[x][y], 'cyan')
    else:
        return l[x][y]
def display(l, score):
    print(".__  __  __  __.")
    afa= 0
    print("|" + '  '.join([gic(l,afa,0), gic(l,afa,1), gic(l,afa,2), gic(l,afa,3)]) + '|')
    afa=1
    print("|" + '  '.join([gic(l,afa,0), gic(l,afa,1), gic(l,afa,2), gic(l,afa,3)]) + '|')
    afa=2
    print("|" + '  '.join([gic(l,afa,0), gic(l,afa,1), gic(l,afa,2), gic(l,afa,3)]) + '|')
    afa=3
    print("|" + '  '.join([gic(l,afa,0), gic(l,afa,1), gic(l,afa,2), gic(l,afa,3)]) + '|')

    print(".‾‾  ‾‾  ‾‾  ‾‾." + " "*50 + colored("Score: "+str(score).rjust(3, "0"), "blue"))

scorefile = open(os.getcwd() +"data.txt", "a+")

cprint(text2art("The 15 Game"), 'blue')
cprint('Version whoCares', 'green')

numlist = list(map(str, [1,2,3,4,5,6,7,8,9,10,11,12,13,15,14,'__']))

numlist = list(map(pad, numlist))

random.shuffle(numlist)

finished = False

origscore=500

score = origscore

display(group(numlist), score)

yessir=False
while not finished:
    a = ''
    while not str(a) in neighbors(group(numlist), indexMatrix(group(numlist), '__')[0],indexMatrix(group(numlist), '__')[1]):
        a = pad(input(colored("Number: ", 'magenta',attrs=['bold'])))
        if a == "FF":
            score = 10
        if a == "GG":
            yessir=True
    index1 = numlist.index(a)
    index2 = numlist.index('__')
    numlist[index1], numlist[index2] = numlist[index2], numlist[index1]
    os.system('clear')
    display(group(numlist), score)
    finished = numlist == sorted(numlist) or group(numlist) == [['01', '02', '03', '04'],['05', '06', '07', '08'],['09', '10', '11', '12'],['13', '15', '14', '__']] or yessir
    score -= 1
    if score < 1:
        print((colored(text2art('Game Over :('), 'red')))
        sys.exit()
coltext = text2art("SORTED! :D", decoration='blink')
cprint(coltext, "green")
print(f'{colored("It took ", "blue")}{colored(str(origscore-score), "green")} moves to solve the puzzle!')
print("Do you want to put your name on the leaderboard?")
cprint('     [1] Yes', 'green')
cprint('     [2] No', 'red')
if input('>') == '1':
    cprint('What is your name?', 'blue', attrs=['bold'])
    name = input('>')
    scorefile.write(str('\n' + name + ':' + str(origscore - score)))
scorefile.close()
