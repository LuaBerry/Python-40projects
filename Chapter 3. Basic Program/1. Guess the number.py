import random as rd
from xmlrpc.client import Boolean

answer = rd.randint(1, 100)
count = 1
while(True):
    try:
        a = int(input("Input number (1~100):"))
        if(answer > a):
            print("UP")
        elif(answer < a):
            print("DOWN")
        else:
            print(f"Correct! The answer is {answer}.")
            print(f"You tried {count} time" + "s" * Boolean(count - 1)+ ".")
            break
        count += 1
    except:
        print("Wrong Input. Please input number.")