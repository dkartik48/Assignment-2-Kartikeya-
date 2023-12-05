numbers=[4,6,9,12,17,22,27,33,44]
print("LIST: ",numbers )
print("The maximum number in the list: ",max(numbers))
x=numbers[7]
numbers[7]=numbers[8]
numbers[8]=x
print("Last number swapped: ",numbers)

numbers.remove(numbers[8])
print("After removing last one: ",numbers)
y=numbers[6]
numbers[6]=numbers[7]
numbers[7]=y
print("Final LIST: ",numbers)
numbers.sort()
print("SORTED LIST: ",numbers)