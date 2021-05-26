# Loops
# Useful for doing repeated actions

# While SOME CONDITION IS TRUE:
#       DO SOMETHING
# else: <-- Optional
#       OTHERWISE DO THIS

# Print numbers 1 to 100
n = 1

while n <= 100:
    print(n)
    if n % 2 == 0:
        print("Even!")
    else:
        print("Odd!")
    n = n + 1
else:
    print("It's done")
