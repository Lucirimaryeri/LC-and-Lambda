#List comprehensions provide a concise way to create lists. 
# It consists of brackets containing an expression followed by a for clause, then
    #zero or more for or if clauses. The expressions can be anything, meaning you can
    #put in all kinds of objects in lists.
# The result will be a new list resulting from evaluating the expression in the
    #context of the for and if clauses which follow it. 
# The list comprehension always returns a result list. '''


''' #this is the same as line 22 but that is more efficient
new_list = [x,y,z,....]
for i in original_list:
    if filter(i):
        result = expression(i)
        new_list.append(result)  '''

# You can obtain the same thing using list comprehension:
# new_list = [expression(i) for i in original_list if filter(i)]
#The list comprehension starts with a '[' and ']', to help you remember that the
#result is going to be a list.
#There are 3 parts to list comprehension:
#*result*  = [*transform/expression*    *iteration*         *filter*     ]
#The filter part answers the question if the item should be transformed.

'''
# making a list 0-10 --------------------------------------------------------------
x = [i for i in range(10)]
print(x)

# Add an expression ---------------------------------------------------------------
squares = [x**2 for x in range(10)]
print(squares)

list1 = [3,4,5]
# multiply
multiplied = [item*3 for item in list1]
print(multiplied)

# List of words -------------------------------------------------------------------
listOfWords = ["this", "is", "a", "list", "of", "words"]
result = [word[0].upper for word in listOfWords] #iterator is word
print(result)

# adding in an IF condition: ------------------------------------------------------
# get the square of every nnumber from 0-10
result = [i*i for i in range(1,11) if i % 2 == 0] # % remainder after division
print(result)

# Taking numbers out of strings
string = "Hello 1234 World"
numbers = [int(x) for x in string if x.isdigit()] #add int to make string result into a digit/integer
print(numbers)
#-----------------------------------
numbers = []
for x in string:
    if x.isdigit():
        y = int(x)
        numbers.append(y)

print(numbers)

#Create a new list------------------------------------------------------------------
list1 = list(range(1,21))
print(list1)

#traditional way -------------------------------------------------------------------
list2 = []
for x in list1:
    if x%2== 0:
        y = x * 100
        list2.append(y)

print(list2)

# new way -------------------------------------------------------------------------
list2 = [x*100 for x in list1 if x%2 ==0]
print(list2)

#create a new list of all odd numbers multiplied by 100-----------------------------
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

list2 = []
for x in list1:
    if x%2 == 1:
        y = x * 100
        list2.append(y)

print(list2)

list2 = [x*100 for x in list1 if x%2==1]

print(list2)

# test.txt exercise ----------------------------------------------------------------
infile = open('test.txt', 'r')
result = [i.rstrip('\n') for i in infile if "line3" in i]
print(result)

#-----------------------------------------------------------------------------------
def double(x):
    return x*2

print(double(10))
result = [double(x) for x in range(10) if x%2 == 0] #the x%2 is if it is an even numvber conditionn
print(result)

result = [x+y for x in [10,30,50] for y in [20,40,60]]
print(result)

'''

## Exercise ## -----------------------------------------------------------------------------------

# 1 Using a list comprehension, create a new list called "newlist" out of the list "numbers", 
# which contains only the positive numbers from the list, as integers.
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x > 0]
print(newlist)
print()


## 2 create a list of integers which specify the length of each word in --------------------------
## a sentence except for the word 'the'

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
list = [len(word) for word in words if word != 'the']
print(list)
print()


## Given dictionary is consisted of vehicles and their weights in kilograms. --------------------- 
## Contruct a list of the names of vehicles with weight below 5000 kilograms. 
## In the same list comprehension make the key names all upper case.

dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, 
"Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

cars = [vehicle.upper() for vehicle, weight in dict.items() if weight < 5000]
print(cars)
print()


# Find all the numbers from 1 to 1000 that have a 4 in them --------------------------------------
num = [i for i in range(1,1001) if '4' in str(i)]
print(num)

# count how many times the word 'the' appears in the text file - 'sometext.txt' ------------------

print()
text = open('sometext.txt', 'r')
words = text.read().split()
count = sum(1 for word in words if word.lower() == 'the')
print("The word 'the' appears ", count, "times in the file")
print()

# Extract the numbers from the following phrase ## -------------------------------------------------------
phrase = f"In 1984 there were 13 instances of a protest with over 1000 people attending. On average there were 15 reported injuries at each event, with about 3 or 4 that were classifled as serious per event."
numbers = [int(x) for x in phrase if x.isdigit()] #add int to make string result into a digit/integer
print(numbers)






