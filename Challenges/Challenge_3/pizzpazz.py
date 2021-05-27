# This is an attempt at Challenge 3 from Module 0 of static void


for n in range(1,101):
    if (n % 3 == 0) and (n % 5 == 0):
            print("PizzPazz")
    elif (n % 3 == 0):
            print("Pizz")
    elif (n % 5 == 0):
            print("Pazz")
    else:
            print(n)

