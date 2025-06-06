import gensim.downloader as api
from gensim.models import Word2Vec, word2vec
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk


medical_corpus = [
    "cardiovascular diseases are the leading cause of deaths worldwide",
    "Hypertension, or high blood pressure can lead to heart diseases",
    "diabetes is a chronic disease that affects the way the body processes sugar"
]

stop_words = set(stopwords.words('english'))
stop_words.add(',')

training_dataset =[]

for sentence in medical_corpus:
    tokens = word_tokenize(sentence)
    filtered = []
    for word in tokens:
        if word not in stop_words:
            filtered.append(word)
    training_dataset.append(filtered)
    
    
print(training_dataset)

word2vec_model = Word2Vec(vector_size=300, window=5, min_count=1, workers=4)
word2vec_model.build_vocab(training_dataset)

word2vec_model.save("medical_word2vec.model")
word2vec_model = Word2Vec.load("medical_word2vec.model")

print(word2vec_model.wv.most_similar("high"))
