def last_index_of(l, n):
    try:
        return next(i for i, val in enumerate(reversed(l)) if val == n) + 1
    except:
        return 0


def play(nums, length=2020):
    while len(nums) < length:
        nums.append(last_index_of(nums[:-1], nums[-1]))
    print(nums)
    return nums[-1]


def play_efficiently(nums, length=2020):
    number_to_position = {}
    position_to_number = {}
    for i, n in enumerate(nums[:-1]):
        position_to_number[i] = n
        number_to_position[n] = i
    next_num = nums[-1]
    for i in range(len(nums), length):
        if next_num in number_to_position:
            position = number_to_position[next_num]
            number_to_position[next_num] = i - 1
            position_to_number[i - 1] = next_num
            next_num = i - position - 1
        else:
            number_to_position[next_num] = i - 1
            position_to_number[i - 1] = next_num
            next_num = 0
    return next_num


if __name__ == "__main__":
    input = [9, 3, 1, 0, 8, 4]
    print("First part:", play_efficiently(input))

    input = [9, 3, 1, 0, 8, 4]
    print("Second part:", play_efficiently(input, length=30000000))
