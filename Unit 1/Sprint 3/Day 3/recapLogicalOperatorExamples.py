membership = input("Enter Membership(non-member/member): ")
amount = int("Enter Amount: ")

if membership == "member" and amount >100:
    print("Eligible for Discount")
elif membership =="non-member" and amount>200:
    print("Eligible for Discount")
else:
    print("Not Eligible for Discount")

#other best solution

if (membership == "member" and amount >100) or (membership =="non-member" and amount>200):
    print("Eligible for Discount")
else:
    print("Not Eligible for Discount")