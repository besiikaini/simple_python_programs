list = []
number = int(input("Enter the length of the list: "))
print("Enter numbers in the list")
for i in range(number):
 data = int(input())
 list.append(data)
print("Numbers in the list")
print(list)
print("Sorted list")
list.sort()
print(list)