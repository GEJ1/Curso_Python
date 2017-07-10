import requests

i = 1

while i < 10:
	
	page = requests.get("https://www.ncbi.nlm.nih.gov/pubmed/" + str(i) + "?report=abstract&format=text")

	print(page.content)
	
	i = i + 1
