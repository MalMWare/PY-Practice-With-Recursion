# Write code for algorithm 1 below
def print_num(n):
    #base case
    if n == 0 :
        return
        #recusive case
    print(n)
    print_num(n-1)

print_num(10)