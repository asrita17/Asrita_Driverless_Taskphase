n=int(input("Enter a number:"))
hash=[[] for _ in range(10)]
for i in range(n):
    num=int(input("Enter an integer:"))
    idx=num%10
    hash[idx].append(num)
print(hash)