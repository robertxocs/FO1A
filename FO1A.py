import random

## OPDRACHT 1 ##


def opdracht1for():
    lengte = int(input('Hoe groot?'))
    for i in range(1, lengte):
        print(f'{"* "*i}')
    for j in range(lengte, 0, -1):
        print(f'{"* "*j}')
def opdracht1foranderekant():
    lengte = int(input('Hoe groot?'))
    for i in range(lengte, 0, -1):
        print(f'{"* "*i}')
    for j in range(2, lengte+1, 1):
        print(f'{"* "*j}')

def opdracht1while():
    lengte = int(input('Hoe groot?'))
    i = 1
    j = lengte-1
    while i<=lengte:
        print(f'{"* "*i}')
        i+=1
    while j != 0:
        print(f'{"* "*j}')
        j-=1
def opdracht1whileanderekant():
    lengte = int(input('Hoe groot?'))
    i = 1
    j = lengte
    while j != 0:
        print(f'{"* " * j}')
        j -= 1
    while i <= lengte:
        print(f'{"* " * i}')
        i += 1

#opdracht 1 met 1 for loop?
def opdracht1eenforloop(lengte):
    count=lengte
    for i in range(1, lengte*2):
        if i<lengte:
            print(f'{"* " * i}')
        if i >= lengte:
            print(f'{"* "*count}')
            count -= 1

## OPDRACHT 2 ##

def tekstcheck():
    input1=input('Geef een string:')
    input2=input('Geef een string:')
    for i in range(len(min(input1, input2))): #loop over de hoeveelheid characters in de kortste string
        if input1[i] != input2[i]: #als er binnen de kortste string al een verschil is met de langere string
            return print(f'Het eerste verschil zit op index: {i}') #return de index
        else:
            return print(f'Het eerste verschil zit op index: {min(len(input1), len(input2))}') #return index van eerste "langere" character

## OPDRACHT 3##

## A ##

def count(x, lst):
    #telt hoe vaak x voorkomt in lst
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count

## B ##
def neighbourdiff(lst):
    #controleert het grootste verschil tussen naast elkaar gelegen waardes in lst
    biggestdiff = 0
    for i in range(0, len(lst)-1):
        if lst[i+1]-lst[i]>biggestdiff:
            biggestdiff = lst[i+1]-lst[i]
    return biggestdiff

## C ##
def eisenchecker(lst):
    #controleert of een lijst meer enen dan nullen heeft en of de lijst niet meer dan 12 nullen heeft
    return count(1, lst) > count(0, lst) and count(0, lst) <= 12

## OPDRACHT 4 ##
##omdat ik niet zeker wist of splicing telde als een bibliotheek functie, heb ik drie versies gemaakt
##aptly named...

def biebfunctiepalindroomchecker(str):
    #checkt op palindromen met reversed method
    return str == ''.join(reversed(str))


def palindroomchecker(str):
    #checkt op palindromen door str te splicen in negatieve richting
    return str == str[::-1]

def handmatigreversepalindroomchecker(str):
    #draait de string om met een while loop
    reversestr = ''
    index = len(str)
    while index:
        index -= 1
        reversestr += str[index]
    return reversestr == str

## OPDRACHT 5 ##
def mergesort(lst):
    #merge sort hakt een lijst
    if len(lst)>1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]

        mergesort(left)
        mergesort(right)
        linkercounter=rechtercounter=counter=0
        while linkercounter < len(left) and rechtercounter < len(right):
            if left[linkercounter] < right[rechtercounter]:
                lst[rechtercounter]=left[linkercounter]
                linkercounter+=1
            else:
                lst[rechtercounter]=right[counter]
                counter+=1
            counter+=1
        while linkercounter < len(left):
            lst[rechtercounter]=left[linkercounter]
            linkercounter+=1
            rechtercounter+=1
        while counter < len(right):
            lst[rechtercounter]=right[j]
            counter+=1
            rechtercounter+=1
        return lst
    else: # als de lijst 1 element bevat (of 0), dan is hij al gesorteerd
        return lst

## OPDRACHT 6 ##
def gemiddelde(lst):
    return sum(lst) // len(lst)

def gemiddeldelijsten(lst):
    ans = []
    for i in lst:
        ans.append(sum(i) // len(i))
    return ans

## OPDRACHT 7 ##
def randomraden():
    geraden = False
    ans = random.randrange(1, 25, 1)
    while geraden == False:
        gok = int(input('Gok een getal tussen de 1 en 25'))
        if gok == ans:
            print('Correct! Doei.')
            geraden = True

## OPDRACHT 8 ##
def compress(file):
    with open(file) as f:
        lines = [x.strip() for x in f.readlines() if x and not x.isspace()]
    with open(file+'_compressed', 'w') as o:
        o.writelines(lines)

## OPDRACHT 9 ##
def cyclic_binary_shift(ch, n):
    binarychar = '{0:07b}'.format(ord(ch)) #convert de ch naar decimal, en de decimal naar binary
    binlist = [i for i in binarychar] #zet de binary in een lijst
    shiftedbin = binlist[n:] + binlist[:n] #zet de lijst in andere volgorde
    ans = chr(int(''.join(shiftedbin),2)) #zet de nieuwe lijst om naar een int, en zet die om naar een character
    return ans

## OPDRACHT 10 ##
def fibonaccifinder(n, a=0, b=1):
    if n > 1:
        return fibonaccifinder(n-1, b, a+b)
    return (a, b)[n]


## OPDRACHT 11 ##
def caesarcijfers():
    inputstring = input('Geef een string:')
    inputkey = int(input('Geef een rotatie:')) % 25 #dit zorgt ervoor dat we ook rotaties van > 50 kunnen invullen, ookal slaat dat niet echt ergens op
    alphabet = 'abcdefghijklmnopqrstuvwyz'
    upperalphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    outputstring = []
    for i in inputstring:
        if i.isupper():
            index = upperalphabet.find(i) + inputkey
            if index > 25:
                index -= 25
            outputstring.append(upperalphabet[index])

        elif i.islower():
            index = alphabet.find(i) + inputkey
            if index >= 25:
                index -= 25
            outputstring.append(alphabet[index])

        else:
            outputstring.append(i)

    return ''.join(outputstring)

## OPDRACHT 12 FizzBuzz ##
def FizzBuzz2Checks(x):

    for i in range(1, x):
        if i % 3 == 0:
            if i % 5 == 0:  #door deze if statement te nesten testen we elke i maximaal 2 keer ipv 3 keer.
                print('Fizzbuzz')
            else:
                print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

def FizzBuzz15mod(x):
    for i in range(1, x):
        if i % 15 == 0: #mod 15 == mod%3 en dan mod%5
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)