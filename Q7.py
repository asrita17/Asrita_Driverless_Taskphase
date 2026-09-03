def sortedlist(l,ref):
        for r in range(len(l)):
            y=r
            for i in range(r+1,len (l)):
                d1=((l[i][0]-ref[0])**2+(l[i][1]-ref[1])**2)**0.5
                d2=((l[y][0]-ref[0])**2+(l[y][1]-ref[1])**2)**0.5
                if d1<d2:
                    y=i
                l[r],l[y]=l[y],l[r]
        print(l)
n=int(input("Enter the number of points:"))
l=[]
for i in range(n):
            x=int(input("x:"))
            y=int(input("y:"))
            l.append((x,y))
rx=int(input("reference x:"))
ry=int(input("reference y:"))
ref=(rx,ry)
sortedlist(l,ref)