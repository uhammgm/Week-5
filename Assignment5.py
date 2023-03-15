import random

x = 8
#x = random.randint(1,10)
#print(x)

y = int(input("Guess a number 1-10: "))

if x - y == 0: 
    print("Honored to play with you, Master.")

elif x - y == 1 or x - y == -1 :
    print("You are a worthy opponent, Knight.")