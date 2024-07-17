import text_loader as loader
puzzle_input = loader.main(6,2015)
#* part 1:
#?grid = [[False] * 1000 for i in range(1000)]
grid = [[0] * 1000 for i in range(1000)]

#?def light_action(lights, instruction, x, y):
#?    if instruction == "turn on":
#?        lights[x][y] = True
#?    elif instruction == "turn off":
#?        lights[x][y] = False
#?    elif instruction == "toggle":
#?        lights[x][y] = not lights[x][y]
#?    return lights

#?def count_lights_on(lights):
#?    counter = 0
#?    for line in lights:
#?        for light in line:
#?            if light:
#?                counter += 1
#?    return counter

def light_action(lights, instruction, x, y):
    if instruction == "turn on":
        lights[x][y] += 1
    elif instruction == "turn off":
        if lights[x][y] > 0:
            lights[x][y] -= 1
    elif instruction == "toggle":
        lights[x][y] += 2
    return lights

def count_lights_on(lights):
    counter = 0
    for line in lights:
        for light in line:
            counter += light
    return counter


def parse_instruction(line):
    instr = {}
    instruction = line.split(" ")
    if len(instruction) == 4:
        instr["action"] = instruction[0]
    elif len(instruction) == 5:
        instr["action"] = instruction[0]+" "+instruction[1]
    start = instruction[-3].split(",")
    stop = instruction[-1].split(",")
    instr["startX"] = int(start[0])
    instr["startY"] = int(start[1])
    instr["stopX"] = int(stop[0])
    instr["stopY"] = int(stop[1])
    return instr

def rect_draw(lights, instruction, startX, startY, stopX, stopY):
    for i in range(startX,stopX+1):
        for j in range(startY,stopY+1):
            lights = light_action(lights,instruction,i,j)
    return lights


for line in puzzle_input:
    instructions = parse_instruction(line)
    grid = rect_draw(grid, instructions["action"], instructions["startX"],instructions["startY"],instructions["stopX"],instructions["stopY"])
print(count_lights_on(grid))