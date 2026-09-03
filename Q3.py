class binarysearch:
    def binarysearch(self,b):
        string=input("Enter the string:")
        left=0
        right=len(b)-1
        while left<=right:
            mid=(left+right)//2
            if b[mid].lower()==string.lower():
                print("String found in index:",mid)
                return
            elif b[mid].lower()<string.lower():
                left=mid+1
            else:
                right=mid-1
        print("String not found in the list")
        
n=int(input("Enter a number:"))
b=[]
for i in range(0,n):
            string1=input("Enter a string:")
            b.append(string1)      
for r in range(len(b)-1):
    y=r
    for i in range(r+1,len(b)):
        if b[i].lower()<b[y].lower():
            y=i
        b[r],b[y]=b[y],b[r]
print(b)
s=binarysearch()
s.binarysearch(b)