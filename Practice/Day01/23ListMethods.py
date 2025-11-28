List = ["Guava",7, "Orange", "Tanuja", True, 90.3]
print(List)
# Output: ['Guava', 7, 'Orange', 'Tanuja', True, 90.3]

List.append("Alekhya") # This method is to add element at the end.
print(List)
# Output: ['Guava', 7, 'Orange', 'Tanuja', True, 90.3, 'Alekhya']

Num = [89,0,6,43,77,2,9,56,90]
Num.sort() # This method to sort in a order.
print(Num)
# Output: [0, 2, 6, 9, 43, 56, 77, 89, 90]

Num.reverse() # to reverse the order of the list
print(Num)
# Output: [90, 89, 77, 56, 43, 9, 6, 2, 0]

Num.insert(3,70 ) # to insert using index numbers
# insert 70 at index 3
print(Num)
# Output : [90, 89, 77, 70, 56, 43, 9, 6, 2, 0]

Val = Num.pop(4)
# pop method will delete element at particular index and returns its value.
print(Val)
# Output: 56
print(Num)
# Output: [90, 89, 77, 70, 43, 9, 6, 2, 0]

Num.remove(0) # removes an element. In this case 0 will be removed.
print(Num)
# Output: [90, 89, 77, 70, 43, 9, 6, 2]