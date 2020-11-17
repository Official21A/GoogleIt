from googlesearch import search


response = list(search("python", num=10, stop=10, pause=2))

for result in response:
    print(result)
  
# to search 
query = "A computer science portal"
  
for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
    print(j) 
