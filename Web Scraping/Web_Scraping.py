#Web_Scraping.py created by John Medeiros, 2021 for the: 2021 Complete Python Bootcamp From Zero to Hero in Python course taught by Jose Portilla on Udemy.com
#Features a list of small excercises using the bs4 and requests libraries, designed to practice web scraping in Python.
import bs4, requests

page = requests.get('http://quotes.toscrape.com/')

#Get names of all authors on the first page:
soup=bs4.BeautifulSoup(page.text,'lxml')
authors=set()
for i in range (0,len(soup.select('.author'))):
    authors.add(soup.select('.author')[i].getText())
print(authors)
print('\n')

#Create a list of all the quotes on the front page:
quotes=[]
for i in range (0,len(soup.select('.text'))):
    quotes.append(soup.select('.text')[i].getText())
print(quotes)

#Extract and print the top 10 tags:
for item in soup.select('.tag-item'):
    print(item.text)

#Grab the complete list of authors from the entire website:
base_url="https://quotes.toscrape.com/page/{}/."
page_num=1
authors=set()
valid=True
while valid:
    scrape_url=base_url.format(page_num)
    page_num+=1
    res = requests.get(scrape_url)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    if "No quotes found!" in res.text:
        valid=False
    else:
        for i in range (0,len(soup.select('.author'))):
            authors.add(soup.select('.author')[i].getText())
print(authors)