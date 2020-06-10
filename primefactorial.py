def primefac(n):
    while n%2 ==0:
        print 2,
        n=n/2
    for i in range(3,n/2):
            while n%i==0:
                print i,
                n=n/i
    if n>2:
        print n


m=raw_input("Enter a number ")
primefac(int(m))


#Enter a number 1024
#2 2 2 2 2 2 2 2 2 2
#Enter a number 400
#2 2 2 2 5 5
#Enter a number 312
#2 2 2 3 13
