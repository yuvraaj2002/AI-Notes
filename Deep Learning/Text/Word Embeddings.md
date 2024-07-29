After cleaning the raw text the next most important step is to make sure that we are providing correct numerical representation to the words, so that machines could efficiently capture the meaning of each word and also of the overall sentence. In this page we will first talk about the frequency based embedding techniques, followed by their drawback and finally about the prediction or neural network based embedding techniques.


### What do you mean by word embedding and what are the various approaches used ? 

Word embedding can simply be defined as the numerical representation of the word in form of vector and in order to create such vectors there are 2 main approaches which are being used

1. Frequency based techniques
2. Prediction or Neural Network Based techniques

The importance of word embeddings is that any machine learning or deep learning algorithms only understands numbers and since words are not in the correct format which such models expect so we need to give a numerical representation to such words so that machines could also understand what information is captured in the words.

### What do you mean by frequency based word embedding techniques and name them

Frequency based word embedding techniques are those techniques which utilize the frequency count of the word in the given document or vocabulary to provide the numerical representation to the word. There are 2 frequency based word embedding technique ⬇️

1. Bag Of Words
2. TF-IDF

### Explain working of BOW and its variants

BOW stands for bag of words and it is one of the most simplest frequency based word embedding technique where the word gets is numerical representation based on the frequency count of that word in the sentence or document. To better understand this let say we have a corpus with around 100 words. The vocabulary size = Dimensionality of the vector

1. Vocabulary words will be set up on the y axis as features and we will start going over the sentences or documents.
2. For every word in sentence we will mark its corresponding feature value with the number of times it came in the document/sentence. Otherwise the minimum feature value will be 0
3. The same process is repeated for all the documents and all the words

| Documents | He | She | good | boy | girl | listeners | speakers | Both |
|-----------|----|-----|------|-----|------|-----------|----------|------|
| He good boy | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| She good girl | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
| Both boy girl good listeners good speakers | 0 | 0 | 2 | 1 | 1 | 1 | 1 | 1 |

*In the above steps we discussed about the frequency based BOW but there is another variant of BOW which is binary BOW where we only focus on the presence of the word and not on occurrence*

| Documents | He | She | good | boy | girl | listeners | speakers | Both |
|-----------|----|-----|------|-----|------|-----------|----------|------|
| He good boy | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| She good girl | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
| Both boy girl good listeners good speakers | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |

```python
from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
documents = [
    "He good boy",
    "She good girl",
    "Both boy girl good listeners good speakers"
]

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Fit the model and transform the documents into a BOW representation
X = vectorizer.fit_transform(documents)

# Convert the BOW matrix to an array
bow_array = X.toarray()

# Get the feature names (vocabulary)
vocabulary = vectorizer.get_feature_names_out()

# Display the results
print("Vocabulary:\n", vocabulary)
print("\nBOW Array:\n", bow_array)

# Display the BOW matrix as a DataFrame for better readability
import pandas as pd

bow_df = pd.DataFrame(bow_array, columns=vocabulary)
print("\nBOW DataFrame:\n", bow_df)

```
### What is the major drawback of using BOW ? 

1. If the vocabulary size is very large then we will get very sparse or high dimensional vectors which increases the computational complexity
2. The vector do not capture the semantic information thus similar words do not have similar vector
3. It can't deal with out of vocabulary words

### Explain working of TF-IDF, also give reasons for why we take inverse and perform log operation ? 

TF-IDF is another frequency based word embedding technique which is much more better than BOW, as it uses both the term frequency and inverse document frequency of the given word to give a vector representation. To better understand this let us first understand what does TF and IDF means ⬇️

1. Term frequency : It is the ratio of frequency count of word in the document to total words in the document.
2. Inverse document frequency : It is the log of ( ratio of total documents in the corpus to total documents having the given word ).

*One of the most important question which comes related to this is that why we consider the inverse and take the log? . So the answer to this query is that by taking inverse we reduce the weightage or importance of common words because common words do not help us to distinguish the documents. And the log operation is applied for doing the smoothing so that we prevent giving too much importance to rare words and too less importance to common words.*

To better understand the idea behind doing inverse and taking log let us assume that there are total 10 documents in the corpus.

- For the rare word (Occurring in only 2 documents) : Its IDF without log will be $10/2 = 5$
- For the common word (Occurring in only 8 documents) : Its IDF without log will be $10/8 = 1.25$

*Now we can clearly see that even though we have been successful in assigning more importance to rare word and less importance to common word, but the weightage is very much loud, so just to smoothen them we do log operation on top*

