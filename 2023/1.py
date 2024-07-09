import text_loader
puzzle_input = text_loader.main(1,2023)
examples = ["two1abc2three","pfiveqr4sthreetthreeuthree8vwx","a1b2c3d4e5f","treb7uchet"]

numbers = ["1","2","3","4","5","6","7","8","9","0"]
string_numbers = ["one","two","three","four","five","six","seven","eight","nine"]
string_to_int = {"one":"1", "two" : "2","three" : "3","four" : "4","five" : "5","six" : "6","seven" : "7","eight" : "8","nine" : "9"}
final_number = 0
for instruction in examples:
    add_number = ""
    double_break = False
    for i in range(len(instruction)):
        if instruction[i] in numbers:
            for number_in_letters in string_numbers:
                if number_in_letters in instruction[:i]:
                    add_number += string_to_int[number_in_letters]
                    double_break = True
                    break
            if double_break:
                double_break = False
                break
            add_number += instruction[i]
            break
    for i in range(len(instruction)-1, -1, -1):
        if instruction[i] in numbers:
            for number_in_letters in string_numbers:
                if number_in_letters in instruction[i:]:
                    add_number += string_to_int[number_in_letters]
                    double_break = True
                    break
            if double_break:
                double_break = False
                break
            add_number += instruction[i]
            break
    print(add_number)
    final_number += int(add_number)
print(final_number)