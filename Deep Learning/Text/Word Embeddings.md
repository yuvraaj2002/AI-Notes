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

![[Deep Learning/Images/TFIDF formula.png|400]]

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



