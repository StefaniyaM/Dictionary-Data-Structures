# Dict items are key value pairs enclosed in curly brackets {}
# Dict is ordered as of Python 3.7 onwards
# Dict is mutable
# Dict keys are unique , cannot have duplicates
# Elements can be of different data types

'''
Dict Attributes
'''

# print(dir(dict))
# print(help(dict.pop))


'''
Creating Python Dictionary
'''

dict_example = {}
# print(dict_example)
# print(type(dict_example))

# # dict_example = {'name': 'Kingsley', 'age': 37 }
# dict_example = dict([(1, 'car') , (2, 'bicycle')])
# print(dict_example)
# # => If we do not put dict before the brackets and print it, it becomes list of tuples.


'''
Access Dictionary Values
'''

# students = {'name': 'Kingsley', 'age': 37}
# print(students['name'])
# print(students['age'])
# print(students.keys())
# print(students.values())

# students = [{'name': 'Kingsley', 'age': 37}, {'name': 'Lisa', 'age': 34}]
# print(students[0]['age'])
# print(students[1]['name'])
 
# for i in range(len(students)):
#     print(students[i]['age'])


# => that is a way of reading Values


'''
Changing Dictionary Elements
'''

# students = {'name': 'Kingsley', 'age': 37}
# students['age'] = 35
# print(students)
# =======================


# students = {'name': 'Kingsley', 'age': 37}
# students.update({'name': 'Jennifer', 'age': 30})
# print(students)
 
#  ===================

# students = {'name': 'Kingsley', 'age': 37}
# students.setdefault('name', 'Steve')
# students.setdefault('subject', 'Python')
# students.setdefault('subject', 'English')
# print(students)

'''
Remove Elements from Dictionary
'''

# students = {'name': 'Kingsley', 'age': 37}
# students.pop('name')
# print(students)

# ============================

# students = {'name': 'Kingsley', 'age': 37}
# students.popitem()
# print(students)

# =============================

# students = {'name': 'Kingsley', 'age': 37}
# students.clear()
# print(students)

# ==============================

# students = {'name': 'Kingsley', 'age': 37}
# del students
# print(students)

'''
Dictionary Membership Test
'''

# students = {'name': 'Kingsley', 'age': 37}

# print('name' in students)
# print('age' not in students)
# print('ages' in students)



fruits = ("orange", "apple", "pear")
print( "orange" in fruits )