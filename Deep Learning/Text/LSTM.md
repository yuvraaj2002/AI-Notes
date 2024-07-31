This page is dedicated towards understanding the concept of LSTM in neural network and the resources used for understanding this topic will be linked below.

### [What do you mean by LSTM and why it got introduced ? ](#)

LSTM RNN stands for Long short term memory RNN and it is basically a variant of RNN which got introduced to cover the major drawback of RNN that was the problem of long term dependencies because of vanishing gradients. The way LSTM solves the issue of vanishing gradient is by introduction a new state along with the hidden state called cell state. 

![[Deep Learning/images/LSTM.png]]

With this new modification, the hidden state is now responsible for only storing the short term context and it is updated the with every time step, whereas the cell state is now responsible for storing the long term context which is updated via the gates (Input and forget gate) and in this way LSTM can better handle long term dependencies.

### [What do you mean by cell in LSTM](#)

A cell is a rectangular memory blocks which take 2 things as input ( Cell state and Hidden state )

### [What do you mean by gates in LSTM and explain working of each type of gate](#)

Gates in LSTM can simply be defined as set of mathematical operations which are used to update the the data stored in the cell state vector responsible for capturing the long term context. The updation involves adding new information and removing irrelevant information from the cell state.

In the LSTM there are 3 different gates called Input gate, Forget gate and Output gate. All of these 3 gates have their own roles and responsibilities. So let's take a look at each of them.

##### [Input Gate](#)

Input gate is the very first gate in the LSTM cell and it is responsible for adding new information from the current time step into the cell state. In the input gate there are 2 operations which are performed which gives us 2 vectors 

- Candidate cell state : Vector containing all the information from the current time step
- Input gate activation vector : Vector containing the importance form each piece information from current time step.

![[Deep Learning/images/Input_Gate.png]]

Finally both of these vectors are multiplied and by doing so only the important information from the current time step is retained and other information is removed. Finally this processed vector is adding to the cell state vector by vector addition operation. 

##### [Forget Gate](#)

Forget gate is the second gate which comes in the LSTM cell and it is responsible for removing the irrelevant information from the cell state.
The operation performed in this gate are

- Concatenating Input vector and previous time step hidden state vector
- Finding the weighted sum and passing them through the sigmoid function
- Finally adding the processed vector $f_t$ with the $C_t$ vector

![[Deep Learning/images/Forget Gate.png]]

ft vector is used to specify what percentage of the information must be retained by the cell state. For example: Ct = [ 2, 3 , 4] and ft = [ 0.1, 0.2 , 0.5 ], then Ct → [ 0.2 , 0.6 , 2.0 ]

##### [Output Gate](#)

Output gate is the 3rd and last gate in the cell and it is used for deciding what would be the output from the present cell.

![[Deep Learning/images/Output Gate.png]]

### [Working of LSTM (GIF)](#)

![[LSTM working.gif]]
### [What is the drawback of using LSTM and how it got solved ? ](#)

- Computationally expensive : LSTM have 3 gates and the usage of 3 gates make the overall architecture very much complex in nature, leading to a lot of trainable parameters making the network computationally expensive to train.
- Access to past information only: LSTM have unidirectional nature which means they primarily focus on past information up to the current time step. This limitation means that they do not have direct access to future information within the sequence.