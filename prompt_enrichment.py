from langchain_cohere import ChatCohere
import gensim.downloader as api

model = api.load('word2vec-google-news-300')


llm = ChatCohere(
    cohere_api_key="o6DdGd0awe4vhcOEBS4r3RJOt0PdNB4iC60lIE40",
    temperature=0.6
)

prompt = 'generate a detailed story about an astronaut exploring a distant exoplanet'

words = ['astronaut', 'exploring', 'distant', 'exoplanet']

def get_similar_words(word):
    similar = model.most_similar(word, topn=3)
    similar_words =[]
    for tup in similar:
        similar_words.append(tup[0])
    
    print(similar_words)
    return similar_words

expanded_prompt = prompt

for word in words:
    similar_words = get_similar_words(word)
    expanded_prompt = expanded_prompt.replace(word, f"{word} ({','.join(similar_words)})")

print(f'original prompt: {prompt}')
print(f'enriched prompt: {expanded_prompt}')

print(llm.invoke(prompt).content)
print('/n')
print(llm.invoke(expanded_prompt).content)

