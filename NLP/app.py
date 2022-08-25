from nltk.stem import WordNetLemmatizer
import nltk 

# nltk.download('wordnet')
# nltk.download('omw-1.4')
lemmatizer = WordNetLemmatizer()
lemma = lemmatizer.lemmatize("was","v")
print(lemma)

print(lemma == lemmatizer.lemmatize('is','v')) 