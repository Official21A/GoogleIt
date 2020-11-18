import googlesearch
from googlesearch import search

import sys


def user_agent():
	# Information about user agent
	print(">> User agant :")
	print(googlesearch.get_random_user_agent())


def safe_search(query, bound):
	# Opening a connection and getting a list of search
	try:
		response = list(search(query, num=10, stop=10, pause=bound, safe="on"))
	except Exception as e:
		print(f"> Error in :: {e}") # connection handeling
		response = []

	with open('python.txt', "w") as file: # save them into a file
		for result in response:
			file.write(result + "\n")
  

def normal_search(query, bound):
	# To search in an normal way
    with open('test.txt', 'w') as file:
    	try:  
    		for j in search(query, tld="com", num=10, stop=10, pause=bound): 
    			file.write(j + "\n") 
    	except Exception as e:
    		print(f"> Error in :: {e}")


def command_input(argumenst):
	# To get the user input and check for the results
	# No input in command
	if len(argumenst) == 1:
		normal_search()
		return

	# Query to search
	if "-q" in argumenst:
		query = argumenst[argumenst.index("-q")+1]
	else:
		query = "google"
	
	# Time to wait for any searchings
	if "-t" in argumenst:
		bound = int(argumenst[argumenst.index("-t")+1])
	else:
		bound = 2

	# Safe search or not
	safe = "-s" in argumenst

	if safe:
		safe_search(query=query, bound=bound)
	else:
		normal_search(query=query, bound=bound)		
			

def execute(argumenst):
	# Program executig
	user_agent()
	command_input(argumenst)

	print("Done")
	


# Program starts
if __name__ == "__main__":
	execute(sys.argv)