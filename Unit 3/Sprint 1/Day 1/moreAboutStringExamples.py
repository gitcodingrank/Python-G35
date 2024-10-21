#Example:- given list of string filter those string which are starting which J, and make these strings small.

#input - langs = ["Java", "Python", "Javascript", "C", "Php"]
#output - ["java", "javascript"]

langs = ["Java", "Python", "Javascript", "C", "Php"]

# startswith(string) - Do in your assignment and do also for rest of inbuilt function

#count() - to check how many times a character is there in the string.

# str = "hello"
# print(str.count("a"))

# nums = [1,2,3,4,5,5]
# print(nums.count(5))
# print(nums.count(6))


#isalpha() - write own function for below functionality.

# str1 = "abc"
# str2 = "abc123"
# print(str1.isalpha())
# print(str2.isalpha())


#isnumeric() or isdigit() 

# str = "123456"
# print(str.isnumeric())
# print(str.isdigit())

# str = "apple1231"
# print(str.isnumeric())
# print(str.isdigit())

# print(str.isalnum())


#index() - it is used to return the index for particular char in the original string.

# str = "hello world"

# print(str.index('e'))
# print(str.index('ello'))

#find() - it returns index of sequence/char if it is present in the original string else it will return -1

# str = "hello world"

# print(str.find("e"))
# print(str.find("ello"))
# print(str.find("ty"))

#replace(old, new) - it replaces the char/sequence by some new char/sequence and returns new String.


# str = "hello everyone everyone everyone"
# print(str.replace("every", "world"))


#strip() - it removes front and back spaces of the string.

# str = "    hello      "
# print(len(str))
# print(str)
# print(str.strip())
# print(len(str.strip()))

#max() - it returns char according to ASCII value of character.

# str = "hello" 
# print(max(str))
# print(min(str))
