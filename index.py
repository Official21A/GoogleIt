import googlesearch
from googlesearch import search

import sys


def user_agent():
	# Information about user agent
	print(">> User agant :")
	print(googlesearch.get_random_user_agent())


def safe_search():
	# Opening a connection and getting a list of search
	try:
		response = list(search("python", num=10, stop=10, pause=2, safe="on"))
	except Exception as e:
		print(f"> Error in :: {e}") # connection handeling
		response = []

	with open('python.txt', "w") as file: # save them into a file
		for result in response:
			file.write(result + "\n")
  

def normal_search():
	# To search in an normal way
    query = "A computer science portal"

    with open('test.txt', 'w') as file:
    	try:  
    		for j in search(query, tld="com", num=10, stop=10, pause=2): 
    			file.write(j + "\n") 
    	except Exception as e:
    		print(f"> Error in :: {e}")


def execute(safe="off"):
	# Program executig
	user_agent()
	if safe == "on":
		safe_search()
	else:
		normal_search()
	print("Done")


# Program starts
if __name__ == "__main__":
	if len(sys.argv) == 1:
		execute()
	else:
		execute("on")