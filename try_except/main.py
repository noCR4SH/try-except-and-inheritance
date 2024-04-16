import sys


while True:
    try:
        user_input = int(input("Provide a birth year: "))
    except ValueError:
        print("\nYou need to provide a number!\n")
    except Exception as e:
        print(f"Program failed! Reason: {e}")
        sys.exit(1)
    else:
        print("This works fine!")
        break
    finally:
        print("This works no matter what!")

age = 2024 - user_input


print(f"Your age is: {age}")