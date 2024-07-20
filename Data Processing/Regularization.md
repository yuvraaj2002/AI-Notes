[[Lasso Regression]]
[[Ridge Regression]]
[[Elastic Net Regression]]


##### L1 and L2 regularization in neural nets

Moreover, even though batch normalization was designed to solve the unstable gradients problems, it also acts like a pretty good regularizer. In this section we will examine other popular regularization techniques for neural networks: ℓ1 and ℓ2 regularization, dropout, and max-norm regularization.

Just like you did in Chapter 4 for simple linear models, you can use ℓ2 regularization to constrain a neural network’s connection weights, and/or ℓ1 regularization if you want a sparse model (with many weights equal to 0)

```python
layer = tf.keras.layers.Dense(100, activation="relu", kernel_initializer="he_normal", kernel_regularizer=tf.keras.regularizers.l2(0.01))
```

The l2() function returns a regularizer that will be called at each step during training to compute the regularization loss. This is then added to the final loss. As you might expect, you can just use tf.keras.regularizers.l1() if you want ℓ1 regularization; if you want both ℓ1 and ℓ2 regularization, use tf.keras.regularizers.l1_l2() (specifying both regularization factors).

Since you will typically want to apply the same regularizer to all layers in your network, as well as using the same activation function and the same initialization strategy in all hidden layers, you may find yourself repeating the same arguments. This makes the code ugly and error-prone. To avoid this, you can try refactoring your code to use loops. Another option is to use Python’s `functools.partial()` function, which lets you create a thin wrapper for any callable,

```python
from functools import partial 

RegularizedDense = partial(tf.keras.layers.Dense, activation="relu", kernel_initializer="he_normal", kernel_regularizer=tf.keras.regularizers.l2(0.01)) 

model = tf.keras.Sequential([ tf.keras.layers.Flatten(input_shape=[28, 28]),  RegularizedDense(100), RegularizedDense(100), RegularizedDense(10, activation="softmax") ])
```


##### Dropout in neural nets

Dropout is one of the most popular regularization techniques for deep neural net works. It was proposed in a paper26 by Geoffrey Hinton. It is a fairly simple algorithm: at every training step, every neuron (including the input neurons, but always excluding the output neurons) has a probability p of being temporarily “dropped out”, meaning it will be entirely ignored during this training step, but it may be active during the next step.

Neurons trained with dropout have to be as useful as possible on their own. They also cannot rely excessively on just a few input neurons; they must pay attention to each of their input neurons. They end up being less sensitive to slight changes in the inputs. In the end, you get a more robust network that generalizes better.

Another way to understand the power of dropout is to realize that a unique neural network is generated at each training step. Since each neuron can be either present or absent, there are a total of 2N possible networks (where N is the total number of droppable neurons). This is such a huge number that it is virtually impossible for the same neural network to be sampled twice. Once you have run 10,000 training steps, you have essentially trained 10,000 different neural networks, each with just one training instance. These neural networks are obviously not independent because they share many of their weights, but they are nevertheless all different. The resulting neural network can be seen as an averaging ensemble of all these smaller neural networks. In practice, you can usually apply dropout only to the neurons in the top one to three layers (excluding the output layer).

1. **Dropout Definition**: Dropout is a regularization technique used during training neural networks to prevent overfitting. It involves randomly setting a fraction ppp of the neurons to zero at each training step.
2. **Example Scenario**:
    - Suppose the dropout probability ppp is 75%. This means each neuron has a 75% chance of being dropped (set to zero) during each training step.
    - Consequently, only 25% of the neurons are active at each training step.
3. **Impact on Neurons During Training**:
    - During training, because of the dropout, the network learns with only 25% of neurons being active at any given step.
    - This helps the network not to rely too heavily on any single neuron and forces it to distribute learning more broadly across neurons.
4. **Post-Training Scenario**:
    - After training, dropout is turned off, meaning all neurons are active.
    - Since during training only 25% of neurons were active, each neuron post-training will now be connected to four times as many input neurons as it was during training.
5. **Adjusting Weights**:
    - To account for this difference, we need to adjust the input connection weights.
    - If we don't adjust, the neural network will not perform well because it will see a different input distribution during training and inference.
    - Specifically, each weight should be multiplied by four (or equivalently, divided by the keep probability, which is 1−p=0.251 - p = 0.251−p=0.25) during training.
    - This adjustment ensures that the scale of inputs remains consistent between training and inference.
6. **General Rule**:
    - More generally, to maintain consistency, the weights of the connections during training should be divided by the keep probability (1−p)(1 - p)(1−p).
    - For p=75%p = 75\%p=75%, the keep probability 1−p=0.251 - p = 0.251−p=0.25, so we divide weights by 0.25 (or multiply by 4) during training.

By applying this scaling, the neural network will handle the transition from training (with dropout) to inference (without dropout) smoothly, maintaining the learned patterns and performance.

Since dropout is only active during training, comparing the train ing loss and the validation loss can be misleading. In particular, a model may be overfitting the training set and yet have similar training and validation losses. So, make sure to evaluate the train ing loss without dropout (e.g., after training).