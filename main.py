from typing import List, Tuple
import math

class Calculator:
    def __init__(self):
        self.history: List[Tuple[str, float]] = []

    def add(self, a: float, b: float) -> float:
        result = a + b
        self.history.append((f"{a} + {b}", result))
        return result

    def subtract(self, a: float, b: float) -> float:
        result = a - b
        self.history.append((f"{a} - {b}", result))
        return result

    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self.history.append((f"{a} × {b}", result))
        return result

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self.history.append((f"{a} ÷ {b}", result))
        return result

    def power(self, a: float, b: float) -> float:
        result = math.pow(a, b)
        self.history.append((f"{a} ^ {b}", result))
        return result

    def show_history(self) -> None:
        if not self.history:
            print("\nNo calculations performed yet.")
            return
        print("\nCalculation History:")
        for i, (operation, result) in enumerate(self.history, 1):
            print(f"{i}. {operation} = {result}")

def get_number_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def display_menu() -> None:
    print("\n=== Calculator Menu ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Show History")
    print("7. Exit")

def main():
    name = input("Please enter your name: ")
    print(f"Hello, {name}! Welcome to the enhanced calculator.")
    
    calc = Calculator()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == "7":
            print(f"\nGoodbye, {name}! Thanks for using the calculator.")
            break
            
        if choice == "6":
            calc.show_history()
            continue
            
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice. Please try again.")
            continue
            
        a = get_number_input("Enter first number: ")
        b = get_number_input("Enter second number: ")
        
        try:
            if choice == "1":
                result = calc.add(a, b)
                print(f"Result: {result}")
            elif choice == "2":
                result = calc.subtract(a, b)
                print(f"Result: {result}")
            elif choice == "3":
                result = calc.multiply(a, b)
                print(f"Result: {result}")
            elif choice == "4":
                result = calc.divide(a, b)
                print(f"Result: {result}")
            elif choice == "5":
                result = calc.power(a, b)
                print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except OverflowError:
            print("Error: Result is too large to compute!")

if __name__ == "__main__":
    main() 