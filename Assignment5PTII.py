import math
print(" DO NOT PUT SPACES AFTER ANSWERS")
print("Person 1")
name1 = input("     What is the name of person 1? ")
posx1 = int(input("     What is the X position of person 1? "))
posy1 = int(input("     What is the Y position of person 1? "))
space1 = int(input("    What is the radius of person 1s bubble? "))
print("Person 2")
name2 = input("     What is the name of person 2? ")
posx2 = int(input("     What is the X position of person 2? "))
posy2 = int(input("     What is the Y position of person 2? "))
space2 = int(input("    What is the radius of person 2s bubble? "))

pos1 = str(posx1)+ " " + str(posy1)
pos2 = str(posx2) + " " + str(posy2)

spacestat = ""
overstat = ""
personstat = ""

distance = math.sqrt(((posx2 - posx1)**2) + ((posy2 - posy1)**2) )
if distance < space1 + space2:
    overstat = " and " + name1 + " and " + name2 + "'s spaces overlap."
     #print("Spaces overlap")
#elif distance > space1 + space2:
    #overstat = "."
    #print("No overlap")
#inside space
if space1 > distance + space2 and space2 > distance + space1:
    spacestat = "They are both in eachothers space."
elif space1 > distance + space2:
    spacestat = name2 + "'s space is in " + name1 + "'s space" 
    #print("Person2 space inside person1 space")
elif space2 > distance + space1:
    spacestat = name1 + "'s space is in " + name2 +"'s space"
    #print("Person1 space inside person2 space")
else:
    spacestat = "Neither of their spaces are in eachothers space"

#person inside space
if distance < space2 and distance < space1:
    personstat = name1 + " and " + name2 + " are both in eachothers space"
    #print("both in space")
elif distance < space1:
    personstat = name1 + " is in " + name2 + "'s space."
    #print("person1 is in person2 space")
elif distance < space2:
    personstat = name2 + " is in " + name1 + "'s space."
    #print("Person2 is in person1 space")
else:
    personstat = "Neither of them are in eachothers space."

msg = "\n" + "Social Situation Analysis Results:\n" + "Person test: " + personstat + "\n" + "Space test: " + spacestat + overstat 

print(msg)

