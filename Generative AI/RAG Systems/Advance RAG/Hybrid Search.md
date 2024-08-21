This page is dedicated towards understanding the concept of the Hybrid search in RAG systems and all the resources that will be used will actually be linked below. Basically this topic comes under the Advance RAG, where we focus on improving the quality of response from the LLM.

- [Self Query Retrieval](https://youtu.be/f4LeWlt3T8Y?si=fPPgnb-yfSQE7prf)
- [TF-IDF, BM25 and SBERT](https://www.youtube.com/watch?v=ziiF1eFM3_4&t=5s)
- [Understanding the BM25](https://www.youtube.com/watch?v=ruBm9WywevM&t=4s)


### [Idea behind Hybrid search](#)

The main goal of using hybrid search is to enhance the quality of responses from language models. To achieve this, it's crucial to focus on the documents provided to the model as context for a given query. In traditional Retrieval-Augmented Generation (RAG) systems, context documents are retrieved from a vector database using semantic or vector search. In contrast, the hybrid search approach combines keyword-based search with vector search to improve the retrieval process.

`Hybrid search = Vector search (Dense vector) + Keyword based search (Sparse vector)`


### [Why include Keyword based search](#)

The primary advantage of keyword-based search is its ability to provide greater precision when exact terms are crucial for retrieving relevant documents. While semantic search focuses on understanding the overall meaning of a document and retrieving those with similar meanings, keyword-based search targets specific terms within documents. This makes keyword-based search particularly useful when precise terms are critical for relevance.

By combining both semantic and keyword-based search, you can significantly enhance the retrieval process, ensuring that you capture both the nuanced meanings and the exact terms necessary for finding the most relevant and important documents.


### [Which algorithms are used to create sparse vector search](#)

For creating sparse vector we utilize the frequency based word embedding techniques which includes TF-IDF and BM25, where BM25 is advance version of the TF-IDF technique. After creating the dense and spare vectors,

Cosine similarity measures the cosine of the angle between two vectors, which helps quantify how similar they are. For sparse vectors derived from TF-IDF or BM25, cosine similarity can be used to compare the query vector with document vectors.
