from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Carregar dados do CSV
justificativas = pd.read_csv('dados/request_anos_utf8.csv', usecols=[4], header=None).values.flatten()

# Pré-processamento do texto
stop_words = set(stopwords.words('portuguese'))
preprocessed_justificativas = []
for justificativa in justificativas:
    tokens = word_tokenize(justificativa.lower(), language='portuguese')
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    preprocessed_justificativas.append(" ".join(filtered_tokens))

# Extração de características
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_justificativas)

# Agrupamento
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
labels = kmeans.labels_

# Criar um dicionário para armazenar as palavras de cada cluster
clusters_words = {i: '' for i in range(kmeans.n_clusters)}

# Concatenar todas as justificativas de cada cluster
for i, justificativa in enumerate(preprocessed_justificativas):
    clusters_words[labels[i]] += justificativa

# Criar nuvem de palavras para cada cluster
plt.figure(figsize=(15, 10))
for i in range(kmeans.n_clusters):
    wc = WordCloud(width=800, height=400, background_color='white').generate(clusters_words[i])
    plt.subplot(1, kmeans.n_clusters, i+1)
    plt.imshow(wc, interpolation='bilinear')
    plt.title(f'Cluster {i}')
    plt.axis('off')

plt.show()
