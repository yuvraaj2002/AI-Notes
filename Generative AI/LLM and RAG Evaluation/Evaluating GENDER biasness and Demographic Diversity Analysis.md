This page is dedicated towards understanding the concept of gender biasness in large language models and how to actually measure the biasness.

- [Evaluating Biases in LLMs using WEAT and Demographic Diversity Analysis](https://www.youtube.com/watch?v=eTenkUPsjko&list=PLrLEqwuz-mRI5ubqVJ7DpbHheCflJDDXk&index=2)
- [Gender bias and stereotypes in Large Language Models](https://arxiv.org/pdf/2308.14921)


### [Fundamental Idea](#)

Even though LLM have shown State of the art results in a lot of domains and for a lot of problem statements, it is essential to evaluate the biasness of LLM towards gender stereotypes. This evaluation is important because currently the LLM powered applications are being used all over the globe and if the LLM responses will be biased towards some specific gender then it will significantly harm the mindset of general population.

### [How do we evaluate the gender biasness ? ](#)

There are basically 3 commonly adopted ways to evaluate the gender biasness of LLM's and these 3 approaches are :

1. WEAT test : **(Word Embedding Association Test)** is a common tool used to measure implicit bias in word embeddings, which are foundational to many LLMs.
2. Direct probing : This involves asking the LLM to generate text or complete tasks that require gender-related decisions. The responses can then be analyzed for bias.
3. Using benchmark dataset : Using datasets specifically designed to evaluate gender bias in LLMs, such as the Winogender Schemas




- This paper investigates LLMs’ behavior with respect to gender stereotypes, a known issue for prior models.
- As current LLMs show an impressive advancement in other domains, far exceeding SOTA, we ask here whether biases have been reduced or eliminated, too. This is particularly interesting in the context of the recent successes of Reinforcement Learning with Human Feedback (RLHF) [25], a methodology introduced to specifically encourage LLMs to avoid unwanted behavior.
- LLMs often use gender stereotypes. When asked to explain their choices, they often make excuses or claim that stereotypes are true. This shows how LLMs reflect the biases found in the data they were trained on. We need to understand why this happens and find ways to fix it.
- 