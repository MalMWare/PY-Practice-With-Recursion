# Write code for algorithm 4 below
def power(a, b):
    #return a ** b
    #print(power(a, b))
    if b <= 1: 
        return a
    return a * power(a, b-1)

for i in range(10)
    print(power(i, i))