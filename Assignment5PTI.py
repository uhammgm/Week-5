import random


x = random.randint(1,10)
#print(x)


y = int(input("Guess a number 1-10: "))

if x - y == 0: 
    print("Honored to play with you, Master.")

elif x - y == 1 or x - y == -1 :
    print("You are a worthy opponent, Knight.")

elif x - y == 2 or x - y == -2:
    print("You have much to learn, Padawan.")
elif x - y == 3 or x - y == -3:
    print("Youngling, your time will come.")
elif x - y > 3 or x - y < -3:
    print("Keep working hard in the Service Corps.")

print(" ")

print ("You picked"), print(y), print("the number was"), print(x), print(" ")