- For the rare word (Occurring in only 2 documents) : Its IDF after log will be $log(10/2) = 0.69$
- For the common word (Occurring in only 8 documents) : Its IDF after log will be $log(10/8) = 0.09$

![Tf-IDF formula](https://github.com/yuvraaj2002/AI-Notes/blob/master/Deep%20Learning/Images/TFIDF%20formula.png)


```python
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "He good boy",
    "She good girl",
    "Both boy girl good listeners good speakers"
]

# Initialize the TfidfVectorizer
vectorizer = TfidfVectorizer()

# Fit the model and transform the documents into a TF-IDF representation
X = vectorizer.fit_transform(documents)

# Convert the TF-IDF matrix to an array
tfidf_array = X.toarray()

# Get the feature names (vocabulary)
vocabulary = vectorizer.get_feature_names_out()

# Display the results
print("Vocabulary:\n", vocabulary)
print("\nTF-IDF Array:\n", tfidf_array)

# Display the TF-IDF matrix as a DataFrame for better readability
import pandas as pd

tfidf_df = pd.DataFrame(tfidf_array, columns=vocabulary)
print("\nTF-IDF DataFrame:\n", tfidf_df)

```
### What is the major drawback of using TF-IDF ? 

1. The vector do not capture a lot of semantic information thus similar words do not have similar vector (even though better than BOW).
2. It can't deal with out of vocabulary words

### What do you mean by prediction based word embedding techniques and name them

Prediction based word embedding techniques are those techniques which utilize the neural network architecture for creating the word embeddings. The word "Prediction" comes from the fact that we try to solve a predictive task (such as predicting the target word by using the context words or vice versa) and as the byproduct of this predictive task we get the embeddings.

Now there are various prediction based word embedding techniques but the common ones are

1. Word2Vec
2. Fasttext
3. Glove
4. Elmo

### What problems are solved with prediction based embeddings ? 

1. **More semantic Information** : This embedding technique captures more semantic information of the words as compared to BOW and TF-IDF
2. **Low dimensional and dense vecto**r : The vector representation which we get after using this embedding technique not only gives us low dimensional vector but also gives us dense vector ( vector with less number of 0’s) as compared to the BOW and TF-IDF technique which makes the processing efficient.


### Explain Word2Vec, its architecture and working of both 

Word2Vec stands for Word To vectors and it is a neural network based technique where we try to solve a predictive task using neural network and as a byproduct of the solution we get the embeddings. Now based on the type of predictive task there are 2 different architectures

1. Predict target words give context words → `CBOW`
2. Predict context words given target word → `Skiagram`

#### Understanding the working of CBOW

To better understand the working of CBOW let us assume that assume that we have a sentence for which we want to create embeddings and this sentence is `Watch ABC channel for Data Science`. Now since CBOW solves a predictive task of predicting the target word using the Context words so we need to prepare dataset for training and for this we need to fix a window size. Let say our window size is of length 3.

I have created the below diagram using Excallidraw tool. You can checkout about this [here](https://excalidraw.com/)
![Data Preparation W2V](https://github.com/yuvraaj2002/AI-Notes/blob/master/Deep%20Learning/Images/Data%20Preparation%20W2V.png)

| Independent Data (Context words) | Dependent Data (Target word) |
| -------------------------------- | ---------------------------- |
| Watch, channel                   | ABC                          |
| ABC, for                         | channel                      |
| channel, Data                    | for                          |
| for, Science                     | Data                         |
Upto this point we know about the context words and the target words but still we need to do one hot encoding here because the neural network only understand the numbers. Thus after doing OHE our dataset will look something like

| Independent Data (Context words) | Dependent Data (Target word) |
| -------------------------------- | ---------------------------- |
| 1 0 0 0 0 0 , 0 1 0 0 0 0        | 0 0 1 0 0 0                  |
| 0 0 1 0 0 0 , 0 1 0 0 0 0        | 0 0 0 1 0 0                  |
| 0 1 0 0 0 0 , 0 0 0 1 0 0        | 0 0 0 0 1 0                  |
| 0 0 0 1 0 0 , 0 0 0 0 1 0        | 0 0 0 0 0 1                  |

Now since we have our input and output data ready with us so let us know train the network, where the input layer will have 12 neurons (Context words) and output layer will be having 6 neurons (Target word). `Note` There will be only single hidden layer and the number of neurons in this layer will represent the dimensionality we want.

![CBOW architecture](https://github.com/yuvraaj2002/AI-Notes/blob/master/Deep%20Learning/Images/CBOW%20architeture.png)

From the very first forward pass since the values will not be correct so the error will be calculated and accordingly the weights will be adjusted to make sure the error is minimized.

![CBOW_error.png](https://github.com/yuvraaj2002/AI-Notes/blob/master/Deep%20Learning/Images/CBOW_error.png)

Finally though the back propagation algorithm when the error will be minimized and we will start getting correct results at that point the training will be stopped and the connections from the hidden layer to output layer will represent the embedding for the given target word.

![CBOW_Output.png](https://github.com/yuvraaj2002/AI-Notes/blob/master/Deep%20Learning/Images/CBOW_Output.png)

```python
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import skipgrams
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Dot, Reshape, Dense
import numpy as np
import itertools

# Sample data
corpus = [
    "we are about to study the idea of a computational process",
    "computational processes are abstract beings that inhabit computers",
    "as they evolve processes manipulate other abstract things called data",
    "the evolution of a process is directed by a pattern of rules called a program",
    "people create programs to direct processes",
    "in effect we conjure the spirits of the computer with our spells"
]

# Preprocess the data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)
word2idx = tokenizer.word_index
idx2word = {v: k for k, v in word2idx.items()}
vocab_size = len(word2idx) + 1  # Adding 1 because of reserved 0 index

# Generate context-target pairs
def generate_context_target_pairs(corpus, window_size):
    pairs = []
    for sentence in corpus:
        words = sentence.split()
        for i, word in enumerate(words):
            target = word2idx[word]
            context = [word2idx[words[j]] for j in range(max(0, i - window_size), i)]
            context += [word2idx[words[j]] for j in range(i + 1, min(len(words), i + window_size + 1))]
            for ctx in context:
                pairs.append((target, ctx))
    return pairs

window_size = 2
pairs = generate_context_target_pairs(corpus, window_size)
pairs = np.array(pairs)

# Define the CBOW model
embedding_dim = 100

input_target = Input((1,))
input_context = Input((1,))

embedding = Embedding(vocab_size, embedding_dim, input_length=1, name='embedding')

target = embedding(input_target)
target = Reshape((embedding_dim, 1))(target)

context = embedding(input_context)
context = Reshape((embedding_dim, 1))(context)

dot_product = Dot(axes=1)([target, context])
dot_product = Reshape((1,))(dot_product)

output = Dense(1, activation='sigmoid')(dot_product)

model = Model(inputs=[input_target, input_context], outputs=output)
model.compile(loss='binary_crossentropy', optimizer='adam')

# Train the model
for epoch in range(10):
    loss = 0
    for pair in pairs:
        target_word = np.array([pair[0]])
        context_word = np.array([pair[1]])
        label = np.array([1])
        loss += model.train_on_batch([target_word, context_word], label)
    print(f'Epoch: {epoch + 1}, Loss: {loss}')

# Extract the word embeddings
word_embeddings = model.get_layer('embedding').get_weights()[0]
print(word_embeddings)

```

Just like this if we will reverse the predictive task we will be get architecture of the SkipGram

### How to choose right window size ? 

- **Larger Window Size (e.g., 5-10 words)**:
    
    - Useful for capturing relationships in tasks like document classification, sentiment analysis, where the overall context of the words matters.
    - Example: In the sentence "The quick brown fox jumps over the lazy dog," a larger window size would capture the relationship between "quick" and "lazy," which are not immediate neighbors.
    
- **Smaller Window Size (e.g., 2-3 words)**:
    
    - Useful for capturing syntactic relationships and dependencies in tasks like part-of-speech tagging, named entity recognition.
    - Example: In the same sentence, a smaller window size would focus on immediate neighbors like "quick" and "brown," "brown" and "fox," capturing tighter syntactic relationships.

### Out of CBOW and Skipgram which one should we use ? 

- **General Purpose Use:** Skip-Gram is often preferred for its ability to produce higher-quality embeddings, especially in applications where understanding the nuances of rare words is important.
- **High Efficiency Needs:** CBOW is a good choice when training speed and computational efficiency are more critical, particularly with very large datasets.

### What is the drawback of Word2Vec how it got solved ? 

- It can’t handle out of vocabulary words
- Word2vec considers a word as atomic unit thus it do not capture the morphological variations of words such as running and runs.

FastText is another prediction based word embedding architecture which is developed by FAIR that is Facebook AI research team. This architecture got introduced to cover the major drawbacks of Word2vec
