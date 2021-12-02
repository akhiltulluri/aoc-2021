input_file = "day_1_input.txt"
lines = (line.rstrip() for line in open(input_file))

increased = 0


def three_measurement_window_generator():
    window = []

    for line in lines:
        window.append(int(line))
        if len(window) == 3:
            yield window
            window = [window[1], window[2]]


prev_window = None

for window in three_measurement_window_generator():
    if prev_window and sum(window) > sum(prev_window):
        increased += 1
    prev_window = window

print(increased)
