This page will be dedicated towards understanding the concept of various chunking techniques which can be used for creating the chunks of the document before creating embeddings and storing them in the vector database. The resources that are being used are mentioned below.

- [5 Levels of Chunking techniques](https://www.youtube.com/watch?v=8OJC21T2SL4)
- [Chunking techniques](https://www.youtube.com/watch?v=pIGRwMjhMaQ&list=PLFEy2mailoA5ALfNHlHqraQ9kClDgOrVG&index=4)
- [Codes for Chunking techniques](https://mer.vin/2024/03/chunking-strategy/)
- [Agentic Chunking Using Llama 3 model](https://www.youtube.com/watch?v=FksDMgww_bw)

### [What is the importance of doing correct chunking ? ](#)

The quality of chunks in the RAG application significantly impacts the performance of the responses we get from the LLM. The thing is that in the RAG application we don't provide the complete document data as context to the LLM for answering the query; instead, we only focus on those chunks that contain the relevant information, and if the chunks do not hold the information necessary to answer the query accurately, the responses generated by the LLM may be incomplete or less accurate.

![[Chunking_Viz.png]]

In the above image we can clearly see that there are a lot of chunks which do not hold the necessary information and thus the LLM responses will also be either incomplete or inaccurate.
### [What are the various chunking techniques which are used?](#)

There are 5 chunking techniques which are being used and out of all these techniques the Agentic splitting gives us the best results because in this technique we utilize a Large language model to create the chunks.

1. Character text splitting
2. Recursive character splitting
3. Document specific splitting
4. Semantic Or Embedding splitting
5. Agentic Splitting

### [What is Character text splitter, its drawback and more advanced version of it ? ](#)

Character text splitter is one of the most simplest and inefficient chunking technique where fixed size chunks are created of specific character length, also in this technique just to ensure some level of cohesion between the chunks we specify the chunk_overlap.

```python
from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(chunk_size = 35, chunk_overlap=10, separator='', strip_whitespace=False)
documents = text_splitter.create_documents([text])
print(documents)
```

To cover the drawback of this, a new advance technique called Recursive character splitter got introduced where the other than creating chunks of specific character length the completeness of the word is also considered. Basically in the recursive character splitter the words are considered as a whole and the substring is not considered and in case considering the word as a whole exceed the token limit, the word is dropped.

Chunk size <= Chunk Limit

### [Semantic Chunking](#)



Ragas

https://hashnode.com/draft/66c986efdec9aaf021c68eff