# Conditional Statements
# if CONDITION: <--- Condition must be True or False
#     DO SOMETHING
# elif CONDITION_2: <-- Run if CONDITION False
#     DO ANOTHER SOMETHING
# elif CONDITION_3: <-- RUn if CONDITION_N-1 False
#     ETC
# else:
#       DO SOMETHING ELSE <-- Executes when ALL CONDITIONS are False
num = int(input("Enter a numner: "))
if num > 3:
    print(f"{num} is greater than 3!")
elif num == 3:
    print(f"{num} is equal to 3!")
else:
    print(num, "is not greater than 3!")
