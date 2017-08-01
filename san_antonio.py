#Show random quote

#If user_answer is 'B' :
# - leave the program

# Else :
# - show another quote

#Function
def show_random_quote(my_list):
	#show another quote
	# TODO: get a random number
	item = my_list[0] # get a quote from a list. For the moment, just get the first one.
	print(item) # show the quote in the interpreter
	return "program is over" # returned value
	
#Variables
quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."] 
characters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "Kirikou"]

user_answer = "A"

while user_answer != "B":
	print(show_random_quote(quotes))
	user_answer = "B"
