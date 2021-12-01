
def find_depth_increases(measurements):
    total_increases = 0
    for i in range(len(measurements) - 1):
        if measurements[i + 1] > measurements[i]:
            total_increases += 1

    return total_increases

def create_rolling_window(measurements):
    rolling = []
    for i in range(len(measurements) - 2):
        rolling.append(measurements[i] + measurements[i+1] + measurements[i+2])
    return rolling

if __name__ == "__main__":
    test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    num_changes = find_depth_increases(test_input)

    if num_changes == 7:
        print("Good job! Test 1 passes")
    else:
        print("Oops. Found {} changes expected 7".format(num_changes))

    
    rolling_avgs = create_rolling_window(test_input)
    expected_avgs = [607, 618, 618, 617, 647, 716, 769, 792]
    if rolling_avgs == expected_avgs:
        print("Good job! Test 2 passes")
    else:
        print("Oops. {} but expected {}".format(rolling_avgs, expected_avgs))


    num_changes = find_depth_increases(expected_avgs)

    if num_changes == 5:
        print("Good job! Test 3 passes")
    else:
        print("Oops. Found {} changes expected 5".format(num_changes))