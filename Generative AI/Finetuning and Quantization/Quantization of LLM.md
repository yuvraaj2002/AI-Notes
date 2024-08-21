This page is actually dedicated towards the notes of the quantization techniques in Large language models and the resources used for this topic are mentioned below.

- [Krish Naik quantization video](https://youtu.be/6S59Y0ckTm4?si=SAhUwYs8Xy8YsclU)
- [A guide to quantization in LLM](https://symbl.ai/developers/blog/a-guide-to-quantization-in-llms/)

#### What is the need of doing quantization ? 

Basically if we want to run some LLM with millions and billions of parameters locally on our system or machine for inference then the basic need for getting a quick response from LLM is to have a high specs hardware including a good amount of RAM and a strong GPU for doing computation. 

Now since most of the individuals do not have access to high specs hardware to store LLM weights and perform computations using them, so the only way we can make running LLM locally on our machine possible is through quantization.

#### What is quantization at all  ?

Quantization is a model compression technique where we convert the model parameters from high precision data representation to low precision data representation. For example from Full precision 32 bit representation to 8 or 4 bit integer.

By doing quantization of LLM we can reduce the memory footprint of the LLM and computation power required by the LLM to give an output.

#### How Does Quantization Work?

In some cases, e.g., mapping a 64-bit or 32-bit float to a 16-bit float, as they share a representation scheme, this is more difficult in other instances. For example, quantizing a 32-bit float value to a 4-bit integer is complex. To do quantization we use a formula

$x_q = round(x/S + Z)$

- $x_q$ is quantized value
- x is original value
- S is scaling factor
- Z is zero point

#### Categories of LLM Quantization: PTQ and QAT

Even though there are a lot of quantization techniques but all those techniques falls under these 2 categories

- PTQ : PTQ stands for Post training quantization and it is a quantization technique which is applied to already trained LLM, now the major drawback of this technique is that it leads to data loss and loss of accuracy and precision of LLM.
- QAT : QAT stands for Quantization aware training and it is a type of technique where we start with pretrained model with full precision and then model is prepared for quantization by adding fake quantization nodes which simulate the effects of quantization during both the forward and backward passes, with this the model is fine tuned with the new data and after fine-tuning, the model is finally converted to a fully quantized version, where the weights and activations are stored in lower precision (e.g., int8).

### What Are the Advantages and Disadvantages of Quantized LLMs?

Let us look at the pros and cons of quantization.

### Pros 

- **Smaller Models**: by reducing the size of their weights, quantization results in smaller models. This allows them to be deployed in a wider variety of circumstances such as with less powerful hardware; and reduces storage costs.   
- **Increased Scalability**: the lower memory footprint produced by quantized models also makes them more scalable. As quantized models have fewer hardware constraints, organizations can feasibly add to their IT infrastructure to accommodate their use. 
- **Faster** **Inference**:  the lower bit widths used for weights and the resulting lower memory bandwidth requirements allow for more efficient computations. 

### Cons 

- **Loss of Accuracy:** undoubtedly, the most significant drawback of quantization is a potential loss of accuracy in output. Converting the model’s weights to a lower precision is likely to degrade its performance – and the more “aggressive” the quantization technique, i.e., the lower the bit widths of the converted data type, e.g., 4-bit, 3-bit, etc., the greater the risk of loss of accuracy.
