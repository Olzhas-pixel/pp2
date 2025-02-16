def asd(N):
    for i in range(N+1):
        yield i**2
a=int(input("give \n"))
for i in asd(a):
    print(i, end=" ")
