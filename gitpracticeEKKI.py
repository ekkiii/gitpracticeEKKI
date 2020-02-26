# Partner 1 Name: Ekki Lu
# Partner 2 Name: Clyde Beuter
###############################
# Assignment Name: GitHub Practice - 2/26/20 - 20 pts

import random as rand

def getNRandom(n):
    '''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
    n_list = []
    for i in range(n):
        n_list.append(rand.randint(1,10))
    return n_list


def multiplyRandom(numbers):
    '''takes in a list of n numbers and returns the product of the numbers'''
    product = 1
    for number in numbers:
        product = int(number) * product
    return product


def main():
    print(multiplyRandom(getNRandom(10)))

if __name__ == "__main__":
    main()
