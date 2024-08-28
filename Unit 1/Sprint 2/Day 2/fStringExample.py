#F-String: if you want to embed any variable and expression directly into String.

name = "Alice"
age = 45

#Hi, I'm Alice and 45 years old.

#life without f-string
# print("Hi, I'm",name, "and", age, "years old.")

#using f-string
# print(f"Hi, I'm {name} and {age} years old.")

#Good Example: Email

# """
# Dear Rakesh,

# I'm from Masai, where I will teach you about Python Programming Language.

# Best Regards
# Anand Singh Yadav
# """

studentName = input("Enter Student Name:")
teacherName = input("Enter Teacher Name:")
language = input("Enter Programming Language:")
org = input("Enter Organization Name:")

email = F"""
Dear {studentName},

I'm from {org}, where I will teach you about {language} Programming Language.

Best Regards
{teacherName}
"""

print(email)