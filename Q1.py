n=int(input("Enter the number of strings:"))
string_list=[]
for i in range(n):
  string_list.append(input("Enter a string:"))
Count={}
for string in string_list:
  for char in string.lower():
    if char.isalpha():
      Count[char]=Count.get(char,0)+1
print("Frequency dictionary",Count)