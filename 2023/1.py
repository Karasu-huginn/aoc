import text_loader
puzzle_input = text_loader.main(1,2023)
examples = ["hbhxhjjl5twoqxmlprccr5","5vhtctxvjrvftwoone2six","2qvbrsxqsix45threeeight","kkrjgpm2sixeight24","35smnsnzxmdjtsns6sevenonethree","one5sevenfour3","one54","ctrv3hmvjphrffktwothree","eightseven9dnvcqznjvfpreight","9six9qbgcvljfvccdjslspprgonenine","xtwone3four","pfiveqr4sthreetthreeuthree8vwx","a1b2c3d4e5f","treb7uchet"]



numbers = ["1","2","3","4","5","6","7","8","9","0"]
string_numbers = ["one","two","three","four","five","six","seven","eight","nine"]
string_to_int = {"one":"1", "two" : "2","three" : "3","four" : "4","five" : "5","six" : "6","seven" : "7","eight" : "8","nine" : "9"}
final_number = 0
for instruction in puzzle_input:
    add_number = ""
    double_break = False
    for i in range(len(instruction)):
        if instruction[i] in numbers:
            substring = instruction[:i]
            for j in range(len(substring)):
                for string_number in string_numbers:
                    if string_number in substring[j:j+5]:
                        add_number += string_to_int[string_number]
                        double_break = True
                        break
                if double_break:
                    break
            if double_break:
                double_break = False
                break
            add_number += instruction[i]
            break
    for i in range(len(instruction)-1, -1, -1):
        if instruction[i] in numbers:
            for j in range(len(instruction), i, -1):
                for string_number in string_numbers:
                    if string_number in instruction[j:j+5]:
                        add_number += string_to_int[string_number]
                        double_break = True
                        break
                if double_break:
                    break
            if double_break:
                double_break = False
                break
            add_number += instruction[i]
            break
    print(instruction," = ",add_number)
    final_number += int(add_number)
print(final_number)