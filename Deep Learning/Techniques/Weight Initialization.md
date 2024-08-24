This page is dedicated towards understanding the concept and various techniques behind weight initialization in deep learning and the resources that I will be using will be mentioned below

- [Importance of Weight initialization and what not to do](https://www.youtube.com/watch?v=2MSY0HwH5Ss)
- [Techniques used for weight initialization](https://www.youtube.com/watch?v=nwVOSgcrbQI)

### [What is the importance of doing weight initialization ?](#)

If we want to improve the performance of the neural networks than other than focusing on optimizers, activation function, dropout and batch normalization, weight initialization is also an important factor which can affect the performance of neural network in term prediction and convergence speed. There are 3 problems which we encounter incase we don't focus on proper initialization of weights

1. Vanishing gradient
2. Exploding gradient
3. Slow convergence

### [How does weight initialization affect the training process of deep neural networks compared to shallow networks?](#)

Since deep neural network have relatively more number of hidden layers as compared to shallow network thus without proper weight initialization, the deep network are more prone to exploding gradient, vanishing gradients and slow convergence.

### [What are the various options for doing weight initialization](#)

- Initializing all the weights with 0
- Initializing all the weights with some constant value other than 0
- Randomly initializing using Standard normal distribution
- Using Xavier or Glorat initialization
- He initialization

### [Why we should not initialize weights as 0](#)

To study the impact of 0 weight initialization we we will be focusing on `Sigmoid`, `Tanh` and `Relu` activation function. Not only this for better understanding let us consider a neural network with only 2 input layer neurons, 1 hidden layer and 1 output layer.

![[Neural_Net_WI.png]](https://github.com/yuvraaj2002/AI-Notes/blob/master/Deep%20Learning/Images/Neural_Net_WI.png)

According to the neural network, a1 and a2 are basically the results after calculating the weighted sum and passing them through the activation functions.

$$a_1 = f(x_1*W_{11} + x_2*W_{21} + b_{11})$$
$$a_2 = f(x_1*W_{21} + x_2*W_{22} + b_{12})$$
Incase we are using 0 weight initialization technique then in that case, $W_{11},W_{12},W_{21},W_{22},b_{11},b_{12}$  all of these will be = 0
#### [For Relu Activation function](#)

Mathematically Relu is defined as $f(x) = max(0,x)$ and in case of 0 initialization a1 and a2 both are 0 thus during the weight updation process, when we will use the formula

$$W_{new} = W_{old} - Lr * ∂(L)/∂(W_{old})$$
The new weight will be equal to the old weight because the gradient will be 0 (We can understanding this by chain rule of differentiation). Now since both old and new weight will be same thus the training  will not happen at all.
#### [For Tanh Activation function](#)

Mathematically Tanh is defined as $f(x) = e^x - e^{-x}/e^x+e^{-x}$ and just like Relu the the a1 and a2 will also be 0 leading to no change in the old and new weights.

#### [For Sigmoid Activation function](#)

Mathematically Sigmoid is defined as $f(x) = 1/1 + e^{-x}$ and in this case the values of a1 and a2 will be 0.5. Now because of this the gradients of all the trainable parameters associated with a particular neuron will become same due to which our network will behave like it is having only single neuron in its hidden layer thus our network will never able to capture non linear pattern in the data.

![[0 Init Sigmoid issue.png]](https://github.com/yuvraaj2002/AI-Notes/blob/master/Deep%20Learning/Images/0%20Init%20Sigmoid%20issue.png)


### [Why we should not initialize weights as any constant value](#)

Rather than using 0, if we will be using some non zero constant value to initialize the weights then the gradients of all the trainable parameters associated with a particular neuron will become same due to which our network will behave like it is having only single neuron in its hidden layer thus our network will never able to capture non linear pattern in the data.

### [What are the issues associated with random value initialization](#)

Random initialization means we will be using the standard normal distribution to generate the weights for our neural network and when we do random initialization then there are 2 problems which we might face 

- Vanishing gradient : If the initial weights are too small, the gradients can become very small as they propagate backward through the layers, especially in deep networks, causing slow learning or no learning at all.
- Exploding gradient : If the initial weights are too large, the gradients can become excessively large, leading to unstable training and divergence.

To prevent both of these problems associated with random value initialization we use scaling techniques, where the scaling of the weight of some neuron is done based on the number of input and output from that neuron.
### [What are the various techniques used for doing weight initialization, explain each of them](#)

- **Xavier/Glorat Initialization**:
    
    - Designed for sigmoid and tanh activations.
    - Weights are drawn from Normal distribution with mean = 0 and standard deviation = $√2/n_{in}+n_{out}$
    
- **He Initialization**:
    
    - Designed for ReLU and its variants.
    - Weights are drawn from Normal distribution with mean = 0 and standard deviation = $√2/n_{in}$

```python
import numpy as np

# Example parameters
n_in = 100
n_out = 50

# Xavier/Glorot Initialization
def xavier_glorot_init(n_in, n_out):
    std_dev = np.sqrt(2 / (n_in + n_out))
    return np.random.normal(0, std_dev, size=(n_in, n_out))

# He Initialization
def he_init(n_in):
    std_dev = np.sqrt(2 / n_in)
    return np.random.normal(0, std_dev, size=(n_in, n_in))  # Assuming square weight matrix for simplicity

# Generate weights
xavier_weights = xavier_glorot_init(n_in, n_out)
he_weights = he_init(n_in)

print("Xavier/Glorot Weights:", xavier_weights)
print("He Weights:", he_weights)
```
