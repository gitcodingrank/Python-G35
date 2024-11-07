#Problem: Sort the following number list in descending order using Selection sort Algorithm.

numList = [5,6,1,7,4,9,0]


#Selection sort
for i in range(len(numList)-1): #n
    biggerIndex = i
    for j in range(i+1, len(numList)): #n*n
        if numList[j] > numList[biggerIndex]:
            biggerIndex = j
    numList[i] , numList[biggerIndex] = numList[biggerIndex], numList[i]

print(numList)

#Time Complexity for Selection Sort is O(n^2)


