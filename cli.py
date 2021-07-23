from Calculator import Calculator


class CLI:
    def __init__(self):
        self.calculator = Calculator()

    def get_operands(self):
        print("Input Your First Number:")
        first_num = int(input())
        print("Input Your Second Number:")
        second_num = int(input())
        return first_num, second_num

    def addition_cli(self):
        print("Addition:")
        op1, op2 = self.get_operands()
        print("Result:")
        print(self.calculator.add(op1, op2))

    def subtraction_cli(self):
        print("Subtraction:")
        op1, op2 = self.get_operands()
        print("Result:")
        print(self.calculator.sub(op1, op2))

    def multiplication_cli(self):
        print("Multiplication:")
        op1, op2 = self.get_operands()
        print("Result:")
        print(self.calculator.multiply(op1, op2))

    def division_cli(self):
        print("Division:")
        op1, op2 = self.get_operands()
        print("Result:")
        print(self.calculator.division(op1, op2))

    def reminder_cli(self):
        print("Remainder:")
        op1, op2 = self.get_operands()
        print("Result:")
        print(self.calculator.reminder(op1, op2))

    def power_cli(self):
        print("Power:")
        op1, op2 = self.get_operands()
        print("Result:")
        print(self.calculator.pow(op1, op2))

    def start_cli(self):
        print("Simple Calculator")
        while True:
            print()
            print("Please Select Your Operation")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Remainder")
            print("6. Power")
            print("10. Exit")
            operation = input()
            if operation == '1':
                self.addition_cli()
            elif operation == '2':
                self.subtraction_cli()
            elif operation == '3':
                self.multiplication_cli()
            elif operation == '4':
                self.division_cli()
            elif operation == '5':
                self.reminder_cli()
            elif operation == '6':
                self.power_cli()
            elif operation == '10':
                break
        print("Thank You For Using Our Calculator")


if __name__ == '__main__':
    cli = CLI()
    cli.start_cli()