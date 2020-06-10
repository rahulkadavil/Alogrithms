#function to determine gcd
def gcd(a,b):
    r=a%b
    q=a/b
    if r==0:
        return b
    else:
        return gcd(b,r)
m = input("Enter a number ")
n = input("Enter another number ")
if m>n:
    k=gcd(m,n)
    print "gcd(%s,%s)" %(m,n) + "is "+ str(k)
elif m==n:
    print "gcd(%s,%s)" %(m,n) + "is "+ str(m)
else:
    k=gcd(n,m) #calling gcd function
    print "gcd(%s,%s)"  %(n,m) + "is " + str(k)


#SAMPLE OUTPUTS
#Enter a number 1024
#Enter another number 10
#gcd(1024,10)is 2
#Enter a number 10
#Enter another number 180
#gcd(180,10)is 10
#Enter a number 123
#Enter another number 16
#gcd(123,16)is 1
