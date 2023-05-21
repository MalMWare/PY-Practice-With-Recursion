# Write code for algorithm 2 below
def natural_num(num, highest_num):
    if num > highest_num:
        return
    print(num) 
    natural_num(num+ 1, highest_num)

natural_num(1, 10)