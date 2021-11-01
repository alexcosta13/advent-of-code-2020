filename = "input14.txt"


def numToBit(num):
    bits = []
    coeff = [2 ** i for i in range(35, -1, -1)]
    for c in coeff:
        if num >= c:
            num -= c
            bits.append(1)
        else:
            bits.append(0)
    return bits


def bitToNum(bit):
    num = 0
    coeff = [2 ** i for i in range(35, -1, -1)]
    for b, c in zip(bit, coeff):
        num += int(b) * c
    return num


def mask(num, mask):
    bit = numToBit(num)
    for b, m in enumerate(mask):
        if m == "0":
            bit[b] = 0
        elif m == "1":
            bit[b] = 1
    return bitToNum(bit)


def bitmaksSum(lines):
    currentMask = ["X"] * 36
    memory = {}
    for line in lines:
        instruction, value = line.split(" = ")[0], line.split(" = ")[1]
        if instruction == "mask":
            currentMask = [c for c in value]
        else:
            index = instruction[4:-1]
            memory[index] = mask(int(value), currentMask)
    return sum(memory.values())


def addresses(index, mask):
    bit = numToBit(index)
    for b, m in enumerate(mask):
        if m == "1":
            bit[b] = 1
        elif m == "X":
            bit[b] = "X"
    addresses = [bit]
    while "X" in addresses[0]:
        address = addresses.pop(0)
        next_i = next(i for i, x in enumerate(address) if x == "X")
        a1 = address.copy()
        a1[next_i] = 0
        a2 = address.copy()
        a2[next_i] = 1
        addresses.append(a1)
        addresses.append(a2)
    return addresses


def addressDecoder(lines):
    currentMask = ["X"] * 36
    memory = {}
    for line in lines:
        instruction, value = line.split(" = ")[0], line.split(" = ")[1]
        if instruction == "mask":
            currentMask = [c for c in value]
        else:
            index = instruction[4:-1]
            add = addresses(int(index), currentMask)
            for a in add:
                i = bitToNum(a)
                memory[i] = int(value)
    return sum(memory.values())


if __name__ == "__main__":
    with open(filename) as f:
        input = f.readlines()
    input = [x.strip() for x in input]

    print("First part:", bitmaksSum(input))

    print("Second part:", addressDecoder(input))
