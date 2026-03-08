import os
import time

#lists all files in system32
sys32 = os.listdir(r"C:\Windows\system32")

def winp():
    #WINP stands for "Wrong Input"
    #I know this seems useless but I use it a lot and I need a shortcut
    print("Nah twin ts is not right for math try again!")
    calc()


#this fake deletes all your files
def fakedelete():
    newnames = []
    for name in sys32:
        fullname = (r"Deleting C:\windows\system32/" + name)
        newnames.append(fullname)
        print("\n".join(newnames))
        time.sleep(0.01)

def calc():
    #intro
    print("Welcome to my calc twin")
    print("It's only four functions though because I'm lazy")
    print("Get ready to do some calcing")

    #numbers prompt
    num1false = input("Number 1:\n")
    if num1false.isdigit():             #making sure the number is a float or integer
        num1 = int(num1false)
    else:
        winp()
    
    #prompt for operator
    oper = input("Operator (+, -, *, /)\n")
    if oper not in ["+","-","/","*"]:       #making sure it's an actual operator and not wrong
        winp()
    
    num2false = (input("Number 2:\n"))
    if num2false.isdigit():             #making sure the number is a float or integer
        num2 = int(num2false)
    else:
        winp()

    if oper == "+":
        ans = num1 + num2
        print ("The answer is ")
        print(ans)

    if oper == "-":
        ans = num1 - num2
        print ("The answer is ")
        print(ans)

    if oper == "*":
        ans = num1 * num2
        print ("The answer is ")
        print(ans)

    if oper == "/":
        ans = num1 / num2
        print ("The answer is ")
        print(ans)

    time.sleep(0.5)
    print("Yo twin")
    time.sleep(0.2)
    print("Twin")
    time.sleep(0.2)
    print("Twin")
    time.sleep(0.2)
    print("Twin")
    time.sleep(0.5)
    print("Brace for impact twin")
    time.sleep(1)
    fakedelete()

calc()
