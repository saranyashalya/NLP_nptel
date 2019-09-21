import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

# read the corpus
words = nltk.Text(nltk.corpus.gutenberg.words('bryant-stories.txt'))

# convert words to lowercase and remove stopwords
words = [word.lower() for word in words if word.isalpha()]
words = [word.lower() for word in words if word not in stop_words]

fdist = FreqDist(words)

for x,v in fdist.most_common(10):
    print(x,v)

for x,v in fdist.most_common(10):
    print(x,v/len(fdist))