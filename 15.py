def lastIndexOf(l, n):
    try:
        return next(i for i, val in enumerate(reversed(l)) if val == n) + 1
    except:
        return 0


def play(nums, length=2020):
    while len(nums) < length:
        nums.append(lastIndexOf(nums[:-1], nums[-1]))
    print(nums)
    return nums[-1]


def playEfficiently(nums, length=30000000):
    number_to_position = {}
    position_to_number = {}
    for i, n in enumerate(nums[:-1]):
        position_to_number[i] = n
        number_to_position[n] = i
    nextNum = nums[-1]
    for i in range(len(nums), length):
        if nextNum in number_to_position:
            position = number_to_position[nextNum]
            number_to_position[nextNum] = i - 1
            position_to_number[i - 1] = nextNum
            nextNum = i - position - 1
        else:
            number_to_position[nextNum] = i - 1
            position_to_number[i - 1] = nextNum
            nextNum = 0
    return nextNum


if __name__ == "__main__":
    input = [9, 3, 1, 0, 8, 4]
    print("First part:", play(input))

    input = [9, 3, 1, 0, 8, 4]
    print("Second part:", playEfficiently(input))
