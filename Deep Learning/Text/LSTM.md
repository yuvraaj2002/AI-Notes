This page is dedicated towards understanding the concept of LSTM in neural network and the resources used for understanding this topic will be linked below.

### [What do you mean by LSTM and why it got introduced ? ](#)

LSTM RNN stands for Long short term memory RNN and it is basically a variant of RNN which got introduced to cover the major drawback of RNN that was the problem of long term dependencies because of vanishing gradients. The way LSTM solves the issue of vanishing gradient is by introduction a new state along with the hidden state called cell state. 

![[Deep Learning/images/LSTM.png]]

With this new modification, the hidden state is now responsible for only storing the short term context and it is updated the with every time step, whereas the cell state is now responsible for storing the long term context which is updated via the gates (Input and forget gate) and in this way LSTM can better handle long term dependencies.

### [What do you mean by cell in LSTM](#)

A cell is a rectangular memory blocks which take 2 things as input ( Cell state and Hidden state )

### [What do you mean by gates in LSTM and also explain what are the different gates in LSTM](#)

Gates in LSTM can simply be defined as set of mathematical operations which are used to update the the data stored in the cell state vector responsible for capturing the long term context. The updation involves adding new information and removing irrelevant information from the cell state.

### [Explain the working of each of the gate in LSTM](#)

In the LSTM there are 3 different gates called Input gate, Forget gate and Output gate. All of these 3 gates have their own roles and responsibilities. So let's take a look at each of them.




### [What is the drawback of using LSTM and how it got solved ? ](#)
