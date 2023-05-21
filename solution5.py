# Write code for algorithm 5 below
def pala(word):

    if len(word) < 2:
        return True

    else:
        if word[0] == word[-1]:
            return pala(word[1:-1])
        else: 
            return False

print(pala("racecar"))