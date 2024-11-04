#Problem: Given a string, your task is to find out the count of particular character.


# str = "apple"
#find out the count of 'p'

#Solution 1:

# count = 0

# for char in str:
#     if char=='p' or char == 'P':
#         count+=1

# print(count)


#Solution 2:

# count = 0

# for char in str:
#     if char in ('p','P'):
#         count+=1

# print(count)

#Solution 3:

# print(sum([1 for char in str if char in ["p","P"]]))


# #Solution 4:

# print(str.lower().count('p'))


#Good Problem 1: Given a string, your task is to reverse each word in the string.

#input str = "hello world"
#output = "olleh dlrow"

#Solution 1:

# str = "hello world"

# for word in str:
#     print(reversed(word), end=" ")



# #Solution 2:
# str = "hello world"

# for word in str:
#     print(word[::-1], end=" ")


# #Shorthand Way of above two solutions:

# str = "hello world"

# print([word[::-1] for word in str.split()])
# print([reversed(word) for word in str.split()])

# print(list(map(lambda word: word[::-1], str.split())))

# Try using reduce 

#Good Problem 2: Given a string, your task is to find out the number of vowel and consonant in the following format.

#input - str = 'apple'
#output - {"vowels":2, "consonant":3}

# str = 'apple'
# vowelCount = 0
# consonantCount = 0
# for char in str:
#     if char in 'aeiou':
#         vowelCount+=1
#     if char not in 'aeiou':
#         consonantCount+=1

# print({'Vowels':vowelCount, 'Consonants':consonantCount})


print({char: str.count(char) for char in set(str)})


#Good Problem 3: Given a string, your task is to find out the freequency of each character in the string.

# str = "apple"

# nums = [1,2,3,4,3,2,32,3,4]

# #Solution 1: 
# charFrequency = {}

# for char in nums:
#     charFrequency[char] = charFrequency.get(char, 0) + 1

# print(charFrequency)


#Good Problem 4: Given a string, your task is to find out the freequency of each word in the string.

#str = "hello world hello world hello hello"