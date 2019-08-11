import sys
lists = []
write_file = open('output.txt', 'w')
class LCD:
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2
        #print(s1,s2)

    def solve(self):
        a = [ [ 0 for y in range(len(self.s2)+1) ] for x in range(len(self.s1)+1) ]
        k=0
        for x in range(len(self.s1)):
            for y in range(len(self.s2)):
                d = 1 if self.s1[x]==self.s2[y] else 0
                a[x+1][y+1] = max(
                        a[x][y]+d,
                        a[x][y+1],
                        a[x+1][y]
                        )



        print(a[-1][-1])
	write_file.write(str(a[-1][-1])+"\n")
        self.p(a,len(self.s1),len(self.s2))

	
    def p(self,a,i,j):
	stra = ''
        if i<0 or j<0:
            return
        if a[i][j]>a[i-1][j] and a[i][j]>a[i][j-1]:
            self.p(a,i-1,j-1)
	    #print self.s1[i-1]
	    lists.append(self.s1[i-1])	
        else:
            if a[i-1][j]>a[i][j-1]:
                self.p(a,i-1,j)
            else:
                self.p(a,i,j-1)
def read_input(files):
    list1=files.read().splitlines()
    LCD(list1[0],list1[1]).solve()
    #print list1

filename=sys.argv[1]
files=open(filename,'r');
read_input(files)
str1 = ''
for i in lists:
	str1=str1+i
print str1
write_file.write(str1)
write_file.close()

