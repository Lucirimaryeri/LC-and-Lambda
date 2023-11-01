''' 1) ------------------------------------------------------------------------------------------
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
original_list = [1,2,3,4,5,6,7,8,9,10]
Even = list(filter(lambda x: x % 2 == 0, original_list))
Odd = list(filter(lambda x: x %2 != 0, original_list))
print(Even)
print(Odd)
print()


''' 2) ------------------------------------------------------------------------------------------
find which days of the week have exactly 6 characters.
'''
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = list(filter(lambda day: len(day) == 6, weekdays))
print(days)
print()


''' 3) ------------------------------------------------------------------------------------------
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
og_list = ['orange', 'red', 'green', 'blue', 'white', 'black']
remove = ['orange', 'black']
remove_words = list(filter(lambda word: word not in remove, og_list))
print(remove_words)
print()


''' 4) ------------------------------------------------------------------------------------------
remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
remove = list(filter(lambda x: x not in list2, list1))
print(remove)


''' 5) ------------------------------------------------------------------------------------------
find the elements of a given list of strings that contain specific substring using lambda
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
print()
#original list
c_list = ['red', 'black', 'white', 'green', 'orange']
#substring to search
search = 'ack'
#filter
result = list(filter(lambda x: search in x, c_list))
#print
print("Original list: ", c_list)
print("Substring search ", search)
print("Elements of the list that contains substring: ", result)
print()

''' 6) ------------------------------------------------------------------------------------------
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''
'''''
str1 = "Hello8world" #should not fail
str1 = "HELLO" #should fail
str1= "hello" #should fail

#also look at the function any
'''
#you can also use liist comprehension

check_password = lambda password: all([
    any(char.isupper() for char in password),
    any(char.islower() for char in password),
    any(char.isdigit() for char in password),
    len(password)>=8
])

str1 = "Hello8world" 
print(check_password(str1))
str2 = "HELLO" 
print(check_password(str2))
str3= "hello" 
print(check_password(str3))


''' 7) ------------------------------------------------------------------------------------------
Write a Python program to sort a list of tuples using Lambda.
# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
# Original list of tuples: 
print()
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

#sorting 
sorted_scores = sorted(original_scores, key=lambda x: x[1])
print("Original list: ", original_scores)
print("Sorted List: ", sorted_scores)