a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

choice = int(input("Enter your choice from the above given options: "))

if choice == 1:
    result1 = a+b
    print(f"{a} + {b} = {result1}")
elif choice == 2:
    result2 = a-b
    print(f"{a} - {b} = {result2}")
elif choice == 3:
    result3 = a*b
    print(f"{a} * {b} = {result3}")
elif choice == 4:
    try:
        result4 = a/b
        print(f"{a} / {b} = {result4}")
    except ZeroDivisionError as e:
        print("Number cannot be divided by 0")
else:
    print("Invalid choice")
