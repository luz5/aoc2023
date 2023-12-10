def find_sum(engine: list[str]) -> int:
    checked = []
    result = 0
    for row in range(len(engine)):
        for column in range(len(engine[0])):
            char:str = engine[row][column]
            if char.isnumeric() or char == ".":
                continue
            else:
                result += sum(check_part_num(checked, engine, (row, column)))
    return result

def check_part_num(checked: list[tuple], engine:list[str], symbol: tuple, local_checked_mode: bool = False) -> list[int]:
    numbers = []
    if local_checked_mode:
        checked = []
    check_direction = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    for direction in check_direction:
        row = symbol[0] + direction[0]
        column = symbol[1] + direction[1]
        char:str = engine[row][column]
        if char.isnumeric() and (row, column) not in checked:
            checked.append((row, column))
            #find start
            start = column-1
            while start>=0 and engine[row][start].isnumeric():
                checked.append((row, start))
                start -=1
            #find end
            end = column+1
            while end < len(engine[0]) and engine[row][end].isnumeric():
                checked.append((row, end))
                end +=1
            #print(int(engine[row][start+1:end]))
            numbers.append(int(engine[row][start+1:end]))
    return numbers

def find_gear_ratio(engine: list[str]) -> int:
    checked = []
    result = 0
    for row in range(len(engine)):
        for column in range(len(engine[0])):
            char:str = engine[row][column]
            if char == "*":
                numbers = check_part_num(checked, engine, (row, column), local_checked_mode=True)
                #print(numbers)
                if len(numbers) == 2:
                    result += numbers[0] * numbers[1]
    return result

f = open("test.txt", "r")  
engine = []
for line in f:
    engine.append(line.strip("\n"))
print(find_sum(engine=engine))
print(find_gear_ratio(engine=engine))