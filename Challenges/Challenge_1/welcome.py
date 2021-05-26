# This is my attempt at Satic Void's first challenge, to create a program that helps point people to the correct rooms

# Asking user for their name
name = input("Please enter your name: ")

# Welcomgin user and asking where they want to go
destination = input(f"Welcome, {name}! Where would you like to go? (Cafeteria, Office, Playground, Restroom): ")

# Giving directions based off users input for where they want to go
if destination == "Playground":
    # Asking user for their age if they say they want to go to the Playground
    age = int(input("Please confirm your age: "))
    if age > 11:
    # Based on their given age, the an appropriate message is displayed
        print("You do not meet the age restrictions for our playground. Sorry!")
    else:
        print("Our Playground is back out the main door and around the side.")
elif destination == "Cafeteria":
    print("The Cafeteria is straight ahead at the end. Enjoy!")
elif destination == "Office":
    print("The office is up the stairs and to the left")
elif destination == "Restroom":
    print("The Restroom is down the hall and to the right before the cafeteria")
else:
    print("Sorry, I don't know where that is.")

