accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

def search(c):
	for i in range(len(accounts)):
		if accounts[i]['account_number'] == c:
			print(accounts[i]['client_name'], accounts[i]['balance'])

search(23456311)
def trans(from_a, to_b, amount_):
	A = False
	B = False
	for i in range(len(accounts)):
		if accounts[i]['account_number'] == from_a:
			A = True
		if accounts[i]['account_number'] == to_b:
			B = True
	if A and B:
		for i in range(len(accounts)):
			if accounts[i]['account_number'] == from_a:
				accounts[i]['balance'] -= amount_
			if accounts[i]['account_number'] == to_b:
				accounts[i]['balance'] += amount_
	else:
		print(404)

search(4113546731)
search(23456311)

trans(2345346311, 4389546731, 56231234)

search(4123546731)
search(23456311)