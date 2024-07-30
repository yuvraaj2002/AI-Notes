This page is dedicated towards understanding the concept of Recurrent neural networks in deep learning and the resources used for this topic will be linked below.

### [What do you mean by RNN, where do we use it and why can't we use ANN or CNN instead of RNN](#)

RNN stands for recurrent neural networks and these are simply the type of neural networks which are specifically used with the data in which the sequence matters such as time series data or textual data. The unique thing about RNN is that it is feed forward neural network with feedback loop because of which it can maintain a short term memory called `hidden state` for the sequential data.

The reasons behind why we don't use ANN or CNN in place of RNN are mentioned below

1. ANN only works with fixed size input, so to make it work with the textual data which could of variable size we would need to do padding or truncation of the flattened vector both of which are not good, because padding would lead to increase in the computation and truncation would lead to loss of information.
2. Although CNNs can handle variable-size inputs to some extent using techniques like padding and pooling, they are primarily designed for spatial hierarchies data and are less efficient for capturing long-term dependencies in sequences.
3. Both ANN and CNN do not have any kind of feedback look thus they whole of the information needs to be passed in the single go and by doing so the sequential information gets lost.

![[Deep Learning/images/Why_ANN_notUsed.png]]

### [What are the types of RNN and where do we use them ? ](#)



### [How forward and backward propagation works in RNN](#)

### [Why do RNN have shared weights for each time step ? ](#)

### [What is the major drawback of RNN and the reason behind it](#)

### [How can we deal with the drawback of RNN](#)
