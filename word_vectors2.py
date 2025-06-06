import gensim.downloader as api
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

print('loading the model...')
model = api.load("word2vec-google-news-300")
print('model loaded successfully.')

tech_words =[
    "programming", "software", "hardware", "network", "data",
    "database", "computer", "keyboard", "server", "algorithm"
]

vectors = [model[word] for word in tech_words]

pca = PCA(n_components=2)
vectors_2d = pca.fit_transform(vectors)

plt.figure(figsize=(8, 6))
for i, word in enumerate(tech_words):
    x, y = vectors_2d[i]
    plt.scatter(x, y, marker='o', color='blue')
    plt.text(x+0.02, y+0.02, word, fontsize=12)
plt.show()

word = input('Enter a word to get 5 most similar words:')
similar_list = model.most_similar(positive = [word], topn = 5)
for w in similar_list:
    print(w, '\n')
