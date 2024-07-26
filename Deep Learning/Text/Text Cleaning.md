This page is dedicated towards understanding the various text cleaning techniques which we implement on the raw text, before creating embeddings or using some other pre-processing technique. Basically in this page we will first discuss about what are the various sources from where we generally get our data from and after that we will discuss each text cleaning processing sequentially.

### What are the various sources from where we can get our data from ? 

Data can be obtained from a wide variety of sources, depending on the nature of the project and the type of data required. Some common sources for acquiring data are :

1. Public datasets
2. Web scraping
3. API 
4. Internal databases

### Why do we even need to do text cleaning at all and what are the general steps? 

When we are working with text data coming from various sources, it is common to encounter "dirty" data, which includes inconsistencies, irrelevant information, and noise. Thus text cleaning is a crucial preprocessing step to ensure that the data is consistent and suitable for analysis and free from any irrelevant information for model training.

Now even though the specific steps will be very much unique to the data we are having at hand, because text cleaning is itself an art, but still there are some common steps which are being followed.

1. Tokenization : Break down the large sentences into smaller chunks for further data cleaning steps
2. Lowercasing : To reduce the ambiguity and unnecessary long vocabulary
3. Tags removal : When we do data scraping then generally tags also gets introduced in the data so we need to remove them
4. Emoji/ Special character encoding: When dealing with the social media data then we should encode the emoji's to capture the emotion represented by the emoji 
5. Stop word removal : To remove the words such as the, is etc
6. Punctuation removal :  To remove unnecessary punctuation

### What do you mean by tokenization and its types ? 

Tokenization is a data pre- processing step where we break down the text into smaller chunks for parsing and processing them easily. Tokenization itself is of different types 

1. Sentence level tokenization : Breakdown paragraphs into sentences
2. Word level tokenization : Breakdown the sentence into words
3. Character level tokenization : Breaking down words into characters

```python
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Ensure you have downloaded the necessary NLTK resources
nltk.download('punkt')

def tokenize_text(text):
    """
    Perform sentence, word, and character level tokenization on the input text.

    Parameters:
    text (str): The input text to be tokenized.

    Returns:
    dict: A dictionary with sentence, word, and character level tokenization.
    """
    
    # Sentence level tokenization
    sentences = sent_tokenize(text)
    
    # Word level tokenization
    words = word_tokenize(text)
    
    # Character level tokenization
    characters = list(text.replace(" ", ""))  # Removing spaces for characters only
    
    return {
        'sentence_level': sentences,
        'word_level': words,
        'character_level': characters
    }

# Example usage
text = "Tokenization is a data pre-processing step where we break down the text into smaller chunks for parsing and processing them easily. Tokenization itself is of different types."

tokenization_result = tokenize_text(text)

print("Sentence Level Tokenization:")
print(tokenization_result['sentence_level'])
print("\nWord Level Tokenization:")
print(tokenization_result['word_level'])
print("\nCharacter Level Tokenization:")
print(tokenization_result['character_level'])
```
### What are stop words and why do we even need to remove them ?

Stop words are those words which convey little or no information about the overall context of the document and by keeping the stop words only the vocabulary size increases and other than this there is no benefit. Example: is, a, the

```python
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# Sample sentence
sentence = "This is a sample sentence, showing off the stop words filtration."

# Tokenize the sentence
words = nltk.word_tokenize(sentence)

# Load English stop words
stop_words = set(stopwords.words('english'))

# Remove stop words
filtered_words = [word for word in words if word.lower() not in stop_words]

print("Original Sentence:", sentence)
print("Filtered Sentence:", ' '.join(filtered_words))
```

### Why it is always recommended to lowercase the words, also talk about thing to be careful about?

Lowercasing is another pre-processing which helps us to deal with the problem of unnecessary increase in vocabulary size. To better understand this let us assume that we are having words `hut` and `Hut` in some sentence, now from the human perspective we know that both of these words are conveying the same meaning but due to difference in the casing of the first character, the algorithm will consider them to be different words, thus it is recommended to lowercase the words.

Sometimes the words after lowercasing loose their actual information, for example words `us` and `US`➡️(America) after lowercasing both the words will represent collectiveness.

### What is need to stemming and lemmatization, also talk about what is the difference between them ?

Both stemming and lemmatization are pre-preprocessing techniques which involves reducing the inflection of the word to their base form so as to reduce unnecessary long vocabulary size leading to high computational complexity. From big picture if our data is small then we can use stemming due to its less computational requirement, but the exact difference is that

- Stemming use strict prefix-suffix truncating algorithm because of which sometime we may get the root word which do not make sense.
- Lemmatization do POS tagging and dictionary lookup to reduce the word to its base form and thus the root form always make a sense.

### What are the different types of stemming techniques which are used, which one is the most efficient ?

1. PorterStemmer : This is one of the most simplest type of stemming where a basic rule based suffix removal algorithm is used.
2. RegexStemmer : This type of stemming is used incase we want to remove suffix or prefix from the words by removing some specific data.
3. Snowball Stemmer : This is an advancement over porter stemmer and it is not only capable of supporting multiple languages but also use some more refined suffix stripping algorithm.

```python
from nltk.stem import PorterStemmer, SnowballStemmer, RegexpStemmer

# Sample words
words = ["running", "happiness", "caresses", "flying"]

# Initialize stemmers
porter_stemmer = PorterStemmer()
snowball_stemmer = SnowballStemmer("english")
regex_stemmer = RegexpStemmer("ing$|s$|ed$", min=4)  # Custom regex pattern

# Apply Porter Stemmer
print("Porter Stemmer:")
for word in words:
    print(f"{word} -> {porter_stemmer.stem(word)}")

# Apply Snowball Stemmer
print("\nSnowball Stemmer:")
for word in words:
    print(f"{word} -> {snowball_stemmer.stem(word)}")

# Apply Regex Stemmer
print("\nRegex Stemmer:")
for word in words:
    print(f"{word} -> {regex_stemmer.stem(word)}")

```

### What are the problems associated with stemming ? 

- Understemming : In Understemming our stemming algorithm don’t stem different words even though they are related to each other.
- Overstemming : his is basically a condition where our stemming algorithm stem different words to one stem , even though the words are not related to each other.

This is an example of overstemming where different words such as universal, university and universe are stemmed to common stem
![[Deep Learning/Images/Over_Stemming.png]]









