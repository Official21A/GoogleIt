import googlesearch
from googlesearch import search
from firewall import active


MAIN_DIR = "./docs/"

def user_agent():
	# Information about user agent
	print(">> User agant :")
	print(googlesearch.get_random_user_agent())


def safe_search(query, bound, output):
	# Opening a connection and getting a list of search
	try:
		response = list(search(query, num=10, stop=10, pause=bound, safe="on"))
	except Exception as e:
		print(f"> Error in :: {e}") # connection handeling
		response = []

	with open(f'{MAIN_DIR}{output}.txt', "w") as file: # save them into a file
		for result in response:
			if active(result):
				file.write(result + "\n")
  

def normal_search(query, bound, output):
	# To search in an normal way
    with open(f'{MAIN_DIR}{output}.txt', 'w') as file:
    	try:  
    		for j in search(query, tld="com", num=10, stop=10, pause=bound): 
    			file.write(j + "\n") 
    	except Exception as e:
    		print(f"> Error in :: {e}")