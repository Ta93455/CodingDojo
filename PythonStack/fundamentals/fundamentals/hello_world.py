# 1. TASK: print "Hello World"
print("Hello World ")
name = "Tommy"
print("Hello", name)
print("Hello" + name)
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello", name,"!")	# with a comma
print("Hello " + name+"!")	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", name,"!") 	# with a comma
print("hello" + name)	# with a +	-- this one should give us an error!

num = 13
print("Hello", num,"!")
print("Hello "+ num +"!") 
print("Hello "+str(num)+"!")
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1,fave_food2) ) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

fave_food3 = "burrito"
fave_food4 = "nachos"
print("I love to eat {}s and {}.".format(fave_food3,fave_food4) )
print(f"I love to eat {fave_food3} and {fave_food4}.")
