import nltk 
from nltk.sentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()
text = 'what a beautiful day to row a boat'
print(analyser.polarity_scores(text))

if analyser.polarity_scores(text)["compound"] > 0:
    print("Exudes positivity")
else:
    print("Negative nancy")