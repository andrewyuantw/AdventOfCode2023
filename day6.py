input2_time = [7,15, 30]
input2_distance = [9, 40, 200]

input_time = [62,64,91,90]
input_distance = [553,1010,1473,1074]

# Part 1

total = 1
for i in range(len(input_time)):
    time = input_time[i]
    count = 0
    for holding_time in range(time + 1):
        time_moving = time - holding_time
        moved = time_moving * holding_time
        if moved > input_distance[i]:
            count += 1
    total *= count

print(total)
