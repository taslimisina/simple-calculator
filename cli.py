class CLI:
    def start_cli(self):
        while True:
            print("Simple Calculator")
            print("Please Select Your Operation")
            print("1. Exit")
            operation = input()
            if operation == '1':
                break
        print("Thank You For Using Our Calculator")


if __name__ == '__main__':
    cli = CLI()
    cli.start_cli()