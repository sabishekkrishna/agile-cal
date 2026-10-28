def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def menu():
    print("\n--- Menu-Driven Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter choice (1-3): ")
        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice")