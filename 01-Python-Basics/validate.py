import re


email = input("What's your email? ").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")





# username, domain = email.split("@")

# if username and "." in domain:
#     print("valid")
# else:
#     print("invalid")



if re.search(".+@.+\.com", email):
    print("valid")
else:
    print("invalid")