This page is dedicated towards understanding the concept of LLM summarization and the resources used for this topic will be linked below.

- [LLM summarization](https://arize.com/blog/llm-summarization-getting-to-production/)
- [An Empirical Survey on Long Document Summarization: Datasets, Models and Metrics](https://arxiv.org/pdf/2207.00939)
- [5 Levels of summarization](https://www.youtube.com/watch?v=qaPMdcCqtWk)
- [Token counter](https://platform.openai.com/tokenizer)


### [What is LLM summarization](#)

LLM summarization is the use of LLMs to generate concise and informative summaries of longer texts. The benefits of summarization includes

1. Efficient information storage and retrieval
2. Better retention and understanding of the content because with summarization we remove extra or redundant information.

![[Summarization_Diagram.png]]

### [Usecases of LLM summarization](#)

- Grabbing core concepts spread across multiple documents
- Zoom AI meeting summary
- Amazon products review summary

### [LLM summarization approaches](#)

There are 2 fundamental type of summarization approaches, but other than these 2 the other one is hybrid which is combination of the below mentioned approaches.

| Extractive summarization                                                                          | Abstractive summarization                                                                             |
| ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Extract the exact sentences from the source document and combines them to create a final summary. | Understand the complete document and create a summary based on the concept mentioned in the document. |
| Existing content is used                                                                          | New content is generated                                                                              |


![[Summarization_Approaches.png]]

##### [Pros and Cons of Extractive summarization](#)

1. Pro : Since this approach utilize the exact content from the document thus the factual accuracy is high.
2. Con : It lacks creativity and summary is not very coherent because the independent sentences are just combined without considering the mutual relevance or coherence. 

##### [Pros and Cons of Abstractive summarization](#)

1. Pro : We get a human like summary
2. Con : Prone to some biasness


### [Hybrid approach](#)

The hybrid approach begins with an extractive phase, where the system identifies and selects crucial content from the source document.

Then, the hybrid approach transitions into an abstractive phase. Here, the system employs language processing techniques, such as LLM, to refine and enhance the extracted content.