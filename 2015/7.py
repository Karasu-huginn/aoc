import text_loader as loader
puzzle_input = loader.main(7,2015)

class Wire:
    def __init__(self, name, action, value, source1, source2):
        self.name = name
        self.action = action
        self.value = value
        self.source1 = source1
        self.source2 = source2
    
    def execute_action(self):
        if self.source1 == "" or self.source2 == "":
            return
        if check_wire_value(self.source1) == "" or check_wire_value(self.source2) == "":
            return
        if self.action == "RSHIFT":
            self.r_shift(check_wire_value(self.source1), self.source2)
        elif self.action == "LSHIFT":
            self.l_shift(check_wire_value(self.source1), self.source2)
        elif self.action == "NOT":
            self.not_value(check_wire_value(self.source1))
        elif self.action == "OR":
            self.or_value(check_wire_value(self.source1, self.source2))
        elif self.action == "AND":
            self.and_value(check_wire_value(self.source1, self.source2))
        elif self.action == "SET":
            self.set_value(self.source1)


    def get_name(self, attr):
        return eval("self."+attr)
    
    def r_shift(self, value, shift):
        self.value = value[-shift:]+value[:-shift]

    def l_shift(self, value, shift):
        self.value = value[shift:]+value[:shift]

    def not_value(self, value):
        final_value = ""
        for number in value:
            if number == "1":
                final_value += "0"
            else:
                final_value += "1"

    def and_value(self, value1, value2):    #todo handle numeral values
        final_value = ""
        for i in range(len(value1)):
            if value1[i] == "1" and value2[i] == "1":
                final_value += "1"
            else:
                final_value += "0"
        self.value = final_value

    def or_value(self, value1, value2):    #todo handle numeral values
        final_value = ""
        for i in range(len(value1)):
            if value1[i] == "1" or value2[i] == "1":
                final_value += "1"
            else:
                final_value += "0"
        self.value = final_value

    def set_value(self, value):
        if value.isnumeric():
            self.value = value
        else:
            self.value = check_wire_value(self.source1)

def check_wire_value(name):
    for wire in wires:
        if wire.get_name() == name:
            return wire.get_value()

#* 3 = SET, 4 = NOT, 5 = SHIFT / AND / OR
def parse_instructions(line):
    instr = line.split(" ")
    instructions = {}
    if len(instr) == 3:
        instructions["action"] = "SET"
        instructions["source1"] = instr[0]
        instructions["source2"] = "*"
        instructions["destination"] = instr[2]
    elif len(instr) == 4:
        instructions["action"] = instr[0]
        instructions["source1"] = instr[1]
        instructions["source2"] = "*"
        instructions["destination"] = instr[3]
    elif len(instr) == 5:
        instructions["action"] = instr[1]
        instructions["source1"] = instr[0]
        instructions["source2"] = instr[2]
        instructions["destination"] = instr[4]
    return instr

def bin_to_dec(value):
    return int(value, 2)

def dec_to_bin(value):
    binary = bin(value)[2:]
    if len(binary) < 16:
        for i in range(16-len(binary)):
            binary = "0"+binary
    return binary


wires = []

for i in range(10):
    wires.append(Wire(chr(97+i),"",str(i),"",""))


print("Circuit initializing...")
for line in puzzle_input:
    instr = parse_instructions(line)
print("Circuit initialized---")
print("Setting values...")
all_values_set = True
while all_values_set:
    all_values_set = False
    for wire in wires:
        if wire.get_value() == "":
            all_values_set = True
        wire.execute_action()
print("All values set---")
print("Value of the wire a :", check_wire_value("a"))