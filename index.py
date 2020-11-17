import googlesearch
from googlesearch import search


# First we give a information about user agent
print(">> User agant :")
print(googlesearch.get_random_user_agent())


# Opening a connection and getting a list of search
try:
	response = list(search("python", num=10, stop=10, pause=2, safe="on"))
except (e,):
	print(f"> Error in {e}") # connection handeling

with open('python.txt', "w") as file: # save them into a file
    for result in response:
    	file.write(result + "\n")
  
# to search in an other way
query = "A computer science portal"

with open('test.txt', 'w') as file:
    try:  
    	for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
    		file.write(j + "\n") 
    except (e,):
    	print(f"> Error in {e}")


print("Done")
