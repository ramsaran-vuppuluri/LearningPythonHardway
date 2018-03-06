from sys import argv

script,name = argv

print "Hi %s, I'm the %s script\n I'd like to ask you a few questions."%(name, script)

prompt = "-->"

print "Do you like me %s" %name
like = raw_input(prompt)

print "Where do you live %s" %name
location = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you sair %r about liking me.
You live in %r. Not sure where that is.\nAnd you have a %r computer. Nice.
"""%(like,location,computer)
