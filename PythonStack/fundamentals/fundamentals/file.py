num1 = 42    #variable declaration, numbers
num2 = 2.3   #variable declaration , number
boolean = True      #variable delcaration, boolean, type check
string = 'Hello World'    #variable declaration, Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# #5 variable declaration, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# #7 variable declaration, dictionary
fruit = ('blueberry', 'strawberry', 'banana')   #variable declaration, tuple
print(type(fruit)) #log statement , tuple
print(pizza_toppings[1])    #log statement, list access - initialize
pizza_toppings.append('Mushrooms')   #list - add value
print(person['name']) #log statement, access value
person['name'] = 'George'   #variable declaration, tuple access value, strings
person['eye_color'] = 'blue' #variable declaration, tuple access value , string
print(fruit[2]) #log statement, tuple- initialize 

if num1 > 45:       #conditional function , variable declaration , number
    print("It's greater")   #log statement , initialize string
else:       #conditional 
    print("It's lower")     #log statement , initialize string

if len(string) < 5:     #conditional function , length check , variable declaration, number
    print("It's a short word!")      #log statement, initialize string
elif len(string) > 15:      #conditional function , length check , variable declaration , number
    print("It's a long word!")      #log statement, initialize string
else:           #conditional
    print("Just right!")        #log statement, initialize string

for x in range(5):         #for loop variable declaration , function , number
    print(x)        #log statement  , variable 
for x in range(2,5):        #for loop, variable declaration, , function , number
    print(x)        #log statement, initialize variable
for x in range(2,10,3):     #for loop , variable declaration,function, number 
    print(x)        #log statement  ,  initialize variable
x = 0           #variable declaration, numbers
while(x < 5):   #while loop, variable declaration , number)
    print(x)        #conditional , initialize numbers
    x += 1      #variable delcaration , function , number 

pizza_toppings.pop()        #list - remove value 
pizza_toppings.pop(1)       #list - remove value = Array[1]

print(person)          #log statement , variable
person.pop('eye_color') #dictionary - remove value 
print(person)       #log statement , variable 

for topping in pizza_toppings:      #for loop, variable declaration ,  variable declaration 
    if topping == 'Pepperoni':      #conditional , variable declaration , strings
        continue        #for loop 
    print('After 1st if statement') #log statement, string
    if topping == 'Olives':     #conditional, variable declaration , string
        break           #for loop

def print_hello_ten_times():        #function, 
    for num in range(10):       #for loop , variable declaration,function parameter, number 
        print('Hello')      #log statement, initialize string

print_hello_ten_times()     #log statement,

def print_hello_x_times(x): #function
    for num in range(x): #for loop , variable declaration , function parameter , variable
        print('Hello')  #log statement , initialize string

print_hello_x_times(4)  #log statement, 

def print_hello_x_or_ten_times(x = 10):    #function , variable declaration, number
    for num in range(x):        #for loop , variable declaration , function parameter , variable
        print('Hello')      #log statement

print_hello_x_or_ten_times()        #log statement, initialize 1 times
print_hello_x_or_ten_times(4)       #log statement, initialize 4 times


"""
Bonus section
"""

# print(num3)           
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)