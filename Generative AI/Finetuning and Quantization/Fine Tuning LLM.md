This page is actually dedicated towards understanding the Fine tuning of a large language model and there are couple of resources which have been used to understand this concept, all of them are mentioned below.

- [LLM finetuning crash course](https://youtu.be/mrKuDK9dGlg?si=XMklV7kJWFaxKPbA)
- [Fine Tuning LLM Crash Course By Krish Naik](https://www.youtube.com/watch?v=iOdFUJiB0Zc)
- [Transformer Math 101](https://blog.eleuther.ai/transformer-math/)

3 approaches for training the LLM
- Pre-Training LLM
- Fine tuning
- LORA, Q-LORA

### [Pre-training](#)

- We need to have the massive text data [Tb] and after that we need to identify the model architecture.
- Need a Tokenizer to [Encode and decoding] the data (depends on task)
- Data is preprocessed using tokenizer vocabulary
	- Mapping the tokens to ids
	- Incorporating the special tokens

### [What happens in pretraining phase](#)

- Model learns to predict next word in the sentence
- Or it also fill-in missing words
- Fill in missing words is also called the Masked language model (where certain tokens are masked and model have to fill in the missing tokens by utilizing the surrounding tokens) whereas for generation is called the Causal language modeling (it focus on predicting the next token based on previous pattern or context)
- After pre-training (its capable of capturing general language but lacks specific knowledge about task or domain)

### [Fine tuning](#)

It allows us to specialize the LLM capabilities and optimize its performance on task specific dataset.

- Fine tuned model are also called Instruction tuned model : For this we task specific model we need dataset of instruction and response, such as question - answer pairs
- We try to optimize the task specific loss function 

### [LORA (Low rank adaptation)](#)

- Fine tuning is expansive
- To solve this LORA got introduced
- LORA = 3x memory requirement and to further we use QLORA, we use library called bitsandbytes. (Loss less quantization of LLM and then apply that using LORA technique)

Before QLORA we need16 A100 GPU : 80 GB each
with QLORA we need 2 RTX : 3090 or 1 A100

- LLAMA2 7B or Mistral 7B
- Memory : 150 - 195 GB
- Rent GPU : Runpod. VastAPI, Lambda Labs, AWS sagemaker, Google colab

Best is the Runpod
Cheapest is VastAI

- File size should be 10mb (Thumb of rule)























The reversal curse is like we ask gpt about something but when we ask gpt in reversed fashion we get different results, so to prevent this we need to make sure that the data is provided to the LLM from different perspectives so that it could build a good statistical representation of the data which could lead to better memorization.

![[Questions_creator.png]]

What we can do is to ask the LLM to provide rephrase of the query point which could be some statement or question/answer from different angles using different temperatures.

Talk about the hyper parameters 
- Model : Compare or analyze the performance without even using the RAG
### The need of Fine Tuning



### Techniques used for Fine Tuning 


##### LORA


