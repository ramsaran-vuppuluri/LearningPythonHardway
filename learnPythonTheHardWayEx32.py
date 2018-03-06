the_count = [1,2,3,4,5]
fruits = ["apple","orange","pears","apricots"]
change = [1,"pennies",2,"dimes",3,"quaters"]

for number in the_count:
    print "This is the count %d"%number

for fruit in fruits:
    print "This is the fruit: %s"%fruit

for i in change:
    print "I got %r"%i

elements = range(0,6)

for i in range(0,6):
    print "Adding %d to the list"%i
    elements.append(i)

for ele in elements:
    print "Element was: %d"%ele
