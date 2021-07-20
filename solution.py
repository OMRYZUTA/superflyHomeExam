HOUR_HAND_OFFSET = 30
MINUTE_HAND_OFFSET = 6
TWELVE_BASE = 12
SHARP_ANGLE_OFFSET = 90
OBTUSE_ANGLE_OFFSET = 180
HOUR_END_INDEX = 2
MINUTES_START_INDEX = 3


def get_hour_hand_value(str_hour_hand_value):
    int_representation = int(str_hour_hand_value)
    int_representation %= TWELVE_BASE
    return int_representation * HOUR_HAND_OFFSET


def get_minute_hand_value(str_minute_hand_value):
    int_representation = int(str_minute_hand_value)
    return int_representation * MINUTE_HAND_OFFSET


def get_angle(hour_hand_value, minute_hand_value):
    fixed_hour_value = get_fixed_hour_hand_value(
        hour_hand_value, minute_hand_value/6)
    angle = abs(
        fixed_hour_value-minute_hand_value) % OBTUSE_ANGLE_OFFSET
    if angle > 90:
        angle = abs(angle) - SHARP_ANGLE_OFFSET

    return angle


def get_fixed_hour_hand_value(initial_hour_hand_value, int_representation_of_minute_hand_value):
    return initial_hour_hand_value + int_representation_of_minute_hand_value/2


def solution(str_input):
    hour_hand_value = get_hour_hand_value(str_input[:HOUR_END_INDEX])
    minute_hand_value = get_minute_hand_value(str_input[MINUTES_START_INDEX:])
    return get_angle(hour_hand_value, minute_hand_value)


def main():
    while True:
        str_input =input("please enter the timeq in format HH:MM or q to quit")
        if str_input =='q':
            break
        else:
            print(f"the angle is: {solution(str_input)}")


if __name__ == '__main__':
    main()
