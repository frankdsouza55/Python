# Problem Statement: https://edabit.com/challenge/9S8qp4XKG2qwQMdrb

def ways_to_climb(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return ways_to_climb(n-1) + ways_to_climb(n-2)

#Driver Program
n = int(input("Enter Number of stairs: "))
print("Ways to climb => " + str(ways_to_climb(n+1)))