#String Slicing: it is a technique through which you can extract the some portion of the orginal string but it is always in continuous manner.

str = "chitkara"
"""
substrings:
tk
kt- not valid
c
chi
chra - not valid

chitkara substrings: c, ch, chi, chit, chitk, chitka, chitkar, chitkara, h, hi, hit, hitk, hitka, hitkar, hitkara, i, it, itk, itka, itkar, itkara, t, tk, tka, tkar, tkara, k, ka, kar, kara, a, ar, ara, r, ra, a
"""

# for i in range(len(str)):
#     for j in range(i, len(str)):
#         bag = ""
#         for k in range(i, j+1):
#             bag+=str[k]
#         print(bag)


#using string slicing:

# for i in range(len(str)):
#     for j in range(i, len(str)):
#         print(str[i:j+1])


# name = "pablo"

#string slicing: string_name[start:end:step] - by default start - 0, end- end of particular string, step - 1
# print(name[1:len(name):1])
# print(name[1:])
# print(name[:-4:-1])
