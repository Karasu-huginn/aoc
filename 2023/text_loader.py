def main(day, year):
    file = open("python/AoC/"+str(year)+"/puzzle_inputs/"+str(day)+".txt")
    puzzle_input = []
    for line in file:
        puzzle_input.append(line.rstrip())
    return puzzle_input

print(main(1,2023))