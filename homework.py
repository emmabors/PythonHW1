# Excercise 1
for num in range(1001):
    print(num**3)
    if num >= 10:
        break

print("\n")
# Excercise 2
for num in range(1,101):
    if num == 1:
        continue
    elif num % 2 == 0 and num > 2:
        continue
    elif num % 5 == 0 and num > 5:
        continue
    elif num % 3 == 0 and num >= 9:
        continue
    elif num % 7 == 0 and num >7:
        continue
    else:
        print(num) 

print("\n")
# Excercise 3
age = 18
older = 65
user_age = int(input('How old are you?'))
if user_age < age:
    print('kids')
elif user_age <= older:
    print('adults')
else:
    print('seniors')