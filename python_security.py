# Asking for input and saving it to a variable in order to pass it to the function when calling it.
username = input("Username: ")
# The def keyword defines the function and inside the brackets is  the params required when calling it
def check(username_):
    # Is alpha num ensures that it is only alphanumeric characters and not symbols like >
    # The Len function checks the lenght (amount of characters) and checks it has equal to 10 or more.
    if username_.isalnum() and len(username_) <= 10:
        # Showing that the username does fit the requirements
        print("Username fits requirements")
    else:
        print("Doesn't fit")
# Calls the function and passes it the input 
check(username)