import hashlib

puzzle_input = "bgvyzdsv"
#puzzle_input = "abcdef"
not_found = True
added_int = 0

def check_zeros(string):
    zeroes = 0
    #* part 2 :
    #? for i in range(6):
    #* part 1 :
    #? for i in range(5):
        if string[i] == "0":
            zeroes += 1
    #* part 2 :
    #? if zeroes >= 6:
    #* part 1 :
    #? if zeroes >= 5:
        print(string)
        return False
    else:
        return True

while not_found:
    string_to_hash = puzzle_input+str(added_int)
    result = hashlib.md5(string_to_hash.encode())
    not_found = check_zeros(result.hexdigest())
    added_int += 1
print(string_to_hash)