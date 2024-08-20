This page is dedicated towards my the notes related to langchain framework. The major source will obviously be the official langchain documentation, but here in this page/notes I will simply be explaining the things in my own simple language.

##### [Different Langchain components](#)


##### [LECL : Langchain Expression Language](#)

LECL allows us to chain runnables into a sequence using the `pipe (|)` operator and the sequence which we get is itself runnable, which means it can be invoked, streamed, or further chained just like any other runnable.

```
chain = prompt | llm | parser
```

RunnableWithMessageHistory wraps another Runnable and manages the chat message history for it; it is responsible for reading and updating the chat message history.

![[Pasted image 20240817185644.png]]