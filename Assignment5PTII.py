import math
#name1 = input("What is the name of person 1? ")
#name2 = input("What is the name of person 2? ")
print("     Welcome to")
posx1 = int(input("What is the X position of person 1? "))
posy1 = int(input("What is the Y position of person 1? "))
posx2 = int(input("What is the X position of person 2? "))
posy2 = int(input("What is the Y position of person 2? "))
space1 = int(input("What is the radius of person 1s bubble? "))
space2 = int(input("What is the radius of person 2s bubble? "))

pos1 = str(posx1)+ " " + str(posy1)
pos2 = str(posx2) + " " + str(posy2)

spacestat = 0

distance = math.sqrt(((posx2 - posx1)**2) + ((posy2 - posy1)**2) )
if distance < space1 + space2:
    print("Spaces overlap")
if distance > space1 + space2:
    print("No overlap")
#inside space
if space1 > distance + space2:
    print("Person2 space inside person1 space")
if space2 > distance + space1:
    print("Person1 space inside person2 space")
#person inside space
if distance < space2 and distance < space1:
    print("both in space")
elif distance < space1:
    print("person1 is in person2 space")
elif distance < space2:
    print("Person2 is in person1 space")

