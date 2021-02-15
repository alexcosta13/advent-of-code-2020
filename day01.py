filename="input1.txt"

def findSum(l, total=2020):
    for i in range(0,len(l)):
        for j in range(i,len(l)):
            if(l[i]+l[j]==total):
                return l[i]*l[j]

def findSumThree(l, total=2020):
    for i in range(0,len(l)):
        for j in range(i,len(l)):
            for k in range(i,len(l)):
                if(l[i]+l[j]+l[k]==total):
                    return l[i]*l[j]*l[k]

with open(filename) as f:
    input = f.readlines()
input = [int(x.strip()) for x in input]

print("First part:", findSum(input))

print("Second part:", findSumThree(input))
