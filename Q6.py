def binarysearch(b,target):
        left=0
        right=len(b)-1
        while left<=right:
            mid=(left+right)//2
            if b[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left
n=int(input("Enter a number:"))
hash =[[] for _ in range(10)]
for i in range(n):
    num=int(input("Enter an integer:"))
    idx=num%10
    pos=binarysearch(hash[idx],num)
    hash[idx].insert(pos,num)
print(hash)