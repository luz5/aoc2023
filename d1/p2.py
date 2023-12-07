f = open("input.txt", "r")
text_to_num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def find_index(text):
    result = []
    for number in text_to_num:
        if number in text:
            index = text.find(number)
            while index != -1:
                result.append((index, text_to_num[number]))
                index = text.find(number, index + 1)

    result.sort()
    return result

sum = 0
for line in f:
    index_to_number = find_index(line)
    # print(index_to_number)
    num = 0
    for i, c in enumerate(line):
        if c.isnumeric():
            # print(i,c)
            if index_to_number and i > index_to_number[0][0]:
                num += 10 * index_to_number[0][1]
                break
            num += 10 * int(c)
            break
    for i, c in reversed(list(enumerate(line))):
        if c.isnumeric():
            # print(i,c)
            if index_to_number and index_to_number[-1][0] > i:
                num += index_to_number[-1][1]
                break
            num += int(c)
            break
    if index_to_number and num == 0:
        sum += 10*index_to_number[0][1] + index_to_number[-1][1]
    else:
        sum += num
    print(num)
    

print(sum)