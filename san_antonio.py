import random

quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]

characters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "Kirikou"]


def get_random_item(my_list):
    rand = random.randint(0,10)# get a random number
    item = my_list[rand] # get a quote from a list
    return item # return the item


def capitalize(words):
    for word in words:
        return word.capitalize()


def message(character, quote):
    n_character = capitalize(character)
    n_quote = capitalize(quote)
    return "{} a dit : {}".format(n_character, n_quote)


user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')


while user_answer != "B":
    print(message(get_random_item(characters), get_random_item(quotes)))
    user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')


