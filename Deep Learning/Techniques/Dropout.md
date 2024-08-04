This page is dedicated towards understanding the concept of dropouts in deep learning and the resources that I will be using will be mentioned below.

- [Introduction to Dropout](https://www.youtube.com/watch?v=gyTlcHVeBjM)

### [What do you mean by dropout, its need and how does this works ? ](#)

Dropout is basically a technique which is used to deal with the problem of overfitting in [[Artificial Neural Net]]. After using dropout our neural network behaves like some ensemble learning architecture where for every epoch we train a different neural network. 

The idea behind dropout is to randomly drop certain percentage of nodes from input and hidden layer per epoch and by doing so with every epoch we get a new neural network architecture which approach the data from a different perspective and in this way the decision boundary or the regression line get well generalized.

![[Dropout.png]](https://github.com/yuvraaj2002/AI-Notes/blob/master/Deep%20Learning/Images/Dropout.png)

#### [To ensure numerical coherence](#)

An important thing that we must keep in mind is that dropout is only applied during the training phase and not during the testing phase, so to keep the numerical coherence between training and testing phase we multiply the testing phase weights by (1-p), where p = dropout percentage.

The idea behind multiplying the testing phase weight by (1-p) is that, the weight only got utilized for (1-p) times out of 100 so we will only be considering a percentage of the weight and not the complete weight.


#### [Python Code](#)

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Define the neural network
def create_model(input_size, hidden_size, output_size, dropout_prob):
    model = Sequential()
    
    # Input layer
    model.add(Dense(hidden_size, input_dim=input_size, activation='relu'))
    
    # Dropout layer
    model.add(Dropout(dropout_prob))
    
    # Hidden layer
    model.add(Dense(hidden_size, activation='relu'))
    
    # Dropout layer
    model.add(Dropout(dropout_prob))
    
    # Output layer
    model.add(Dense(output_size, activation='softmax'))
    
    return model

# Parameters
input_size = 784  # For example, MNIST dataset
hidden_size = 128
output_size = 10  # Number of classes
dropout_prob = 0.5

# Create the model
model = create_model(input_size, hidden_size, output_size, dropout_prob)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Summary of the model
model.summary()

# Dummy data for demonstration
import numpy as np
X_train = np.random.rand(60000, input_size)
y_train = tf.keras.utils.to_categorical(np.random.randint(10, size=(60000, 1)), num_classes=output_size)

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
```

Keras automatically scales the weights by multiplying by `(1-p)`. Thus, you do not need to manually scale the weights during the testing phase.
