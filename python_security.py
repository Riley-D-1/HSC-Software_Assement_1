username = input("Username: ")
def check(username_):
    # Is alpha num ensures that it is only alphanumeric characters and not symbols like >
    if username_.isalnum() and len(username_) <= 10:
        print("Username fits requirements")
    else:
        print("Doesn't fit")
check(username)