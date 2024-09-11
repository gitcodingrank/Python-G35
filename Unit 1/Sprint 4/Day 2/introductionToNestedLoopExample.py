#Nested Loop: When any iteration/round of loop is connected/related to some set of rounds then you can say there is loop inside loop

"""
syntax:

#outer loop
for var_name in range(n):
    #inner loop
    for var_name in range(n):
"""

#Example 1: Golgappe analogy:

# for chintu in range(1, 6):
#     print("Chintu has done with his round", chintu)
    
#     for familyMember in range(1, 5):
#         print(f"Family Member {familyMember} has done his round {chintu}")


#Example 2: Father Son Analogy
#In Each round of Father son goes for five rounds
"""
Father Rounds: 2
Father Round 1: 
        Son Round 1
        Son Round 2
        Son Round 3
        Son Round 4
        Son Round 5
Father Round 2: 
        Son Round 1
        Son Round 2
        Son Round 3
        Son Round 4
        Son Round 5
"""

# for father in range(1, 3):
#     print("Father has started Round:", father)

#     for son in range(1, 6):
#         print("Son has done with his Round:",son)

#     print("Father has ended Round:", father)


#Example: Print from 1 to 5 in one line.

# for i in range(1, 6):
#     print(i, end=" ")

#Without end parameter.

# bag = ""

# for j in range(1, 6):
#     bag+= str(j)+" "

# print(bag)

#Example 3: Print in the following manner:
"""
Father Round 1: Son Rounds: 1 2 3 4 5
Father Round 2: Son Rounds: 1 2 3 4 5
"""

for father in range(1,3):
    sonBag = ""
    for son in range(1, 6):
        sonBag+=str(son)+" "
    print(f"Father Round: {father}: Son Rounds: {sonBag}")

