import googlesearch
from googlesearch import search

print(">> User agant :")
print(googlesearch.get_random_user_agent())

response = list(search("python", num=10, stop=10, pause=2, safe="on"))


with open('python.txt', "w") as file:
    for result in response:
    	file.write(result + "\n")
  
# to search 
query = "A computer science portal"

with open('test.txt', 'w') as file:  
    for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
    	file.write(j + "\n") 

print("Done")
