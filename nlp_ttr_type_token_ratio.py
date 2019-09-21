import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

words_bryant = nltk.Text(nltk.corpus.gutenberg.words('bryant-stories.txt'))
words_emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))

# converting lower case
words_bryant = [word.lower() for word in words_bryant if word.isalpha()]
words_emma = [word.lower() for word in words_emma if word.isalpha()]

#removing stop words
words_bryant = [word.lower() for word in words_bryant if word not in stop_words][:15000]
words_emma = [word.lower() for word in words_emma if word not in stop_words][:15000]

TTR_bryant = len(set(words_bryant)) / len(words_bryant)
TTR_emma = len(set(words_emma)) / len(words_emma)

print("Number of words , Vocabulary and TTR for bryant ", len(words_bryant), len(set(words_bryant)), TTR_bryant)
print("Number of words "+str(len(words_emma)) +" Vocabulary "+str(len(set(words_emma)))+ " TTR emma " + str(TTR_emma))