This page is dedicated towards understanding the concept of Recurrent neural networks in deep learning and the resources used for this topic will be linked below.

### [What do you mean by RNN, where do we use it and why can't we use ANN or CNN instead of RNN](#)

RNN stands for recurrent neural networks and these are simply the type of neural networks which are specifically used with the data in which the sequence matters such as time series data or textual data. The unique thing about RNN is that it is feed forward neural network with feedback loop because of which it can maintain a short term memory called `hidden state` for the sequential data.

The reasons behind why we don't use ANN or CNN in place of RNN are mentioned below

1. ANN only works with fixed size input, so to make it work with the textual data which could of variable size we would need to do padding or truncation of the flattened vector both of which are not good, because padding would lead to increase in the computation and truncation would lead to loss of information.
2. Although CNNs can handle variable-size inputs to some extent using techniques like padding and pooling, they are primarily designed for spatial hierarchies data and are less efficient for capturing long-term dependencies in sequences.
3. Both ANN and CNN do not have any kind of feedback look thus they whole of the information needs to be passed in the single go and by doing so the sequential information gets lost.

![[Deep Learning/images/Why_ANN_notUsed.png]]

### [What are the types of RNN and where do we use them ? ](#)

Based on the nature of input and output data there are 4 different types of RNN which are used for different purposes.

1. `One to One RNN` : Single word classification
2. `One to Many RNN` : Image caption generation
3. `Many to One RNN` : Text classification, Sentiment Analysis
4. `Many to Many (Synchronous)` : POS tagging , Named Entity recognition
5. `Many to Many (Asynchronous)` : Text summarization, Machine translation 

![[Deep Learning/images/Types of RNN.png]]

### [How forward and backward propagation works in RNN](#)


### [Why do RNN have shared weights for each time step ? ](#)

There are 2 main reasons behind parameter sharing in RNN ⬇️

1. To prevent computational complexity : In case of RNN if different set weights will be used by every layer for every time step then the overall computationally complexity of the model will be increased significantly, because in case of RNN the data is being fed to the model in terms of time steps.
2. Temporal pattern recognition: By using shared parameters, RNNs can retain and capture information spread across multiple time steps efficiently. If different weights were used for every time step, the model would learn something new and disassociated from the previous time steps at each step.

### [What is the major drawback of RNN and the reason behind it, explain it in details and how it got solved](#)

The major drawback of RNN is that it have a short term memory, which basically means that after certain number of time steps (generally after 10 time steps) RNN starts loosing the context of the complete data and this happens due to `vanishing gradient problem`.

![[Deep Learning/images/Dependnecy_Issue.png]]

The vanishing gradient problem is one of the most common issues in neural networks, where the gradients become so small that they start hampering the training process during backpropagation. To be more precise, the gradients become small due to the use of certain activation functions such as sigmoid, tanh, and ReLU. Both tanh and sigmoid are saturating activation functions, meaning they compress the input to a very small output, and their derivatives also produce small outputs. During backpropagation, when we calculate the gradients using the chain rule of differentiation, we obtain very small gradients. As a result, when we update the weights, the new weights are very similar to the old weights, leading to slow convergence or stopping the training prematurely due to a false indication of finding the global minimum.

![[Deep Learning/images/Vanishing_Gradient.png]]

To tackle this researchers started using relu which is comparatively less saturating but relu itself also suffer from the dying relu problem. So rather than using relu we can use different variants of relu, but all in all we use a more advanced version of RNN which is called [[LSTM]] which captures both the short term and long term context of input data.
