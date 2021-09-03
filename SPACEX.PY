from bs4 import BeautifulSoup  # extract data from beautiful soup lib
import urllib.request  # helps open url's
import nltk  # imports text processing lib
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/spacex') # fetches the specified url"S
html = response.read() 
soup = BeautifulSoup(html,"html.parser") # tokenization
text = soup.get_text(strip=True) #returns a copy of string
tokens = [t for t in text.split()]    #Tokenize a string to split 
freq = nltk.FreqDist(tokens)    #gives you the frequency of words within a text
for key,val in freq.items():
print(str(key)+':'+str(val))    #eparating Multiple Arguments
import nltk   # imports text processing lib
nltk.download('stopwords')    #downloads stopwords
from nltk.corpus import stopwords
stopwords.words('english')
clean_tokens = tokens[:]
sr = stopwords.words('english') 
for token in tokens:  # for loop 
    if token in stopwords.words('english'):
        clean_tokens.remove(token) # when the token matches with the stopwords it removes them
freq.plot(10,cumulative=False) # plots a graph for 10 high distribution words
