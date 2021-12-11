import aocd


def most_common_bit(input, index):  
    bit_count = 0
    for num in input:
        bit_count += 1 if num[index] == "1" else -1
    return "1" if bit_count >= 0 else "0"

def least_common_bit(input, index):
    return "0" if most_common_bit(input, index) == "1" else "1"

def num_bits(input):
    return len(input[0])
    
def oxygen_rating(input):
    for index in range(num_bits(input)):
        bit = most_common_bit(input, index)
        input[:] = filter(lambda num, index=index, bit=bit: num[index] == bit, input)
        if len(input) == 1:
            break
    return int(input[0], 2)

def co2_rating(input):
    for index in range(num_bits(input)):
        bit = least_common_bit(input, index)
        input[:] = filter(lambda num, index=index, bit=bit: num[index] == bit, input)
        if len(input) == 1:
            break
    return int(input[0], 2)
    
if __name__ == "__main__":
    input = aocd.get_input(2021, 3)
    print(oxygen_rating(input.copy()) * co2_rating(input.copy()))        
