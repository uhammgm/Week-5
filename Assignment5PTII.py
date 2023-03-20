import math
#name1 = input("What is the name of person 1? ")
#name2 = input("What is the name of person 2? ")
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
if distance > space1 + space2:
    spacestat = 1
else:
    spacestat = 2

if spacestat == 1:
    print("There are no conflicts.")
if spacestat == 2:
    print("Conflict detected.")

