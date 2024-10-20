list = [1, 2, 3, 4, 5]
print(list[-1])
list.append(6)
print(list)
list.insert(2, 7)
print(list)
list.pop(2)
print(list)
list.remove(1)
print(list)
list = list + [8, 9, 10]
print(list)
print(len(list))
print(list[1:4])
print(list[:3])
print(list*2)


Ans:
5
[1, 2, 3, 4, 5, 6]
[1, 2, 7, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[2, 3, 4, 5, 6]
[2, 3, 4, 5, 6, 8, 9, 10]
8
[3, 4, 5]
[2, 3, 4]
[2, 3, 4, 5, 6, 8, 9, 10, 2, 3, 4, 5, 6, 8, 9, 10]
