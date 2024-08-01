This page is dedicated towards understanding the concept of GRU in neural network and the resources used for understanding this topic will be linked below.

- [CampusX GRU](https://www.youtube.com/watch?v=QQfZAoNGQmE)

### [What do you mean by GRU and tell why it got introduced if we already had the LSTM ?](#)

GRU stands for gated recurrent unit and it is a further advancement over LSTM which got introduced in 2016 to cover the major drawback of LSTM. Basically LSTM had a very much complex architecture because of presence of 3 gates and 2 states (cells and hidden), so GRU simplified this architecture by only using 2 gates and single state.

### [What are the various gates present in the GRU and their functionality](#)

There are 2 gates which are present in GRU and both of them have their own roles mentioned below ⬇️

- Reset Gate: It is used to specify how much information from previous hidden state needs to be retained for the current time step.
- Update gate : It is used to update the content in the cell state by adding the relevant information from the current time step.

![[Deep Learning/images/GRU.png]]

##### [Reset Gate](#)

The reset gate is the very first gate which is present in the GRU cell and this gate is actually responsible for deciding how much past information needs to be retained for the current time step. The set of operations which are performed under this gate are 

1. Concatenating the previous hidden state vector and current time step embedding
2. Calculating their weighted sum and passing the result through sigmoid activation function giving us $r_t$ vector
3. Performing pointwise operation $r_t$ vector with the $h_{t-1}$ vector
4. Finally concatenating the $x_t$ vector with $r_t * h_{t-1}$ vector , passing this through neural net layer with Tanh activation function to get candidate hidden state $h_t$

##### [Update Gate](#)

After reset gate there comes update gate which is actually responsible for updating the hidden state. Now the thing is that from the reset gate we get the candidate hidden state (which contains all the relevant and important information from the current time step) but since it is very much biased towards the current time step so we need to decide how much importance should we give to current time step information and on going hidden state vector.

For this we calculate is $z_t$ vector which is actually used to create the balance between the candidate hidden state and previous hidden state.

- If $z_t$ is high then more importance will be given to current time step information
- If $z_t$ is low then less importance will be given to current time step information

![[Deep Learning/images/Final Update Gate calculation.png]]


### [How do we deal with unidirectional problem with GRU ? ](#)

Gated Recurrent Units (GRUs), like other recurrent neural network architectures, are inherently unidirectional. This means that, at any given time step, a GRU can only access information from previous time steps and not from future time steps.

To overcome this limitation and provide access to future context, you can use a bidirectional GRU. In a bidirectional GRU, there are two separate GRU layers: one processes the input sequence from start to end (forward direction), and the other processes it from end to start (backward direction). The outputs of these two layers are typically concatenated or otherwise combined to provide a richer representation of the sequence, leveraging both past and future contexts.

Bidirectional GRUs are useful in tasks where understanding the full context of a sequence is important, such as in sequence labeling, machine translation, or text comprehension tasks.