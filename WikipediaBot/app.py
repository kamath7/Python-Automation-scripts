from nltk.stem import WordNetLemmatizer
import nltk 
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
long_sent = "Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked."
lemmatizer = WordNetLemmatizer()
question = "what are vegetables?"
def sent_lemmati(sent):
    sentence_token = nltk.word_tokenize(sent)
    pos_tags = nltk.pos_tag(sentence_token)
    sentence_lem = []
    for token, post_tag in zip(sentence_token,pos_tags):
        if post_tag[1][0].lower() in ['n','v','a','r']:
            lemma = lemmatizer.lemmatize(token,post_tag[1][0].lower())
            # print(lemma)
            sentence_lem.append(lemma)
        else:
            # print(token)
            pass
    return sentence_lem

def process(text, question):
    sentence_tokens = nltk.sent_tokenize(long_sent)
    sentence_tokens.append(question)
    tv = TfidfVectorizer(tokenizer=sent_lemmati)
    tf = tv.fit_transform(sentence_tokens)

    df = pd.DataFrame(tf.toarray(), columns=tv.get_feature_names())

    values = cosine_similarity(tf[-1],tf)

    index = values.argsort()[0][-2]
    values_flat = values.flatten()
    coeff = values_flat[-2]

    if coeff > 0.3:
        return (sentence_tokens[index])

while True:
    question = input("What knowledge can I impart on you today? Press N for exiting ")
    if question  == "N":
        break
    op = process(long_sent, question)
    if op:
        print(op)
    else:
        print("Check your input again")