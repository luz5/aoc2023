f = open("input.txt", "r")

sum = 0
counter = 0
for line in f:
    counter += 1
    num = 0
    for c in line:
        if c.isnumeric():
            num += 10 * int(c)
            sum += 10 * int(c)
            break
    for c in reversed(line):
        if c.isnumeric():
            sum += int(c)
            break
    

print(sum, counter)