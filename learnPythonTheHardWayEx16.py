fileName = raw_input("Enter file path")

print "We're going to erase %r."%fileName
print "If you don't wasnt press CTRL+C (^+C)."
print "If you want to continue press RETURN."
raw_input("?")

print "Opening the file"

file = open(fileName, 'w')

print "Truncating the file"
file.truncate()

print "Now I'm going to ask you for three lines:"

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these lines to the files"
file.write(line1+"\n"+line2+"\n"+line3+"\n")

print "And finally, we close it."

file.close
