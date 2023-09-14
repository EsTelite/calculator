class interface:
    from calculator_tooling import tooling
    from arithmetic_operation import arithmetic_operation
    def __init__(self):
        init_value = 0

    def main():
        pass

    def test():
        pass

    def validate_input(self,input):
        operations = ["add", "substract", "multiply", "sqrt", "sqr", "cubert", "cube"]
        # Handling single string opcode
        if input == "exit" or input == "neg" or input == "cancel" or input == "":
            return True
        try:
            input = input.split()
            # if input[0] contains add, substract, multiply, sqrt, sqr, cubert and cube then check for if input[1] is a number(int,float)
            if input[0] in operations or input[0] == "":
                if isinstance(input[1], int) or isinstance(input[1], float):
                    return True
                else:
                    return False
            else:
                return False
        except:
            print("Invalid input")
            return False

        # Split input into a list from string separated by space
        



    def prompt_display(self):
        _ = input(">")
        # If input is not valid, prompt again
        if not self.validate_input(_):
            print("Invalid input")
            self.prompt_display()
        print("lolot")
        # Associate with function from calculator tooling and arithmetic operation

obj = interface()
obj.prompt_display()