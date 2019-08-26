from bs4 import BeautifulSoup
import requests
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import requests
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 

a = SentimentIntensityAnalyzer()
url = "https://www.rottentomatoes.com/m/toy_story_4/reviews?type=user"
driver = webdriver.Chrome()
driver.get(url)

num =0
pos = 0
neg=0
while True:
	soup = BeautifulSoup(driver.page_source, 'html.parser')

	data = soup.find_all("p", {"class": "audience-reviews__review js-review-text clamp clamp-8 js-clamp"})
	tokenizer = RegexpTokenizer(r'[a-zA-Z]{3,}')

	stop_word = set(stopwords.words("english"))
	final=[]

	for item in data:
		words = tokenizer.tokenize(item.text)
		for w in words:
			w = w.lower()
			if w not in stop_word:
				final.append(w)
				num = num +1
				score = a.polarity_scores(w)
				if score['compound']>=0.05 :
					pos+=1
				elif score['compound']<= -0.05 :
					neg+=1
	
	try:
		driver.find_element_by_class_name("prev-next-paging__button-right").click()

	except :
        	break

pos_perc = (pos/num)*100
neg_perc = (neg/num)*100

print("Positive reviews are ", pos_perc)
print("Negative reviews are ", neg_perc)


p = nltk.FreqDist(final)
print("\n", p.most_common(10))






