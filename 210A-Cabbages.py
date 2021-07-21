N,A,X,Y = map(int,input().split())

if N <= A:
    price = N*X
if N > A:
    price = (A*X)+((N-A)*Y)

print(price)
