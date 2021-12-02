input_file = "day_1_input.txt"
lines = (line.rstrip() for line in open(input_file))

prev_number = None
increased = 0

for line in lines:
    number = int(line)
    if prev_number and number > prev_number:
        increased += 1
    prev_number = number

print(increased)
