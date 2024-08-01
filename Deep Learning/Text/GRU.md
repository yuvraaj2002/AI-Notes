This page is dedicated towards understanding the concept of GRU in neural network and the resources used for understanding this topic will be linked below.

- [CampusX GRU](https://www.youtube.com/watch?v=QQfZAoNGQmE)

### [What do you mean by GRU and tell why it got introduced if we already had the LSTM ?](#)

GRU stands for gated recurrent unit and it is a further advancement over LSTM which got introduced in 2016 to cover the major drawback of LSTM. Basically LSTM had a very much complex architecture because of presence of 3 gates and 2 states (cells and hidden), so GRU simplified this architecture by only using 2 gates and single state.

### [What are the various gates present in the GRU and their functionality ?](#)

There are 2 gates which are present in GRU and both of them have their own roles mentioned below ⬇️

- Reset Gate: It is used to specify how much information from previous hidden state needs to be retained for the current time step.
- Update gate : It is used to update the content in the cell state by adding the relevant information from the current time step.

![[Deep Learning/images/GRU.png]]

##### [Reset Gate](#)

The reset gate is the very first gate which is present in the GRU cell and this gate is actually responsible for deciding how much past information needs to be retained for the current time step. The set of operations which are performed under this gate are 

1. Concatenating the previous hidden state vector and current time step embedding
2. Calculating their weighted sum and passing the result through sigmoid activation function.
3. Performing pointwise operation of this vector with ongoing hidden state

##### [Update Gate](#)



### [Why does the candidate hidden state calculated in the update gate is not added in the hidden state directly ?](#)
