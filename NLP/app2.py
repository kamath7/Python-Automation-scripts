from nltk.stem import WordNetLemmatizer
import nltk 
# nltk.download("punkt")
nltk.download('averaged_perceptron_tagger')
lemmatizer = WordNetLemmatizer()
sentence = "the quick brown fox jumped over the lazy dog"

#Tokenization
sentence_token = nltk.word_tokenize(sentence)
print(sentence_token)

# pos_tags = nltk.pos_tag(sentence_token)


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



print(sent_lemmati("i want to see the jog falls and spend some time eating"))