from sortedcontainers import SortedDict

def print_menu():
	print('1. Print Users')
	print('2. Add a User')
	print('3. Remove a User')
	print('4. Lookup a Phone Number')
	print('5. Quit')
	print()

# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

#display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user
	menu_choice = int(input("Type in a number (1-5): "))
    
    # view current entries
	if menu_choice == 1:
		try:
			print("Current Users: ")
			for x,y in usernames.items():
				print("Name: {} \tUser Name: {} \n".format(x,y))
		except IOError:
			print("Error: can't find file or read data")
		
    # add an entry
	elif menu_choice == 2:
		try:
			print("Add User")
			name = input("Name: ")
			username = input("User Name: ")
			usernames[name] = username
		except SyntaxError:
			print("What are you even putting in here?")
        
    # remove an entry
	elif menu_choice == 3:
		try:
			print("Remove User")
			name = input("Name: ")
			if name in usernames:
				#delete from the dictionary
				del usernames[name]
		except SyntaxError:
			print("What are you even putting in here?")

    # view user name      
	elif menu_choice == 4:
		try:
			print("Lookup User")
			name = input("Name: ")
			if name in usernames:
				#print the username
				print(usernames[name])
			else:
				#print that username not found
				print("username not found")
		except SyntaxError:
			print("What are you even putting in here?")
    
    # is user enters something strange, show them the menu
	elif menu_choice != 5:
		try:
			print_menu()
		except IOError:
			print("Error: can't find file or read data")