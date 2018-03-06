ten_things = "Apples Orange Crows Telephone Light Sugar"
print "Wait there are not 10 things in the list, lets fix that."

stuff = ten_things.split(" ")

more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

print stuff

while len(stuff)<=10:
    stuff.append(more_stuff.pop())

print stuff

print stuff[1]
print stuff[-1]
print stuff
print " ".join(stuff)
print "#".join(stuff[3:5])
