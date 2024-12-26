class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if (y == 0):
            print("Error: Denominator should not be '0'")
        else:
            return x / y

    def modulus(self, x, y):
        if (y == 0):
            print("Error: Denominator should not be '0'")
        else:
            return x % y

def main():
    cal = Calculator()

    while True:
        print("\n***************************")
        print("Simple Calculator App:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Remainder")
        print("6. Exit")
        print("***************************\n")

        choice = input("Enter your choice: ")

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number (num1): "))
                num2 = float(input("Enter second number (num2): "))

                if (choice == '1'):
                    result = cal.add(num1, num2)
                    print(f"\nResult:\nAddition of {num1} and {num2} = {result}")
                elif (choice == '2'):
                    result = cal.subtract(num1, num2)
                    print(f"\nResult:\nSubtraction of {num1} and {num2} = {result}")
            except ValueError:
                print("Invalid Choices!!!")
        else:
            print("Invalid Choices!!!")


if __name__ == '__main__':
    main()    