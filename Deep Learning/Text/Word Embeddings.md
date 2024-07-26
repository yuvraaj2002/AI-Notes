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

### What is the major drawback of using BOW ? 

1. If the vocabulary size is very large then we will get very sparse or high dimensional vectors which increases the computational complexity
2. The vector do not capture the semantic information thus similar words do not have similar vector
3. It can't deal with out of vocabulary words

### Explain working of TF-IDF and its drawback ? 

### In TF-IDF while calculating the IDF why we take log?

### What do you mean by prediction based word embedding techniques and name them

