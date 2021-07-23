class CLI:

    def get_operands(self):
        print("Input Your First Number:")
        first_num = int(input())
        print("Input Your Second Number:")
        second_num = int(input())
        return first_num, second_num

    def addition_cli(self):
        print("Addition:")
        op1, op2 = self.get_operands()
        #todo use calculator to calculate results

    def subtraction_cli(self):
        print("Subtraction:")
        op1, op2 = self.get_operands()
        #todo use calculator to calculate results

    def multiplication_cli(self):
        print("Multiplication:")
        op1, op2 = self.get_operands()
        #todo use calculator to calculate multiplication

    def reminder_cli(self):
        print("Reminder:")
        op1, op2 = self.get_operands()
        #todo use calculator to calculate reminder

    def start_cli(self):
        while True:
            print("Simple Calculator")
            print("Please Select Your Operation")
            print("1. Addition")
            print("2. subtraction")
            print("3. Multiplication")
            print("5. Reminder")
            operation = input()
            if operation == '1':
                self.addition_cli()
            elif operation == '2':
                self.subtraction_cli()
            elif operation == '3':
                self.multiplication_cli()
            elif operation == '5':
                self.reminder_cli()
        print("Thank You For Using Our Calculator")


if __name__ == '__main__':
    cli = CLI()
    cli.start_cli()