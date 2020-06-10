lists=[]
listk=[]
listr=[]
ab=[]
def determinant(matrix):
    n=len(matrix)
    if n==2:
        detera=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        print "Determinant:" +str(detera)
        for i in range (2):
            for j in range(2):
                matrix[i][j]=round((1.0/detera)*matrix[i][j],1)
        print "Inverse: "+ str(matrix)

    elif n==3:
            deter=matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])-matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])+matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
            print "Determinant:" +str(deter)
    else:
        print "Out of scope"


n=int(raw_input("Enter size of matrix: "))
if n==2:
    print "Enter first row:"
    for i in range(n):
        a=int(raw_input())
        lists.append(a)
    print lists
    print "Enter second row:"
    for j in range(n):
        b=int(raw_input())
        listr.append(b)
    print listr
    ab.append(lists)
    ab.append(listr)
    determinant(ab)
elif n==3:
    print "Enter first row:"
    for i in range(n):
        a=int(raw_input())
        lists.append(a)
    print "Enter second row:"
    for j in range(n):
        b=int(raw_input())
        listr.append(b)
    print "Enter Third row:"
    for k in range(n):
        c=int(raw_input())
        listk.append(c)
    ab.append(lists)
    ab.append(listr)
    ab.append(listk)
    determinant(ab)
else:
    print "out of scope"
