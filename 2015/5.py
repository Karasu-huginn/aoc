import text_loader as loader

puzzle_input = loader.main(5,2015)
examples = ["qjhvhtzxzqqjkmpb","xxyxx","uurcxstgmygtbstg","ieodomkazucvgmuy"] #* nice nice naughty naughty

def double_letter_check(string):  #* returns bool
    for i in range(len(string)):
        if i < len(string)-1:
            if string[i] == string[i+1]:
                return True
    return False

def vowels_check(string):   #* returns bool
    vowels = ["a","e","i","o","u"]
    counter = 0
    for letter in string:
        if letter in vowels:
            counter += 1
    if counter >= 3:
        return True
    else:
        return False

def forbidden_strings_check(string):    #* returns bool
    forbidden_strings = ["ab", "cd", "pq", "xy"]
    for i in range(len(string)):
        if i < len(string)-1:
            if string[i]+string[i+1] in forbidden_strings:
                return True
    return False

#? def twice_double_letters_check(string):
#?     for i in range(len(string)):
#?             for j in range(len(string)):
#?                     if string[j]+string[j-1] == string[i]+string[i-1] and i != j:
#?                     #?if string[i]+string[i+1] in string[:i]+string[i+2:]:
#?                         print("PAIRS : ",string[i]+string[i-1])
#?                         return True
#?     return False

#? def letter_repeat_between(string):
#?     for i in range(len(string)-1,0,-1):
#?         if string[i] == string[i-2]:
#?             return True
#?     return False


def twice_double_letters_check(string):
    for i in range(len(string)):
            for j in range(len(string)):
                    if string[j]+string[j-1] == string[i]+string[i-1] and i != j:
                        print("PAIRS : ",string[i]+string[i-1])
                        return True
    return False

def letter_repeat_between(string):
    for i in range(len(string)):
            if string[i] == string[i-2]:
                print("LETTERS : ",string[i]+string[i-1]+string[i-2])
                return True
    return False

counter = 0
for word in puzzle_input:   #$ puzzle_input
    #* part 1 :
    #? if double_letter_check(word) == True and vowels_check(word) == True and forbidden_strings_check(word) == False:
    if twice_double_letters_check(word) == True and letter_repeat_between(word) == True:
        counter += 1
        print(word,"is nice\n")
        
print(counter)