This page is dedicated towards understanding the concept of the Hybrid search in RAG systems and all the resources that will be used will actually be linked below. Basically this topic comes under the Advance RAG, where we focus on improving the quality of response from the LLM.

- [Weviate Hybrid search explained](https://weaviate.io/blog/hybrid-search-explained)
- [Weviate fusion algorithm explained](https://weaviate.io/blog/hybrid-search-fusion-algorithms)
- [Self Query Retrieval](https://youtu.be/f4LeWlt3T8Y?si=fPPgnb-yfSQE7prf)
- [TF-IDF, BM25 and SBERT](https://www.youtube.com/watch?v=ziiF1eFM3_4&t=5s)
- [Understanding the BM25](https://www.youtube.com/watch?v=ruBm9WywevM&t=4s)



### [Idea behind Hybrid search](#)

The main goal of using hybrid search is to enhance the quality of responses from language models. To achieve this, it's crucial to focus on the documents provided to the model as context for a given query. In traditional Retrieval-Augmented Generation (RAG) systems, context documents are retrieved from a vector database using semantic or vector search. In contrast, the hybrid search approach combines keyword-based search with vector search to improve the retrieval process.

`Hybrid search = Vector search (Dense vector) + Keyword based search (Sparse vector)`


### [Why include Keyword based search](#)

While semantic search focuses on understanding the overall meaning of a document and retrieving those with similar meanings, keyword-based search targets specific terms within documents. This makes keyword-based search particularly useful when precise terms are critical for relevance.

By combining both semantic and keyword-based search, you can significantly enhance the retrieval process, ensuring that you capture both the nuanced meanings and the exact terms necessary for finding the most relevant and important documents.


### [Which algorithms are used to create sparse vector search](#)

Sparse embeddings are generated from algorithms like [BM25](https://en.wikipedia.org/wiki/Okapi_BM25) and [SPLADE](https://arxiv.org/abs/2107.05720). Dense embeddings are generated from machine learning models like [GloVe](https://text2vec.org/glove.html) and [Transformers](https://huggingface.co/docs/transformers/index).


