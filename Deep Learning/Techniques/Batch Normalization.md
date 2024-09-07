This page is dedicated towards understanding the concept of batch normalization in deep learning and the resources that I will be using will be linked below.

- [CampusX Video](https://www.youtube.com/watch?v=2AscwXePInA)

### [What do you mean by Batch normalization](#)

Batch normalization is a technique which is used to improve the convergence speed of the neural network and in the absence of batch normalization we will face the issue of slow convergence which basically means that it would take a lot of epochs to converge to the global minima of the cost function.

### [What do you mean by covariance shift ? ](#)

Covariance shift, is a term used in machine learning to describe a situation where the distribution of the input features (covariates) changes between the training and testing phases. This means that the data used to train the model has a different distribution compared to the data it encounters when making predictions.

### [Why does the convergence speed reduce in the absence of batch normalization](#)

Basically in the absence of batch normalization there is internal covariance shift in the neural network, which in more simpler terms means that the distribution of the input data (i.e. output of previous layer neurons) going into the hidden layer neurons gets changed, due to changing weights during the training and due to this change in distribution the neural network takes more number of epochs to converge to adjust to the new evolving data.

![[Batch Normalization.png]](https://github.com/yuvraaj2002/AI-Notes/blob/master/Deep%20Learning/Images/Batch%20Normalization.png)


### [How does batch normalization solves the issue](#)

In Batch normalization technique for the given batch of inputs, 

- The weighted sums are calculated (Output before activation)
- From the calculated outputs the mean and variance is calculated
- The outputs are normalized using the mean and variance
- Scale and shift normalized values using the alpha and beta values (learnable parameters) $yi​=γ*x_{Normalized}+β$
- Pass the value to the activation function

`Note` : After normalization the mean becomes 0 and standard deviation becomes 1 and while this is beneficial for stabilizing learning, it might not be the optimal transformation for every layer in the network. Some layers may benefit from a different mean and variance So to add this flexibility the scaling and shift is done to the normalized values.


### [Python Code](#)

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization, Activation

# Define the model
model = Sequential()

# Add a dense layer with batch normalization
model.add(Dense(64, input_shape=(128,)))
model.add(BatchNormalization())
model.add(Activation('relu'))

# Add another dense layer with batch normalization
model.add(Dense(32))
model.add(BatchNormalization())
model.add(Activation('relu'))

# Add the output layer
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Summary of the model
model.summary()
```

![[Pasted image 20240827053224.png]]

![[Pasted image 20240827053804.png]]