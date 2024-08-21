This page is dedicated towards understanding everything related to RAG architecture in generative AI and the resources that I will be using will be linked below. Majorly I will be using the official documentations along with Youtube videos.


### [What is RAG and why do we use it?](#)

RAG stands for Retrieval augmented generation and it is basically a framework which allows us to use the LLM over specific or sensitive data without having a need to fine tune the complete LLM. The overall idea behind using RAG system is that, rather than using the pre-existing knowledge of the LLM to answer our query about the specific data we will rather pass some context to the LLM along with the query and in this way the LLM will use the context to answer our query.

![[Rag_Diagram.png]](https://github.com/yuvraaj2002/AI-Notes/blob/master/Generative%20AI/RAG%20Systems/Basic%20RAG/Diagrams/Rag_Diagram.png)

### [What are the various components of the RAG](#)

There are basically 4 components in any of the RAG system and these are :

1.  **Text Splitter**: This component is responsible for splitting the text into chunks. We don’t send the complete data as context to the LLM because every LLM has a fixed-size context window. Additionally, only specific parts of the data are typically relevant, so creating chunks not only helps in dealing with the fixed-size context window of the LLM but also allows us to provide the most important pieces of information as context to the LLM.
2. **Embedder**: This component is responsible for giving numerical representations to the chunks and storing them in a vector database.
3. **Retriever**: This component is responsible for retrieving the most relevant chunks from the vector database given the user query.
4. **Generator**: This component is responsible for taking both the user query and the context data as input, passing them through the LLM, and providing the output.

