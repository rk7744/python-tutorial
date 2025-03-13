# 16. Menu-driven program.
def menu():
    while True:
        print("1. Check even or odd")
        print("2. Check if number is positive, negative, or zero")
        print("3. Generate factors of a number")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            num = int(input("Enter number: "))
            print("Even" if num % 2 == 0 else "Odd")
        elif choice == '2':
            num = float(input("Enter number: "))
            if num > 0: print("Positive")
            elif num < 0: print("Negative")
            else: print("Zero")
        elif choice == '3':
            num = int(input("Enter number: "))
            print([i for i in range(1, num + 1) if num % i == 0])
        elif choice == '4':
            break

menu()