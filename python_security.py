username = input("Username: ")
# Is alpha num ensures that it is only alphanumeric characters and not symbols like >
if username.isalnum() and len(username) <= 10:
    print("Username fits requirements")
else:
    print("Doesn't fit1234")