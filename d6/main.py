import math

def find_ways(time, record):
    start = -1
    end = -1
    for i in range(time):
        if i*(time-i) > record:
            start = i
            end = i
            break
    for i in reversed(range(time)):
        if i*(time-i) > record:
            end = i
            if start > end:
                Warning("Something is wrong")
            break
    print(start, end)
    if -1 in (start, end):
        return 0  
    return (end-start) + 1

f = open("input.txt")
time_list = []
record_list = []
for line in f:
    if line.startswith("Time"):
        time_list_str = line.strip("Time:").strip().split()
        time_list = [int(x) for x in time_list_str]
    if line.startswith("Distance:"):
        record_list_str = line.strip("Distance:").strip().split()
        record_list = [int(x) for x in record_list_str]
print(time_list, record_list)
ways_list = []
for i in range(len(time_list)):
    ways_list.append(find_ways(time_list[i], record_list[i]))
print(math.prod(ways_list))
time = int("".join(time_list_str))
record = int("".join(record_list_str))
print(find_ways(time, record))
