k = 2
n = input("Enter the number of prime numbers to generate: ")
while n>0:              # controls how many numbers are displayed
    for j in range(2,k):
        if k%j == 0:
            break
    else:
        print k
        n=n-1
    k=k+1
