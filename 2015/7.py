import text_loader as loader

# ? possibilité d'optimisation : trier les inputs par ordre alphabétique après initialisation et avant calcul des valeurs
# $ 46065

puzzle_input = loader.main(7, 2015)


class Wire:
    def __init__(self, name, action, value, source1, source2):
        self.name = name
        self.action = action
        self.value = value
        self.source1 = source1
        self.source2 = source2

    def execute_action(self):
        if self.source1 == "" or self.source2 == "" or self.value != "":
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
            self.or_value(
                check_wire_value(self.source1), check_wire_value(self.source2)
            )
        elif self.action == "AND":
            self.and_value(
                check_wire_value(self.source1), check_wire_value(self.source2)
            )
        elif self.action == "SET":
            self.set_value(self.source1)

    def get(self, attr):
        return eval("self." + attr)

    def r_shift(self, value, shift):
        shift = int(shift)
        added_bits = ""
        for i in range(shift):
            added_bits += "0"
        self.value = added_bits + value[:-shift]

    def l_shift(self, value, shift):
        shift = int(shift)
        added_bits = ""
        for i in range(shift):
            added_bits += "0"
        self.value = value[shift:] + added_bits

    def not_value(self, value):
        final_value = ""
        for number in value:
            if number == "1":
                final_value += "0"
            else:
                final_value += "1"
        self.value = final_value

    def and_value(self, value1, value2):
        final_value = ""
        for i in range(len(value1)):
            if value1[i] == "1" and value2[i] == "1":
                final_value += "1"
            else:
                final_value += "0"
        self.value = final_value

    def or_value(self, value1, value2):
        final_value = ""
        for i in range(len(value1)):
            if value1[i] == "1" or value2[i] == "1":
                final_value += "1"
            else:
                final_value += "0"
        self.value = final_value

    def set_value(self, value):
        if value.isnumeric():
            self.value = dec_to_bin(value)
        else:
            self.value = check_wire_value(self.source1)


def check_wire_value(name):
    if name.isnumeric():
        return dec_to_bin(name)
    for wire in wires:
        if wire.get("name") == name:
            return wire.get("value")


# * 3 = SET, 4 = NOT, 5 = SHIFT / AND / OR
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
    return instructions


def bin_to_dec(value):
    return int(value, 2)


def dec_to_bin(value):
    binary = bin(int(value))[2:]
    if len(binary) < 16:
        for i in range(16 - len(binary)):
            binary = "0" + binary
    return binary


wires = []


print("Circuit initializing...")

for line in puzzle_input:
    instr = parse_instructions(line)
    wires.append(
        Wire(
            instr["destination"],
            instr["action"],
            "",
            instr["source1"],
            instr["source2"],
        )
    )
print("Circuit initialized---")
print("Setting values...")
values_unset = True
while values_unset:
    counter = 0
    wires_set = list()
    values_unset = False
    for wire in wires:
        if wire.get("value") == "":
            counter += 1
            values_unset = True
        else:
            value, name = wire.get("value"), wire.get("name")
            wires_set.append([value, name])
        wire.execute_action()
    print("Unset values :", counter)
print("All values set---")
print("Value of the wire a :", bin_to_dec(check_wire_value("a")))
for wire in wires_set:
    wire[0] = bin_to_dec(wire[0])
