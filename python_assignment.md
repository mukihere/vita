# python assignment

```python
1)
list1 = [10, 20, 30, 40, 50]
for i in range(4,-1,-1):
    print(list1[i])


2)
s1="Chrisdem"
s2="IamNewString"
newstr=s1[0:3]+s2+s1[3:]
print(newstr)


3)import re

inputStr = "English = 78 Science = 83 Math = 68 History = 65"
markList = [int(num) for num in re.findall(r'\b\d+\b', inputStr)]
totalMarks = 0
for mark in markList:
  totalMarks+=mark
per = totalMarks/len(markList)  
print("Total", totalMarks, "Percentage is ", per)

4)listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
finallist=list()
odd = listOne[1::2]
print(odd)
even = listTwo[0::2]
print(even)
finallist.extend(odd)
finallist.extend(even)
print(finallist)

5)string=input("Enter the string:")

List = string.split()
lower_char_list = []
upper_char_list = []
for char in string:
    if char.islower():
        lower_char_list.append(char)
    else:
        upper_char_list.append(char)
string1 = ''.join(lower_char_list + upper_char_list)
print("arranging characters giving precedence to lowercase letters:"+str(string1))
