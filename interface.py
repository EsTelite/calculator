class interface:
    from calculator_tooling import tooling
    from arithmetic_operation import arithmetic_operation

    def __init__(self):
        self.init_value = 0
        self.calc_memory = []
        self.operation_tracker = []

    def exit(self):
        """
        This function is used to exit the program.

        Parameters:
            None

        Returns:
            None
        """
        exit(0)

    def neg(self,a):
        """
        This function is used to negate a number.

        Parameters:
            a (float or int): The number to calculate the negate of.

        Returns:
            Int
        """
        return a * -1

    def op_tracker(self, opcode, a=0):
        """
        This function will track the operations performed by the user.
        """
        # If opcode contains repeat then do not track
        if "repeat" in opcode or "cancel" in opcode:
            return
        elif a == 0:
            self.operation_tracker.append(opcode)
        else:
            self.operation_tracker.append(opcode + " " + str(a))

    def cancel(self):
        """
        This function will do the cancel by poping the last operation from the memory
        """
        try:
            self.calc_memory.pop()
        except:
            print("Nothing to cancel")
    

    def validate_input(self, input):
        operations = ["add", "substract", "multiply", "sqrt", "sqr", "cubert", "cube", "repeat"]
        # Handling single string opcode
        if input == "exit" or input == "neg" or input == "cancel" or input == "sqrt" or input == "sqr" or input == "cubert" or input == "cube" or input == "repeat":
            return True
        try:
            input = input.split()
            input_length = len(input)
            # if input[0] contains add, substract, multiply, sqrt, sqr, cubert and cube then check for if input[1] is a number(int,float)
            if input[0] in operations or input[0] == "":
                if len(self.calc_memory) > 1:
                    input[1] = float(input[1])
                    if isinstance(input[1], int) or isinstance(input[1], float):
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False
        except:
            return False

    def get_last_op_result(self):
        if len(self.calc_memory) > 0:
            a = self.calc_memory[-1]
        else:
            a = 0.0
        return a

    def opcode_mapper(self, input):
        # Split opcode from input
        opcode = input.split()[0]
        a = self.get_last_op_result()

        #TODO: Cleaner input handling
        if len(input.split()) > 1:
            b = float(input.split()[1])
        else:
            pass
        if opcode == "exit":
            self.exit()
        elif opcode == "neg":
            a = self.neg(a)
            self.calc_memory.append(a)
        elif opcode == "cancel":
            self.cancel()
        elif opcode == "add":
            a = self.arithmetic_operation.add(a, b)
            self.calc_memory.append(a)
        elif opcode == "substract":
            a = self.arithmetic_operation.subtract(a, b)
            self.calc_memory.append(a)
        elif opcode == "multiply":
            a = self.arithmetic_operation.multiply(a, b)
            self.calc_memory.append(a)
        elif opcode == "sqrt":
            a = self.arithmetic_operation.sqrt(a)
            self.calc_memory.append(a)
        elif opcode == "sqr":
            a = self.arithmetic_operation.sqr(a)
            self.calc_memory.append(a)
        elif opcode == "cubert":
            a = self.arithmetic_operation.cubert(a)
            self.calc_memory.append(a)
        elif opcode == "cube":
            a = self.arithmetic_operation.cube(a)
            self.calc_memory.append(a)
        elif opcode == "repeat":
            self.repeat(b)

    def repeat(self, n):
        """
        This function repeating n previous commands and will be using the last result, and do it until repat command. 
        For example we have op_tracker = [add 5, add 10, multiply 3]
        last_result=10
        so if repeat 2 it will be, 10+10=20, 20*3=60.
        Dunno, maybe this is the idea???
        * Will not be logged in optracker 
        """
        # Get list of opcode that will be executed
        n = int(n)
        opcode = self.operation_tracker[-n:]
        print(opcode)
        for i in range(n):
            self.opcode_mapper(opcode[i])

    def prompt_display(self):
        while True:
            _ = input(">")
            # If input is not valid, prompt again
            if not self.validate_input(_):
                print("Invalid input")
            # Associate with function from calculator tooling and arithmetic operation
            else:
                self.opcode_mapper(_)
                self.op_tracker(_)
                print(self.calc_memory[-1])

