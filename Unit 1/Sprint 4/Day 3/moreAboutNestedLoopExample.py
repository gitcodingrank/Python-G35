"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

Rows: 4: outer loop is responsible for rows
Columns: 5: inner loop is responsible for column
"""
#defaut behavior of end parameter= \n
# for father in range(1, 5):
#   for son in range(1, 6):
#     print(son, end=' ')
#   print()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# for father in range(1, 6):
#   for son in range(1, father+1):
#     print(son, end=' ')
#   print()


"""
*
* *
* * *
* * * *
* * * * *
"""

# for father in range(1, 6):
#   for son in range(1, father+1):
#     print("*", end=' ')
#   print()

"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

# for father in range(6,0,-1):
#   for son in range(1, father):
#     print(son, end=' ')
#   print()


"""
* * * * *
* * * *
* * * 
* * 
* 
"""

# for father in range(6,0,-1):
#   for son in range(1, father):
#     print('*', end=' ')
#   print()


"""
*
* *
* * *
* * * *
* * * * *
* * * * *
* * * *
* * * 
* * 
* 
"""

# for father in range(1, 6):
#   for son in range(1, father+1):
#     print("*", end=' ')
#   print()

# for father in range(6,0,-1):
#   for son in range(1, father):
#     print('*', end=' ')
#   print()


"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

# for father in range(1, 6):
#   for son in range(1, father+1):
#     print(son, end=' ')
#   print()

# for father in range(6,0,-1):
#   for son in range(1, father-1):
#     print(son, end=' ')
#   print()


"""
1
*
1 2
* *
1 2 3
* * *
1 2 3 4
* * * *
1 2 3 4 5
* * * * *
"""

# for father in range(1, 6):
#   for son in range(1, father+1):
#     print(son, end=' ')
#   print()

#   for son in range(1, father+1):
#     print('*', end=' ')
#   print()

"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

# for i in range(1, 6):
#   for j in range(5, i-1, -1):
#     print(j, end=' ')
#   print()

"""
   *
  ***
 *****
*******
"""

# rows = 5

# for i in range(1,rows+1):
#   for j in range(rows-i):
#     print(" ", end='')
#   for k in range(2*i-1):
#     print("*", end='')
#   print()

"""
**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
**********
"""

# outer loop: rows
for i in range(1, 11):
  if(i==1 or i == 10):
    for j in range(1, 11):
      print('*', end='')
  else:
    for k in range(1, 11):
      if(k==1 or k==10):
        print('*', end='')
      else:
        print(' ', end='')
  print()

  #Assignment Problem: 7. Create a diamond pattern of stars with a maximum width of 5 stars