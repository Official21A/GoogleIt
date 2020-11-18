import sys
from headers import safe_search, normal_search, user_agent
from utils import utils_init


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

	if "-o" in argumenst:
		output = argumenst[argumenst.index("-o")+1]
	else:
		output = query

	# Safe search or not
	safe = "-s" in argumenst

	if safe:
		safe_search(query=query, bound=bound, output=output)
	else:
		normal_search(query=query, bound=bound, output=output)		
			

def execute(argumenst):
	# Program executig
	# Files and folders check
	utils_init()
	# Start searching
	user_agent()
	command_input(argumenst)

	print("Done")
	


# Program starts
if __name__ == "__main__":
	execute(sys.argv)