import gensim.downloader as api

print('loading model...')
model = api.load("word2vec-google-news-300")
print('model loaded successfully!')

king_vector = model['king']
print('The first 10 dimensions of king vector are: ')
print(king_vector[:10], "\n")

print("Top 10 words most similar to 'king':")
for word, similarity in model.most_similar('king'):
    print(f"{word}: {similarity:.4f}")
print()

result = model.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
print("Analogy - 'king' - 'man' + 'woman' ≈ ?")
print(f"Result: {result[0][0]} (Similarity: {result[0][1]:.4f})\n")