people = 20
cats = 30
dogs = 15

if people<cats:
    print "Too many cats! The world is doomed!"
elif people>cats:
    print "Not many cats! World is saved."

if people < dogs:
    print "The world is drooled on!"
elif people > dogs:
    print "The world is dry!"

dogs+=5

if people >= dogs:
    print "People are greater than or equal to dogs."
elif people <= dogs:
    print "People are less than or equal to dogs."
elif people == dogs:
    print "People are dogs."
