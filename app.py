import time
def add(a, b):
    print(a+b)
    return a + b

def subtract(a, b):
    print(a-b)
    return a - b

def menu():
    print("\n--- Menu-Driven Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")

if __name__ == "__main__":
    while(True):
        add(5,3)
        subtract(5,3)
        time.sleep(10)