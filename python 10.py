import nltk
stopword= nltk.corpus.stopwords.words('englsih')
stopwords.append ('retrived')
from wordcloud import wordcloud
import matplotlib.pyplot as plt
fie= open ('AI.text')
text =file.read()
wordcloud = wordcloiud (mode='RGB',
background_colour='white' , stopwords=stopwords,

max_words=100 , width=1500, height=1000).generate (text)
plt.imshow(wordcloud , interpolation='biliner')
plt.axis('off')
plt.show()
           


