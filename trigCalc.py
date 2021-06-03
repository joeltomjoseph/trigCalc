import math

''' Functions '''

def sinQ(opp, hyp):
    angleQ = math.asin(float(opp)/float(hyp))
    return angleQ

def cosQ(adj, hyp):
    angleQ = math.acos(float(adj)/float(hyp))
    return angleQ

def tanQ(opp, adj):
    angleQ = math.atan(float(opp)/float(adj))
    return angleQ

''' Main '''

answer1 = input("What part of the triange do you need?\n1. The Angle\n2. The Hypotenuse\n3. The Adjacent side\n4. The Opposite side\n\n(1, 2, 3 or 4)\n\n")

if answer1 == "1":
    answer2 = input("\nWhat sides do you have?\n\n1. Opposite + Hypotenuse\n2. Adjacent + Hypotenuse\n3. Opposite and Adjacent\n\n")
    
    if answer2 == "1":
        opp, hyp = input("\nPlease enter the values of the Opposite side (FIRST VALUE) and the Hypotenuse (SECOND VALUE) SEPERATED BY A COMMA\nlike 7.4, 8\n\n").split(", ")
        print("The angle is", math.degrees(sinQ(opp, hyp)), "degrees!")

    elif answer2 == "2":
        adj, hyp = input("\nPlease enter the values of the Adjacent (FIRST VALUE) and the Hypotenuse (SECOND VALUE) SEPERATED BY A COMMA\nlike 7.4, 8\n\n").split(", ")
        print("The angle is", math.degrees(cosQ(adj, hyp)), "degrees!")

    elif answer2 == "3":
        opp, adj = input("\nPlease enter the values of the Opposite (FIRST VALUE) and the Adjacent (SECOND VALUE) SEPERATED BY A COMMA\nlike 7.4, 8\n\n").split(", ")
        print("The angle is", math.degrees(tanQ(opp, adj)), "degrees!")

elif answer1 == "2":
    answer2 = input("\nWhat angle + side combination do you have?\n\n1. Angle + Opposite\n2. Angle + Adjacent\n\n")
    
    if answer2 == "1":
        angleQ, opp = input("\nWhat is your angle (FIRST VALUE) and your Opposite length (SECOND VALUE) SEPERATED BY A COMMA\nlike 62, 7.4\n\n").split(", ")
        hyp = float(opp)/math.sin(math.radians(float(angleQ)))
        print("The length of the Hypotenuse is", hyp)

    elif answer2 == "2":
        angleQ, adj = input("\nWhat is your angle (FIRST VALUE) and your Adjacent length (SECOND VALUE) SEPERATED BY A COMMA\nlike 62, 7.4\n\n").split(", ")
        hyp = float(adj)/math.cos(math.radians(float(angleQ)))
        print("The length of the Hypotenuse is", hyp)

elif answer1 == "3":
    answer2 = input("\nWhat angle + side combination do you have?\n\n1. Angle + Opposite\n2. Angle + Hypotenuse\n\n")

    if answer2 == "1":
        pass

    elif answer2 == "2":
        pass

elif answer1 == "4":
    pass