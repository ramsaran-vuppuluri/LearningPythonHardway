states = {
    "Oregon":"OR",
    "Florida":"FL",
    "California":"CA",
    "New York":"NY",
    "Michigan":"MI"
}

cities = {
    "CA":"San Fancisco",
    "MI":"Detroit",
    "FL":"Jacksonville"
}

cities["NY"]= "New York"
cities["OR"]="Portland"

print "-"*10
print "NY state has",cities["NY"]
print "OR state has",cities["OR"]

print "-"*10
print "Michigan abbrevation is:",states["Michigan"]
print "Florida abbrevation is:",states["Florida"]

print "-"*10
print "Michigan has:",cities[states["Michigan"]]
print "Florida has:",cities[states["Florida"]]

print "-"*10
for state,abbrevation in states.items():
    print "%s is abbrevated as %s"%(state, abbrevation)

print "-"*10
for abbrevation,city in cities.items():
    print "%s state has %s"%(abbrevation,city)

print "-"*10
state = states.get("Texas",None)

if not state:
    print "Sorry, no Texas."

city = cities.get("TX","Does not exist.")
print "The city for the state 'TX' is: %s"%city
