# 1. TASK: print "Hello World"
print( "Hello World" )

# 2. print "Hello Noelle!" with the name in a variable
name = "Leah"
print("My name is", name, "!" )	# with a comma
print("My name is" + name + "!")	# with a +


# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", name, "!")	# with a comma
print("Hello" + str(42) + "!")	# with a +	-- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}".format (fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string


# bonus print "I love rock climbinf and hiking."
love1 = "rock climbing"
love2 = "hiking"
print("I love %s and %s" % (love1, love2))