def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r"%(arg1,arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r"%(arg1,arg2)

def print_one(argv):
    print "argv: %r"%argv

def print_none():
    print "I got nothing"

print_two("Ram","Saran")
print_two_again("Ram","Saran")
print_one("Ram Saran")
print_none
