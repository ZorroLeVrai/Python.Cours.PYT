import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://fr.wikipedia.org/wiki/Suite_de_Fibonacci"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #titles = soup.find_all('textarea', id='read-only-cursor-text-area')
    titles = soup.find_all('title')

    # Titres
    print("Titres trouvés:")
    for title in titles:
        print(title.text)
else:
    print("Erreur. Status code:", response.status_code)
