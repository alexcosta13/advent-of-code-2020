SUBJECT_NUMBER = 7
DIVISOR = 20201227


def transform_subject_number(subject_number, divisor, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject_number
        value = value % divisor
    return value


def guess_loop_size(subject_number, divisor, public_key):
    value = 1
    loop_size = 0
    while True:
        value *= subject_number
        value = value % divisor
        loop_size += 1
        if value == public_key:
            return loop_size


if __name__ == "__main__":
    public_key_1 = 6930903
    public_key_2 = 19716708

    loop_size_2 = guess_loop_size(SUBJECT_NUMBER, DIVISOR, public_key_2)
    print("First part:", transform_subject_number(public_key_1, DIVISOR, loop_size_2))
