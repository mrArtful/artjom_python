# empty = []
# empty = list()

# print(type(empty))
# print(bool(empty))

# filled_lst = [
#     123,
#     123.3213,
#     'Hello world',
#     [1, 2, 3, [4, 5, 6]],
#     False,
# ]

# courses = ['History', 'Math', 'Literature', 'Physics', 'Programming']
# numbers = [1, 5, 6, 8, 3, 4, 2]

# # courses.append('Art')
# # print(courses)

# # print(courses[3])
# # courses.insert(0, 'English')
# # print(courses[3])
# # print(courses)

# # courses.extend(['Art', 'English'])
# # print(courses)

# # courses.remove('Math')
# # print(courses)

# # deleted = courses.pop(1)
# # print(deleted)
# # print(courses)

# # courses.reverse()
# # print(courses)

# # courses.sort(reverse=True)
# # print(courses)

# # print(min(courses))
# # print(max(courses))
# # print(sum(numbers))

# # print(min('hello_world'))

# # print(courses.index('Math', 2))

# # print(' - '.join(courses))
# # x = 'Hello people of planet Earth, are you all ok?'
# # # print(list(x))
# # print(x.split(', '))

# # print([1, 2, 3] + [4, 5, 6])

# # x, y, *z = [1, 2, 3, 4, 5, 6, 7]

# # print(x, y, z)
# # print([10, 20, *z])

# # x = [1, 2, 3]
# # print([10, 20, 30, *x])

# # a = [1, 2, 3]
# # b = a.copy()
# # a += [4, 5, 6]

# # print('A', a, 'B', b)

# courses = ('History', 'Math', 'Literature', 'Physics', 'Programming',)

# print(type(courses))

# print(courses.index('Math'))
# print(courses.count('Physics'))

# empty = (1,)
# print(type(empty))

# x = [1,]

# print(len(x))

# print((1, 2, 3) + courses)

# print(courses[2])

# courses = list(courses)
# courses.insert(2, 'Art')
# courses = tuple(courses)
# print(courses)

courses = {'History', 'Math', 'Literature', 'Physics', 'Programming', 'Math', 'Math', 'Math'}
courses.add('Art')
courses.remove('Math')
deleted = courses.pop()

print(courses)
print(deleted)


set1 = {'Art', 'English', 'Math', 'Programming'}
set2 = {'Art', 'Spanish', 'Math', 'Physics'}

# print(set1.intersection(set2))
# set1.intersection_update(set2)

# print(set1.difference(set2))
# print(set2.difference(set1))

# print(set1.symmetric_difference(set2))

# set3 = {'Art', 'English'}
# print(set3.issubset(set1))
# print(set3.issubset(set2))

# print(set1.issuperset(set3))

# print({1, 2, 3}.union({4, 5, 6}))


x = [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6]

x = list(set(x))

print(x)

y = ['a', 'a', 'b', 'c', 'c', 'c', 'd', 'd']
y = list(set(y))

print(y)