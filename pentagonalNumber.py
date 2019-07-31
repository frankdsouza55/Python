# Problem Statement: https://edabit.com/challenge/st8mDxreMcuWxuz8c

def pentNum(n):
    if(n==1):       #Base case
        return 1
    return 5*(n-1) + pentNum(n-1)

#Driver program
num=int(input("Enter number of iterations: "))
print("pentagonal("+str(num)+") => "+str(pentNum(num)))
