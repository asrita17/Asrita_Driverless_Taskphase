class matrixmultiplication:
    def multiply(m1,m2):
        if len(m1[0])!=len(m2):
            print("not possible")
            return
        res=[]
        for i in range(len(m1)):
            row=[]
            for j in range(len(m2[0])):
                val=0
                for k in range(len(m2)):
                    val+=m1[i][k]*m2[k][j]
                row.append(val)
            res.append(row)
        print(res)
r1=int(input("Enter rows for m1: "))
c1=int(input("Enter columns for m1:"))
m1=[]
for i in range(r1):
    row=[]
    for j in range(c1):
        num=int(input("Enter element:"))
        row.append(num)
    m1.append(row)
r2=int(input("Enter rows for m2:"))
c2=int(input("Enter columns for m2:"))
m2=[]
for i in range(r2):
    row=[]
    for j in range(c2):
        num=int(input("Enter element:"))
        row.append(num)
    m2.append(row)
    m=matrixmultiplication
    m.multiply(m1,m2)