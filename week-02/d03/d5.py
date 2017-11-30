# Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# OPTIONAL:
# The frist columns should be automatically as wide as the longest key

ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": True },
	{ "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": True },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": True },
	{ "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": True },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": False },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": False },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": True },
	{ "name": "soda", "in_stock": 0, "needs_cooling": True }
]

# looking for max length string in name
longitude = []

for o in range(len(ingredients)):
	longitude.append(ingredients[o]['name'])

l = max(len(x) for x in longitude)
k = len("Needs cooling")
j = len("In stock")



def draw(things):
	print("+-" + ((l+2) * "-") + "-+-" + (k * "-") + "-+-" + (j * "-") + "-+")
	print("| " + "Ingredient" + (((l-(len("Ingredient")))+2) * " ") + " | " + "Needs cooling" + ((k-(len("Needs cooling"))) * " ") + " | " + "In stock" + ((j-(len("In stock"))) * " ") + " |")
	print("+-" + ((l+2) * "-") + "-+-" + (k * "-") + "-+-" + (j * "-") + "-+")
	for i in range(len(things)):
		cooling = str(things[i]['needs_cooling'])
		stock = str(things[i]['in_stock'])
		if cooling == "False":
			cooling = "no"
		else:
			cooling = "yes"
		if stock == 0:
			stock = "-"
		print("|",things[i]['name'], (l-(len(things[i]['name']))) * " "," | ", cooling , ((k-(len(cooling)))-3) * " "," | ", stock, ((j-(len(stock)))-3) * " "," |",)
	print("+-" + ((l+2) * "-") + "-+-" + (k * "-") + "-+-" + (j * "-") + "-+")

draw(ingredients)