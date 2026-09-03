class Selection_sorter:
  def sorter(self,r):
    for i in range(len(r)-1):
      x=i
      for j in range(i+1,len(r)):
         if r[j].lower()<r[x].lower():
          x=j
      r[i],r[x]=r[x],r[i]
    print(r)
    return
n=int(input("Enter the number of strings:"))
r=[]
for j in range(0,n):
  string=input("Enter a string:")
  r.append(string)
m=Selection_sorter()
m.sorter(r)