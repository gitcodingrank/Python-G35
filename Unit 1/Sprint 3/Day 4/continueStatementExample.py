#Continue Statment: it is used to terminate/stop/skip only current round/iteration of the given loop at certain condtion


"""
syntax:
sp = 1
while condition: 
   if condition
        continue
    sp+=1

"""

#Example: print number fro 1 to 10 but skip 5 and 7

sp = 0

while sp<=10:

    sp+=1
    if sp==5 or sp == 7:
        continue
    print(sp)

    