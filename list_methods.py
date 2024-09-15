#example 1
number = [3,5,4,2,3]
number.append(20)
print(number)

#example 2
number = [3,5,4,2,3]
number.insert(0,20)
print(number)

#example 3
number = [3,5,4,2,3]
number.remove(5)
print(number)

#example 4
number = [3,5,4,2,3]
number.pop
print(number)

#example 5
number = [3,5,4,2,3]
number.index(2)
print(number)

#example 6
numbers = [3,5,4,2,3]
print(numbers.index(2))

#example 7
numbers = [3,5,4,2,3]
print(numbers.count(3))

#example 8
numbers = [3,5,4,2,3]
print(3 in numbers)

#example 9
number = [3,5,4,2,3]
number.sort()
print(number)

#example 10
numbers = [3,5,4,2,3]
numbers.sort()
numbers.reverse()
print(numbers)

#example 11
numbers = [3,5,4,2,3,4,6]
unique = []
for number in numbers:
 if number not in unique:
    unique.append(number)
    print(unique)