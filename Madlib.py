noun_1 = input("Pick a noun: ")
adj_1 = input ("Pick an adjective: ")
adj_2 = input ("Pick an adjective: ")
clothing_type = input ("Pick a clothing type: ")
food = input("What's your favorite food? ")
number = input ("Choose a number: ")
body_part = input ("Choose a bodypart: ")
color = input ("Choose a color: ")
acessory = input ("Choose an acessory: ")
madlib = noun_1 + "s are " + adj_1 + ". I met one the other day. She wears (a/an) "
madlib = madlib + adj_2   + clothing_type  + "and eats " + food   + "every " + number  + "minutes.\n Sometimes her " + body_part    + "turns " +  color
madlib = madlib + ". She also carries " + adj_1     + acessory     + "everywhere she goes."

print(madlib)