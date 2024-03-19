from validator_collection import validators

email = input("Enter your email: ")

try:
    checkedemail = validators.email(email, allow_empty = True)
    var = (email == checkedemail)
    print(var)
except ValueError:
    print("Invalid email")


